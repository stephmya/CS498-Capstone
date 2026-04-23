import os
import torch
import torch.nn as nn
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
from torchvision.models import efficientnet_b0, EfficientNet_B0_Weights

transform = transforms.Compose([ # transform resize and tensor conversion
    transforms.Resize((224, 224)), #fixed reso
    transforms.ToTensor()
])

train_dataset = datasets.ImageFolder(
    "dataset/classifier/crops/train",
    transform=transform
)

val_dataset = datasets.ImageFolder(
    "dataset/classifier/crops/val",
    transform=transform
)

print(len(train_dataset.classes))
print(train_dataset.classes[:20])
num_classes = len(train_dataset.classes)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32)
# efficientnet does compound scaling so small is reasonable
weights = EfficientNet_B0_Weights.DEFAULT
model = efficientnet_b0(weights=weights)

model.classifier[1] = nn.Linear( # replacing for class #
    model.classifier[1].in_features,
    num_classes
)

device = "cuda" if torch.cuda.is_available() else "cpu" #sanity
print(f"Using device: {device}")
model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

for epoch in range(10): # 10 was optimal balance again 
    model.train()
    total_loss = 0

    for imgs, labels in train_loader: 
        imgs, labels = imgs.to(device), labels.to(device)

        outputs = model(imgs)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch} Loss: {total_loss:.4f}")

torch.save(model.state_dict(), "models/classifier/efficientnet.pth")

model.eval()
correct = 0
total = 0

with torch.no_grad():
    for imgs, labels in val_loader:
        imgs, labels = imgs.to(device), labels.to(device)

        outputs = model(imgs)
        _, preds = outputs.max(1)

        total += labels.size(0)
        correct += (preds == labels).sum().item()

acc = 100 * correct / total
print("Val Accuracy:", acc)
print("Classifier training complete.")