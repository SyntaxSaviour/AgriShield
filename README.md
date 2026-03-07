# 🌾 AgriShield: AI-Powered Crop Disease Detection using Swin Transformers

AgriShield is an **AI-driven crop health monitoring system** designed to detect crop diseases at an early stage using **advanced computer vision and Transformer-based deep learning models**. The project leverages **Swin Transformer architecture** to analyze leaf images and accurately identify disease patterns, enabling faster and more reliable crop health assessment.

AgriShield aims to assist **farmers, agricultural researchers, and agri-tech stakeholders** by providing a scalable and intelligent solution for early disease detection and crop monitoring.


# 📌 Problem Statement

Crop diseases are one of the leading causes of reduced agricultural yield worldwide. Farmers often rely on manual inspection to identify plant diseases, which is:

- Time-consuming
- Dependent on expert knowledge
- Prone to human error
- Difficult to scale across large farms

In many regions, farmers lack access to agricultural specialists who can diagnose diseases early. Delayed detection leads to **rapid disease spread, crop loss, and economic damage**.

Therefore, an **automated AI-based crop disease detection system** that can analyze plant leaf images and provide early diagnosis is essential.


# 🎯 Objectives

- Detect and classify crop diseases from leaf images using AI
- Implement **Swin Transformer-based vision models** for improved feature extraction
- Provide **early disease detection** to prevent crop loss
- Build a **scalable system adaptable to multiple crops and diseases**
- Enable future integration with **mobile applications and precision agriculture systems**


# 🧠 Proposed Solution

AgriShield uses **Transformer-based deep learning models** to perform image-based disease classification. The system processes crop leaf images and learns complex spatial patterns associated with plant diseases.

Unlike traditional CNN-based approaches, AgriShield leverages the **Swin Transformer**, a hierarchical vision transformer that captures both **local and global image features efficiently**.


## 🔄 System Workflow

1️⃣ **Image Acquisition**

Leaf images are collected using:
- Smartphone cameras
- Agricultural datasets
- Drone or field monitoring systems

2️⃣ **Image Preprocessing**

- Image resizing
- Normalization
- Data augmentation (flip, rotation, brightness adjustments)

3️⃣ **Feature Extraction**

The **Swin Transformer** processes images by dividing them into patches and applying **shifted window self-attention**, enabling the model to learn complex disease patterns.

4️⃣ **Disease Classification**

The extracted features are passed to a classification head that predicts:

- Healthy leaf
- Disease class 1
- Disease class 2
- Additional disease categories

5️⃣ **Prediction Output**

The system returns:
- Predicted disease label
- Confidence score
- Optional visualization (future Grad-CAM integration)


# 🧪 Dataset

AgriShield uses publicly available crop disease image datasets such as:

- **PlantVillage Dataset**
- Additional agricultural image datasets for model generalization

Images are categorized by:

- Crop type
- Disease type
- Healthy leaves


## 📂 Dataset Structure

```bash
data/
├── train/
│   ├── healthy/
│   ├── disease_1/
│   └── disease_2/
├── validation/
└── test/
```

## ⚙️ Technologies Used

### Programming & Frameworks

- Python  
- TensorFlow / Keras  
- PyTorch (for Transformer models)  
- NumPy  
- Pandas  
- OpenCV  
- Matplotlib  

### Machine Learning & Deep Learning

- Vision Transformers  
- Swin Transformer Architecture  
- Image Preprocessing & Augmentation  
- Transfer Learning  
- Model Evaluation Metrics  


## 🏗️ Model Architecture

AgriShield uses a **Transformer-based vision model** rather than a traditional CNN pipeline.

### Core Architecture

**1. Input Layer**

- Leaf images converted into image tensors

**2. Patch Partitioning**

- Images split into fixed-size patches

**3. Swin Transformer Blocks**

- Window-based self-attention  
- Shifted window mechanism  
- Hierarchical feature representation  

**4. Feature Aggregation**

**5. Classification Head**

- Fully connected layer  
- Softmax output  


## 🔄 Model Pipeline

```text
Leaf Image
   ↓
Image Preprocessing
   ↓
Patch Partitioning
   ↓
Swin Transformer Backbone
   ↓
Feature Representation
   ↓
Classification Head
   ↓
Disease Prediction
```

## 📊 Evaluation Metrics

To evaluate model performance, the following metrics are used:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

These metrics ensure the model performs well on unseen validation and test datasets.


## 🚀 Installation & Setup

### Prerequisites

- Python 3.8+
- pip or conda
- GPU recommended for training


### Clone the Repository

```bash
git clone https://github.com/your-username/AgriShield.git
cd AgriShield
```


### Install Dependencies

```bash
pip install -r requirements.txt
```


## ▶️ Run the Project

### Train the Model

```bash
python train.py
```

### Evaluate the Model

```bash
python evaluate.py
```

### Run Inference on a New Image

```bash
python predict.py --image path/to/image.jpg
```


## 📁 Project Structure

```bash
AgriShield/
├── data/
├── models/
├── notebooks/
├── src/
│   ├── preprocessing.py
│   ├── swin_model.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔍 Results

- Achieved high classification accuracy on validation and test datasets
- Demonstrated strong capability in identifying subtle disease patterns
- Transformer-based architecture improved feature learning compared to standard CNNs
- Model shows good generalization across disease classes


## 🌱 Future Enhancements

AgriShield can be extended into a full precision agriculture platform:

- Support for more crop types and diseases
- Mobile app for farmers
- Real-time detection using smartphone camera
- Integration with UAV / drone imagery
- Explainable AI using Grad-CAM
- Integration with weather and soil sensor data
- Farmer advisory system with treatment suggestions


## 🤝 Contributions

Contributions are welcome.

If you'd like to improve AgriShield:

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Submit a pull request


## 📜 License

This project is licensed under the MIT License.
