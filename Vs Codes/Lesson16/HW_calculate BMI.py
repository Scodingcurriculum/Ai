# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import tkinter as tk
from tkinter import messagebox, ttk

# Load the dataset
data = pd.read_csv('C:/Users/HP/Desktop/AIRevamp/Lesson16/heart.csv')

# Separate features (X) and target (y)
X = data.drop('target', axis=1)  # Features
y = data['target']               # Target (1 = Heart Attack, 0 = No Heart Attack)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Function to predict heart attack chances based on user input
def predict():
    try:
        # Get inputs from the form
        age = float(entry_age.get())
        sex = int(entry_sex.get())
        cp = int(entry_cp.get())
        trestbps = float(entry_trestbps.get())
        chol = float(entry_chol.get())
        fbs = int(entry_fbs.get())
        restecg = int(entry_restecg.get())
        thalach = float(entry_thalach.get())
        exang = int(entry_exang.get())
        oldpeak = float(entry_oldpeak.get())
        slope = int(entry_slope.get())
        ca = int(entry_ca.get())
        thal = int(entry_thal.get())

        # Prepare input data
        user_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
                                 columns=X.columns)

        # Predict the outcome
        prediction = model.predict(user_data)[0]
        probability = model.predict_proba(user_data)[0][1]

        # Create a styled result message
        if prediction == 1:
            result = f"🚨 High Risk of Heart Attack!\nProbability: {probability:.2f}"
            color = "red"
        else:
            result = f"✅ Low Risk of Heart Attack.\nProbability: {probability:.2f}"
            color = "green"

        # Show the result with color
        result_label.config(text=result, fg=color)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid inputs.")

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  # Convert height to meters
        bmi = weight / (height ** 2)
        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid weight and height.")

# Create the Tkinter GUI
root = tk.Tk()
root.title("Heart Attack Predictor")

# Styling the window
root.geometry("400x600")
root.configure(bg="#f5f5f5")

# Add a header with a medical theme
header = tk.Label(root, text="💓 Heart Attack Predictor", font=("Helvetica", 18, "bold"), bg="#0078D7", fg="white", pady=10)
header.pack(fill="x")

# Add a scrollable frame for the form
canvas = tk.Canvas(root, bg="#f5f5f5")
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#ffffff")
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Add form labels and entry fields
tk.Label(scrollable_frame, text="Enter Your Health Data", font=("Arial", 16, "bold"), bg="#ffffff", fg="#444").pack(pady=10)

labels = ["Age", "Sex (1=Male, 0=Female)", "Chest Pain Type (0-3)", "Resting Blood Pressure",
          "Cholesterol", "Fasting Blood Sugar (1=Yes, 0=No)", "Resting ECG (0-2)",
          "Max Heart Rate Achieved", "Exercise-Induced Angina (1=Yes, 0=No)",
          "ST Depression", "Slope of Peak ST (0-2)", "Major Vessels (0-3)", "Thalassemia (1-3)",
          "Weight (kg)", "Height (cm)"]

entries = []
for label_text in labels:
    frame = tk.Frame(scrollable_frame, bg="#ffffff")
    frame.pack(fill="x", pady=5)
    tk.Label(frame, text=label_text, font=("Arial", 12), bg="#ffffff", fg="#333").pack(side="left", padx=10)
    entry = tk.Entry(frame, font=("Arial", 12), bg="#f0f0f0", relief="groove")
    entry.pack(side="right", padx=10, ipadx=5, ipady=3)
    entries.append(entry)

# Unpack entries for easy access
(entry_age, entry_sex, entry_cp, entry_trestbps, entry_chol, entry_fbs, entry_restecg,
 entry_thalach, entry_exang, entry_oldpeak, entry_slope, entry_ca, entry_thal,
 entry_weight, entry_height) = entries

# Add Predict button
tk.Button(scrollable_frame, text="Predict", command=predict, bg="#0078D7", fg="white", 
          font=("Arial", 12, "bold"), relief="flat", width=15, height=1).pack(pady=5)

# Add BMI Button
tk.Button(scrollable_frame, text="Calculate BMI", command=calculate_bmi, bg="#4CAF50", fg="white", 
          font=("Arial", 12, "bold"), relief="flat", width=15, height=1).pack(pady=5)

# Add a result label
result_label = tk.Label(scrollable_frame, text="", font=("Arial", 14, "bold"), bg="#f5f5f5")
result_label.pack(pady=20)

# Run the application
root.mainloop()
