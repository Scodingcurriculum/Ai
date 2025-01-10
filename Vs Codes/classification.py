import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Step 1: Create a small labeled dataset of animals
data = {
    "Name": ["Lion", "Elephant", "Shark", "Eagle", "Frog"],
    "Habitat": ["Land", "Land", "Water", "Air", "Water"],
    "Diet": ["Carnivore", "Herbivore", "Carnivore", "Carnivore", "Insectivore"],
    "Size": ["Large", "Large", "Medium", "Medium", "Small"],
    "Classification": ["Mammal", "Mammal", "Fish", "Bird", "Amphibian"]
}

# Convert dataset to a DataFrame
df = pd.DataFrame(data)

# Map categorical features to numerical values
mappings = {
    "Habitat": {"Land": 0, "Water": 1, "Air": 2},
    "Diet": {"Carnivore": 0, "Herbivore": 1, "Insectivore": 2},
    "Size": {"Small": 0, "Medium": 1, "Large": 2},
    "Classification": {"Mammal": 0, "Fish": 1, "Bird": 2, "Amphibian": 3}
}

# Encode the dataset
encoded_df = df.replace(mappings)

# Step 2: Train the Decision Tree Classifier
X = encoded_df[["Habitat", "Diet", "Size"]]  # Features
y = encoded_df["Classification"]  # Labels
model = DecisionTreeClassifier()
model.fit(X, y)

# Reverse mappings for predictions
reverse_mappings = {v: k for k, v in mappings["Classification"].items()}

# Visualize the Decision Tree
def visualize_tree():
    plt.figure(figsize=(10, 6))
    tree.plot_tree(
        model,
        feature_names=["Habitat", "Diet", "Size"],
        class_names=list(reverse_mappings.values()),
        filled=True,
        rounded=True
    )
    plt.title("Decision Tree Visual - Supervised Learning")
    plt.show()

# Step 3: Create the forest-themed quiz using Tkinter
def predict_animal():
    try:
        # Get user inputs
        habitat = habitat_var.get()
        diet = diet_var.get()
        size = size_var.get()

        # Convert inputs to numerical values
        user_data = [[mappings["Habitat"][habitat], mappings["Diet"][diet], mappings["Size"][size]]]

        # Predict the animal's classification
        prediction = model.predict(user_data)[0]
        predicted_animal = reverse_mappings[prediction]

        # Display the result
        messagebox.showinfo(
            "🌲 Forest Quiz Result 🌲", 
            f"The animal is classified as: {predicted_animal} 🐾\n\n(Supervised learning powered by Decision Tree!)"
        )
    except Exception as e:
        messagebox.showerror("Error", "Please fill in all fields correctly.")

# Create the GUI
root = tk.Tk()
root.title("🌳 Forest Animal Classification Quiz 🌳")
root.geometry("600x600")
root.configure(bg="#a8df65")  # Forest green theme

# Title with forest emoji
title = tk.Label(
    root,
    text="🌲 Welcome to the Forest Animal Quiz 🌲",
    font=("Helvetica", 16, "bold"),
    bg="#228b22",  # Dark green
    fg="white",
)
title.pack(fill="x", pady=10)

# Visualize Tree Button
visualize_button = tk.Button(
    root,
    text="Visualize Decision Tree 🌳",
    command=visualize_tree,
    bg="#006400",  # Forest green
    fg="white",
    font=("Arial", 12, "bold"),
)
visualize_button.pack(pady=10)

# Add Habitat question
habitat_label = tk.Label(root, text="🌍 What is the habitat of the animal?", font=("Arial", 12), bg="#a8df65", fg="#2b2b2b")
habitat_label.pack(pady=5)
habitat_var = tk.StringVar(value="Land")
habitat_options = ["Land", "Water", "Air"]
for option in habitat_options:
    tk.Radiobutton(root, text=option, variable=habitat_var, value=option, font=("Arial", 10), bg="#a8df65", fg="#2b2b2b").pack(anchor="w")

# Add Diet question
diet_label = tk.Label(root, text="🍴 What does the animal eat?", font=("Arial", 12), bg="#a8df65", fg="#2b2b2b")
diet_label.pack(pady=5)
diet_var = tk.StringVar(value="Carnivore")
diet_options = ["Carnivore", "Herbivore", "Insectivore"]
for option in diet_options:
    tk.Radiobutton(root, text=option, variable=diet_var, value=option, font=("Arial", 10), bg="#a8df65", fg="#2b2b2b").pack(anchor="w")

# Add Size question
size_label = tk.Label(root, text="📏 What is the size of the animal?", font=("Arial", 12), bg="#a8df65", fg="#2b2b2b")
size_label.pack(pady=5)
size_var = tk.StringVar(value="Large")
size_options = ["Small", "Medium", "Large"]
for option in size_options:
    tk.Radiobutton(root, text=option, variable=size_var, value=option, font=("Arial", 10), bg="#a8df65", fg="#2b2b2b").pack(anchor="w")

# Predict button
predict_button = tk.Button(
    root,
    text="Classify Animal 🐾",
    command=predict_animal,
    bg="#006400",  # Forest green
    fg="white",
    font=("Arial", 14, "bold"),
)
predict_button.pack(pady=20)

# Run the application
root.mainloop()
