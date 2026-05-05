import streamlit as st
import os
import cv2
from PIL import Image
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision.models import efficientnet_b0, EfficientNet_B0_Weights
from ultralytics import YOLO

# -------------------------
# CONFIGURATION
# -------------------------
IMAGE_FOLDER = "dataset/demo_images"
YOLO_MODEL_PATH = "models/best.pt"
CLASSIFIER_MODEL_PATH = "models/classifier/efficientnet.pth"

CLASS_NAMES = [ 
    'bollards_1_serbia', 
    'bollards_singapore_1',
    'bollards_vietnam_1', 
    'sidewalks_1_india', 
    'sidewalks_1_thailand', 
    'sidewalks_2_thailand', 
    'sidewalks_3_thailand', 
    'sidewalks_singapore_1', 
    'sidewalks_vietnam_1'
] #smaller set

# -------------------------
# TRANSFORM
# -------------------------
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# -------------------------
# CLASSIFIER BUILDER
# -------------------------
def load_classifier(model_path, num_classes):
    weights = EfficientNet_B0_Weights.DEFAULT
    model = efficientnet_b0(weights=weights)

    model.classifier[1] = nn.Linear(
        model.classifier[1].in_features,
        num_classes
    )

    state_dict = torch.load(model_path, map_location="cpu")
    model.load_state_dict(state_dict)

    model.eval()
    return model

# -------------------------
# LOAD CACHED MODELS
# -------------------------
@st.cache_resource
def load_models():
    yolo_model = YOLO(YOLO_MODEL_PATH)
    classifier = load_classifier(CLASSIFIER_MODEL_PATH, len(CLASS_NAMES))
    return yolo_model, classifier

yolo_model, classifier = load_models()

# -------------------------
# UI
# -------------------------
st.title("Object detection and classification using YOLOv8m and EfficientNet-B0")

if "selected_image" not in st.session_state:
    st.session_state.selected_image = None

# -------------------------
# LOAD IMAGES
# -------------------------
image_files = [
    f for f in os.listdir(IMAGE_FOLDER)
    if f.lower().endswith((".png"))
]

image_paths = [os.path.join(IMAGE_FOLDER, f) for f in image_files]

# -------------------------
# IMAGE GRID
# -------------------------
st.subheader("Select an image")

cols = st.columns(4)

for i, img_path in enumerate(image_paths):
    with cols[i % 4]:
        img = Image.open(img_path)

        selected = st.session_state.selected_image == img_path

        st.image(
            img,
            use_container_width=True,
            caption="Selected" if selected else None
        )

        if st.button("Select", key=f"img_{i}"):
            st.session_state.selected_image = img_path

selected_image_path = st.session_state.selected_image

# -------------------------
# INFERENCE PIPELINE
# -------------------------
if selected_image_path:

    st.divider()
    st.subheader("Inference Results")

    img = cv2.imread(selected_image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    st.image(img_rgb, caption="Input Image", use_container_width=True)

    # -------------------------
    # YOLO DETECTION
    # -------------------------
    st.write("Running YOLO...")

    results = yolo_model(img_rgb)

    if len(results) == 0 or results[0].boxes is None:
        st.warning("No detections found.")
        st.stop()

    boxes = results[0].boxes.xyxy.cpu().numpy()

    if len(boxes) == 0:
        st.warning("No objects detected.")
        st.stop()

    annotated = img_rgb.copy()
    crops = []

    for box in boxes:
        x1, y1, x2, y2 = map(int, box)

        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(img.shape[1], x2), min(img.shape[0], y2)

        crop = img[y1:y2, x1:x2]

        if crop.size == 0:
            continue

        crops.append(crop)

        cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 2)

    st.image(annotated, caption="Detections", use_container_width=True)

    # -------------------------
    # EFFICIENTNET CLASSIFICATION
    # -------------------------
    st.write("Running classifier...")

    for i, crop in enumerate(crops):

        st.image(
            cv2.cvtColor(crop, cv2.COLOR_BGR2RGB),
            caption=f"Crop {i}",
            use_container_width=True
        )

        input_tensor = transform(crop).unsqueeze(0)

        with torch.no_grad():
            outputs = classifier(input_tensor)
            probs = torch.softmax(outputs, dim=1)
            pred_idx = torch.argmax(probs, dim=1).item()

        label = CLASS_NAMES[pred_idx]
        confidence = probs[0][pred_idx].item()

        st.success(f"{label} ({confidence:.2f})")
        st.markdown(f"### Image: `{os.path.basename(selected_image_path)}`")