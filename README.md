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
## Data Summary:
### Bollards:
| Country     | Variants | Images per Variant | Total Images |
|-------------|----------|--------------------|--------------|
| Monaco      | 2        |                    |              |
| Vietnam     | 2        |                    |              |
| Singapore   | 3        |                    |              |
| Serbia      | 3        |                    |              |
| Thailand    | 6        |                    |              |
| India       | 7        |                    |              |
| Laos        | 4        |                    |              |
| Philippines | 2        |                    |              |

---------------------------------------------------------------------------------
Distinct Object classifications are validated against:
https://geohints.com/, https://geohints.com/meta/bollards,
which is a community database for GeoGuessr "meta" or country-specific identifying information. 

Data for this project is independently collected.


References: 




