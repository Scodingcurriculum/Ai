# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import tkinter as tk
from tkinter import messagebox

# Load the dataset


# Separate features (X) and target (y)


# Split the data into training and testing sets


# Initialize and train the Logistic Regression model


# Function to predict heart attack chances based on user input


# Create the Tkinter GUI
root = tk.Tk()
root.title("Heart Attack Predictor")

# Styling the window
root.geometry("500x700")
root.configure(bg="#f5f5f5")

# Add a header with a medical theme
header = tk.Label(root, text="💓 Heart Attack Predictor", font=("Helvetica", 20, "bold"), bg="#0078D7", fg="white", pady=10)
header.pack(fill="x")

# Create a frame for the form
form_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="ridge")
form_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Add form labels and entry fields
tk.Label(form_frame, text="Enter Your Health Data", font=("Arial", 16, "bold"), bg="#ffffff", fg="#444").pack(pady=10)

labels = ["Age", "Sex (1=Male, 0=Female)", "Chest Pain Type (0-3)", "Resting Blood Pressure",
          "Cholesterol", "Fasting Blood Sugar (1=Yes, 0=No)", "Resting ECG (0-2)",
          "Max Heart Rate Achieved", "Exercise-Induced Angina (1=Yes, 0=No)",
          "ST Depression", "Slope of Peak ST (0-2)", "Major Vessels (0-3)", "Thalassemia (1-3)"]

entries = []
for label_text in labels:
    frame = tk.Frame(form_frame, bg="#ffffff")
    frame.pack(fill="x", pady=5)
    tk.Label(frame, text=label_text, font=("Arial", 12), bg="#ffffff", fg="#333").pack(side="left", padx=10)
    entry = tk.Entry(frame, font=("Arial", 12), bg="#f0f0f0", relief="groove")
    entry.pack(side="right", padx=10, ipadx=5, ipady=3)
    entries.append(entry)

# Unpack entries for easy access
(entry_age, entry_sex, entry_cp, entry_trestbps, entry_chol, entry_fbs, entry_restecg,
 entry_thalach, entry_exang, entry_oldpeak, entry_slope, entry_ca, entry_thal) = entries

# Add Predict button
tk.Button(root, text="Predict", bg="#0078D7", fg="white", font=("Arial", 14, "bold"), relief="flat").pack(pady=10)

# Add a result label
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#f5f5f5")
result_label.pack(pady=20)

# Run the application
root.mainloop()
