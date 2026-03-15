## Quickstart Instructions:
Create Conda Environment:
Using Python 3.9 because labelImg is not compatible with python 3.11

```conda create -n geoCV python=3.9 -y```
```conda activate geoCV```

Install:
ultralytics
timm
opencv-python
neo4j
scikit-learn
numpy
```pip install ultralytics timm opencv-python neo4j scikit-learn numpy```
```pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126```

can also install: ```pip3 install torch torchvision```
for mac/no NVIDIA card.
This works best with cuda enabled gpu.


### Verifying PyTorch
To verify Pytorch works correctly:
```
python -c "import torch; x = torch.rand(5, 3); print(x); print(torch.cuda.is_available())"
```
You should see an array printed.  

If you have an NVIDIA card and installed the CUDA version of PyTorch, you should also see the word ```True``` (otherwise, ```False``` is expected).

##### Windows (CUDA 12.6)

```
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
```

##### Linux (CUDA 12.6)

```
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
```

##### CPU/Mac PyTorch
Default installation:

```
pip3 install torch torchvision
```
--------------------------------------------------------------------------------
## Running this thing:

running only object detection:
``` python train_yolo.py```

---------------------------------------------------------------------------------
### File Structure:
```
├───dataset
│   ├───classification
│   │   ├───images
│   │   │   ├───train
│   │   │   └───val
│   │   └───labels
│   │       ├───train
│   │       └───val
│   └───detection
│       ├───images
│       │   ├───train
│       │   └───val
│       └───labels
│           ├───train
│           └───val
├───processing_data
│   ├───annotations
│   ├───processed_images
│   └───raw_images
├───runs
│   └───detect
│       └───runs
│           └───detect
│               ├───bollard_detect
│               │   └───weights
│               ├───bollard_detect2
│               │   └───weights
│               ├───bollard_detect3
│               │   └───weights
│               ├───bollard_detect4
│               │   └───weights
│               └───bollard_detect5
│                   └───weights
├───scripts // utility scripts for normalizing data prior to labeling
│   └─── resize_images
│   └─── title_images
├─── data.yaml // yaml file for training YOLOv8
└─── train_yolo.py // script for training YOLOv8 on the dataset
```
---------------------------------------------------------------------------------
## Data Summary:
### Bollards:
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

### Post Boxes:
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

Data for this project is independently collected.


### Additional references:




