import zipfile
import os
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

# Set the path to your ZIP file
zip_file_path = "C:/Users/HP/Desktop/AIRevamp/Lesson14-15/converted_keras (1).zip"
model_dir = "model"

# Extract the ZIP file
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(model_dir)

print("Model extracted successfully.")

# Load the model
model_path = os.path.join(model_dir, "keras_model.h5")
model = load_model(model_path, compile=False)

# Load the labels and clean up the label names
labels_path = os.path.join(model_dir, "labels.txt")
class_names = [line.strip() for line in open(labels_path, "r").readlines()]

# Create the array of the right shape to feed into the Keras model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image_path = "C:/Users/HP/Desktop/AIRevamp/Lesson14-15/WIN_20241004_02_26_07_Pro.jpg"
image = Image.open(image_path).convert("RGB")

# Resize the image to 224x224 using ImageOps to fit the model's input size
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# Turn the image into a numpy array
image_array = np.asarray(image)

# Normalize the image to the range [0, 1]
normalized_image_array = image_array.astype(np.float32) / 255.0

# Load the image into the array
data[0] = normalized_image_array

# Predict using the model
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

# Print prediction and confidence score
print("Class:", class_name)
print("Confidence Score:", confidence_score)
