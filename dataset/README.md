# 📂 RoboSort Pro Dataset

## Overview

This dataset was created for **RoboSort Pro – AI-Powered Multi-Parameter Robotic Object Sorting System**, an intelligent automation project that combines **Computer Vision, Machine Learning, Robotics, Embedded Systems, and IoT**.

The dataset is used to train the machine learning model responsible for identifying objects based on their visual characteristics before the robotic arm performs automated sorting.

The visual classification output is later combined with weight measurements from a Load Cell + HX711 module to generate the final sorting category.

---

# 🎯 Project Objective

The goal of the dataset is to enable the system to identify objects based on:

- Shape
- Color
- Size

and classify them into predefined object categories.

The prediction is then combined with weight information to create a complete multi-parameter classification system.

---

# 📁 Dataset Structure

```text
dataset/
│
├── black_small_circle/
├── black_big_circle/
├── white_small_circle/
├── white_big_circle/
├── black_small_rectangle/
├── black_big_rectangle/
├── white_small_rectangle/
└── white_big_rectangle/
```

Each folder contains images belonging to a single object category.

---

# 🏷️ Dataset Classes

| Class ID | Category |
|-----------|-----------|
| 0 | Black Small Circle |
| 1 | Black Big Circle |
| 2 | White Small Circle |
| 3 | White Big Circle |
| 4 | Black Small Rectangle |
| 5 | Black Big Rectangle |
| 6 | White Small Rectangle |
| 7 | White Big Rectangle |

---

# 📸 Dataset Collection Methodology

The dataset was manually created using a Raspberry Pi Camera Module.

### Image Collection Process

1. Objects were placed inside a fixed camera region.
2. Multiple images were captured for every category.
3. Images were collected under controlled lighting conditions.
4. Slight variations in object position and orientation were introduced.
5. Images were grouped according to their visual class.

The goal was to provide sufficient variation while maintaining consistent object visibility for reliable machine learning training.

---

# 🤖 Machine Learning Model Training

The machine learning model was trained using **Google Teachable Machine**.

Google Teachable Machine was selected because it provides an efficient platform for creating image classification models without requiring complex neural network implementation.

---

## Training Workflow

### Step 1 – Dataset Preparation

Images were collected and organized into class-specific folders.

Example:

```text
black_small_circle/
├── image_0.jpg
├── image_1.jpg
├── image_2.jpg
└── ...
```

Each folder represented a unique visual object class.

---

### Step 2 – Model Training

The images were uploaded to Google Teachable Machine.

The platform automatically:

- Extracted image features
- Trained a Convolutional Neural Network (CNN)
- Generated a classification model
- Evaluated model performance

The model learned to distinguish between:

- Circle vs Rectangle
- Black vs White
- Small vs Large

without manually defining classification rules.

---

### Step 3 – Model Export

After successful training, the model was exported as:

```text
model_unquant.tflite
```

along with:

```text
labels.txt
```

The TensorFlow Lite format was chosen because it is optimized for embedded devices such as Raspberry Pi.

---

### Step 4 – Raspberry Pi Deployment

The TensorFlow Lite model was integrated into the RoboSort Pro software stack.

Inference Process:

1. Capture image using Raspberry Pi Camera.
2. Resize image to model input dimensions.
3. Feed image to TensorFlow Lite Interpreter.
4. Obtain prediction probabilities.
5. Select highest-confidence class.
6. Return predicted object category.

---

# 🔄 Classification Pipeline

```text
Object Placement
        │
        ▼
Camera Capture
        │
        ▼
Image Preprocessing
        │
        ▼
TensorFlow Lite Model
        │
        ▼
Visual Classification
        │
        ▼
Weight Measurement
(HX711 + Load Cell)
        │
        ▼
Multi-Parameter Decision Engine
        │
        ▼
Final Category Generation
        │
        ▼
Robotic Arm Sorting
```

---

# 🎯 Visual Categories

The machine learning model predicts one of the following 8 visual categories:

- Black Small Circle
- Black Big Circle
- White Small Circle
- White Big Circle
- Black Small Rectangle
- Black Big Rectangle
- White Small Rectangle
- White Big Rectangle

---

# ⚖️ Final Multi-Parameter Categories

After weight classification, the system generates 16 final categories:

### Circle Categories

- Black Small Circle Light
- Black Small Circle Heavy
- Black Big Circle Light
- Black Big Circle Heavy

- White Small Circle Light
- White Small Circle Heavy
- White Big Circle Light
- White Big Circle Heavy

### Rectangle Categories

- Black Small Rectangle Light
- Black Small Rectangle Heavy
- Black Big Rectangle Light
- Black Big Rectangle Heavy

- White Small Rectangle Light
- White Small Rectangle Heavy
- White Big Rectangle Light
- White Big Rectangle Heavy

---

# 🚀 Dataset Applications

This dataset is used for:

- Machine Learning Training
- TensorFlow Lite Model Generation
- Object Classification
- Robotic Sorting Automation
- Embedded AI Deployment
- Educational Research
- Industrial Automation Demonstrations

---

# 📊 Future Improvements

Potential improvements include:

- Increasing dataset size
- Collecting images under varying lighting conditions
- Adding additional object shapes
- Supporting more colors
- Implementing advanced deep learning architectures
- Improving classification accuracy for industrial environments

---

# 🏆 RoboSort Pro

**RoboSort Pro** is an AI-powered object sorting system capable of classifying and sorting objects using:

✅ Machine Learning  
✅ Computer Vision  
✅ TensorFlow Lite  
✅ Raspberry Pi  
✅ Load Cell Weight Measurement  
✅ Robotic Arm Automation  
✅ TFT Display Monitoring  
✅ Flask Web Dashboard  

This dataset serves as the foundation of the visual intelligence used within the RoboSort Pro ecosystem.
