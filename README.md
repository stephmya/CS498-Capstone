## Key Takeaways:
 - Using YOLO for object detection/localization and EfficientNet for classification showed how modular models can be integrated into a single pipeline fairly efficiently. Use was reasonably straight forward and working with existing documentation was a good learning experience. 
 - The dataset was not perfect by any means, but the models still learned with pretty good acuracy. If I were able to change anything, it would be collecting more data and distinct variants of objects for classification. The postboxes were particularly difficult to train on and I ended up nixing them from the dataset because they were not distinct enough to be classified correctly. 
 - The interactive web app was a fun way to test the model on new images. Not perfect but super simple and efficient.



## Quickstart Instructions:
Create Conda Environment:
Using Python 3.9 because labelImg is not compatible with python 3.11

```
conda create -n geoCV python=3.9 -y
```
```
conda activate geoCV
```

```
pip install ultralytics timm opencv-python neo4j scikit-learn numpy streamlit
```
```
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
```

can also install: ```pip3 install torch torchvision```
for mac/no NVIDIA card.
This works best with cuda enabled gpu, no guarantees on cpu only.


#### CPU/Mac PyTorch
Default installation:

```
pip3 install torch torchvision

---------------------------------------------------------------------------------
### The Pipeline! 

1. Detection using YOLOv8 from ultralytics
2. Classification using EfficientNet from timm

## Image Preprocessing:
1. resize screenshots with ```python src/resize_images.py```
2. Rename screenshots with ```python src/title_images.py``` by folder to add country, object type, varinant, and index. 
3. Use labelImg to label
4. Distribute into train/val folders


### processing pipeline:
1. Run the YOLOv8 training script to train the object detector on the dataset:```python src/train_yolo.py``` 
2. Run the cropping script to crop the original images into individual objects for classification, using the bounding boxes from the YOLOv8 annotations:```python src/parse_labels.py```
3. Run the cropping script to crop the original images into individual objects for classification, using the bounding boxes from the YOLOv8 annotations:```python src/crop_dataset.py```
4. Run the classification training script to train the EfficientNet classifier on the cropped images:
```python src/train_classifier.py```

5. then you can run the interactive web app to test the model on new images:
```streamlit run app.py```

---------------------------------------------------------------------------------

### File Structure:
```
├───dataset
│   ├───classifier
│   │   └───crops
│   │       ├───train
│   │       └───val
│   ├───demo_images
│   └───detection
│       ├───images
│       │   ├───train
│       │   └───val
│       └───labels
│           ├───train
│           └───val
├───models // model files
│   └───classifier
├───runs 
├───scripts //image preprocessing scripts
└───src //primary
```

---------------------------------------------------------------------------------
## Data Summary: 
some image sets are minimized in the actual dataset due to near identical variants or lack of distinct features for the post boxes.
### Bollards: 
some overlapping visuals
| Country     | Variants | Images per Variant | Total Images |
|-------------|----------|--------------------|--------------|
| Monaco      | 2        |  100x2             |      200     |
| Vietnam     | 2        |  100x2             |      200     |
| Singapore   | 3        |  100x2             |      300     |
| Serbia      | 3        |  100x3             |      300     |
| Thailand    | 6        |  100x6             |      600     |
| India       | 7        |  100x7             |      700     |
| Laos        | 4        |  100x4             |      400     |
| Philippines | 2        |  100x2             |      200     |

### Sidewalks: 
slight reduction due to overlapping visuals
| Country     | Variants | Images per Variant | Total Images |
|-------------|----------|--------------------|--------------|
| Monaco      | 0        |                    |       0      |
| Vietnam     | 1        |  100               |      100     |
| Singapore   | 1        |  100               |      100     |
| Serbia      | 0        |                    |       0      |
| Thailand    | 3        |  100x3             |      300     |
| India       | 3        |  100x3             |      300     |
| Laos        | 3        |  100x3             |      300     |
| Philippines | 1        |  100               |      100     |

### Post Boxes: /// post boxes have been nixed. They did not end up being distinct enough to identify correctly. big post box shaped blob in a big blob world.
| Country     | Variants | Images per Variant | Total Images |
|-------------|----------|--------------------|--------------|
| Monaco      | 3        |  100x3             |     300      |
| Vietnam     | 4        |  100x4             |     400      |
| Singapore   | 3        |  100x3             |     300      |
| Serbia      | 7        |  100x7             |     700      |
| Thailand    | 2        |  100x2             |     200      |
| India       | 6        |  100x6             |     600      |
| Laos        | 2        |  100x2             |     200      |
| Philippines | 1        |  100               |     100      |



---------------------------------------------------------------------------------
### Distinct Object classifications are validated against:
https://geohints.com/, 
https://geohints.com/meta/bollards, 
https://geohints.com/meta/sidewalks, 
https://geohints.com/meta/postBoxes

Geohints is a community database for GeoGuessr "meta" or country-specific identifying information. 

Data for this project was independently collected.


### Primary Resources used:

https://docs.streamlit.io/
https://docs.ultralytics.com/
https://www.geeksforgeeks.org/computer-vision/efficientnet-architecture/



