**Pothole Detection**
==========================

**Overview**
------------

This project aims to develop a pothole detection system using deep learning techniques. The system classifies potholes into three classes: safe, medium, and risk-pothole, based on their severity. The models used include the YOLOv8-seg series (small, large, and x-large) for object detection and segmentation, as well as the MiDaS model for depth estimation.

**System Architecture**
---------------------

The system architecture is as follows:

* User uploads an image or video file to the Gradio app
* The app processes the input using the YOLOv8-seg model for object detection and segmentation
* The MiDaS model estimates the depth of the detected potholes
* The system classifies the potholes based on their size and depth
* The annotated output is generated and displayed to the user

**Model Development**
--------------------

The models used in this project are:

* YOLOv8-seg x-large for object detection and segmentation
* MiDaS model for depth estimation

The models were trained on a dataset of 1566 images, which was augmented to 3762 images. The dataset includes images of roads in various conditions, including summer, winter, and daytime.

**Data Sources**
----------------

The dataset used in this project was collected from various sources, including:

* Google search
* Ninja dataset
* Photos of roads taken by the author
* GitHub

**User Instructions**
--------------------

To use the Gradio app, follow these steps:

1. Upload an image or video file to the app
2. Wait for the app to process the input and generate output
3. View the annotated output with detected potholes

**Requirements**
---------------

To run this project, you need to install the following packages:

* ultralytics
* torch
* roboflow
* opencv-python
* timm
* gradio

You can install these packages using pip:
`!pip install -r requirements.txt`


Verify

Open In Editor
Edit
Copy code
**Installation**
---------------

To install the required packages, run the following command:
pip install -r requirements.txt


License
This project is licensed under the MIT License.

Acknowledgments
This project was developed using the following resources:

YOLOv8-seg model: https://github.com/ultralytics/yolov8
MiDaS model: https://github.com/isl-org/MiDas
Gradio: https://gradio.app/
