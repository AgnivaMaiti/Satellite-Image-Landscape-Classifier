import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from PIL import Image, ImageTk

class ImageClassifierApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Image Classifier")
        self.model = load_model('your_model.keras')
        self.class_labels = ['beach', 'ice', 'mars', 'moon', 'mountain', 'ocean', 'river']
        
        self.label = tk.Label(root, text="Select an image:")
        self.label.pack()

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()

    def preprocess_image(self, img):
        img = cv2.resize(img, (150, 150))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        return img

    def predict_image(self, img):
        processed_img = self.preprocess_image(img)
        predictions = self.model.predict(processed_img)
        class_idx = np.argmax(predictions[0])
        return self.class_labels[class_idx]

    def annotate_image(self, img, predictions, box_size=150):
        for (x, y, label) in predictions:
            if label not in ['mars', 'moon', 'ice']:
                cv2.rectangle(img, (x, y), (x + box_size, y + box_size), (0, 255, 0), 2)
                cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        return img

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            img = cv2.imread(file_path)
            height, width, _ = img.shape
            patch_size = 150
            stride = 150

            predictions = []

            for y in range(0, height - patch_size + 1, stride):
                for x in range(0, width - patch_size + 1, stride):
                    patch = img[y:y + patch_size, x:x + patch_size]
                    class_label = self.predict_image(patch)
                    if class_label not in ['mars', 'moon', 'ice']:
                        predictions.append((x, y, class_label))

            annotated_img = self.annotate_image(img, predictions)
            result_img = Image.fromarray(cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB))
            result_img.thumbnail((600, 400))
            self.display_image(result_img)

    def display_image(self, img):
        self.canvas.delete("all")
        self.tk_img = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_img)

if _name_ == "_main_":
    root = tk.Tk()
    app = ImageClassifierApp(root)
    root.mainloop()