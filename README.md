# Satellite Image Landscape Classifier

## Project Overview
This project is an image classification system designed to identify and label different landscapes in satellite images. Using a deep learning model based on VGG16, the classifier can recognize and annotate areas such as beaches, mountains, oceans, rivers, and more. The project also includes a desktop application built with Tkinter that allows users to upload images and view the classified landscape regions.

## Limitations
- *Limited Dataset:* The model was trained on a relatively small dataset, which may limit its ability to generalize to all possible landscape types and variations. While the model performs well on the training data, its accuracy on unseen data might be constrained.
- *Model Performance:* The model might not be perfect in classifying all regions accurately, especially in complex or unclear images. Additionally, due to the limited classes in the dataset, it might fail to recognize or confuse certain landscapes.

## What's Been Done
1. *Dataset Preparation:* 
   - The dataset was collected, preprocessed, and augmented to create a robust training set. The images were categorized into classes such as beach, mountain, ocean, river, mars, moon, and ice.
   
2. *Model Creation:* 
   - A deep learning model based on VGG16 was developed using transfer learning. The model was fine-tuned to classify the landscapes into the defined categories.
   
3. *Model Testing:*
   - The model was tested on multiple landscape images to ensure it can correctly identify and label various landscape types. The images were divided into patches, and each patch was classified to identify the landscape.

4. *Python Application:*
   - A Tkinter-based desktop application was developed. The app allows users to upload an image, which the model then processes and annotates with detected landscape types.

## How to Run the App
### Requirements
- Python 3.x
- TensorFlow
- OpenCV
- Tkinter
- Pillow

### Steps
1. *Clone the Repository:*
   sh
   git clone https://github.com/yourusername/satellite-image-landscape-classifier.git
   cd satellite-image-landscape-classifier
   

2. *Install Dependencies:*
   Install the necessary Python packages using pip:
   sh
   pip install tensorflow opencv-python pillow
   

3. *Run the Application:*
   You can run the application using the following command:
   sh
   python app.py
   

### Model Files
- *TensorFlow Lite Model:* The .tflite model file is uploaded to the repository for ease of use.
- *Keras Model:* The original .keras file is not included due to its size. If you wish to use the .keras model, you can run the training code provided in the repository to generate it, or you can use the pre-trained .tflite model directly.

## Conclusion
This project demonstrates a basic yet functional implementation of satellite image classification using deep learning. While the dataset and model may have their limitations, they provide a foundation for further improvements and applications in satellite imagery analysis.
