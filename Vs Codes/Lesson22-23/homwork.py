import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import cv2
import numpy as np
from PIL import Image, ImageTk
import os

# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# This will hold the path for saved face data
face_data = 'owner_face_data.yml'

# Create the main window
window = tk.Tk()
window.title("Face Recognition System")

# Set window size
window.geometry("400x350")
window.config(bg="#f0f0f0")

# Title Label
label_title = tk.Label(window, text="Face Recognition System", font=("Arial", 20, "bold"), bg="#f0f0f0")
label_title.pack(pady=20)

# Frame for interactive content
frame = tk.Frame(window, bg="#f0f0f0")
frame.pack(pady=10)

# Create label and entry for owner name
label_name = tk.Label(frame, text="Enter Owner Name:", font=("Arial", 12), bg="#f0f0f0")
label_name.grid(row=0, column=0, padx=10, pady=5)

entry_name = tk.Entry(frame, font=("Arial", 12), width=20)
entry_name.grid(row=0, column=1, padx=10, pady=5)

# Status label to show real-time feedback
status_label = tk.Label(window, text="Please click 'Save Face' to start", font=("Arial", 12), bg="#f0f0f0")
status_label.pack(pady=10)

# Create a progress bar for face capturing
progress_bar = ttk.Progressbar(window, length=300, mode='indeterminate')
progress_bar.pack(pady=10)

# Function to capture the owner's face and save it
def save_owner_face():
    owner_name = entry_name.get()
    if not owner_name:
        messagebox.showwarning("Input Error", "Please enter the owner's name!")
        return

    # Open the webcam
    cap = cv2.VideoCapture(0)
    
    face_id = 1  # ID for the owner's face
    count = 0
    faces = []
    labels = []
    
    # Hide the progress bar and change the status label
    progress_bar.start()
    status_label.config(text="Capturing face... Please look at the camera.")
    
    while count < 30:  # Capture 30 images of the face
        ret, frame = cap.read()
        
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        detected_faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # If faces are detected, capture them
        for (x, y, w, h) in detected_faces:
            count += 1
            faces.append(gray[y:y+h, x:x+w])
            labels.append(face_id)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Show the frame with the rectangle around the face
        cv2.imshow("Capture Face", frame)
        
        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Save the captured faces and labels
    recognizer.train(faces, np.array(labels))
    recognizer.save(face_data)  # Save the trained face data
    
    cap.release()
    cv2.destroyAllWindows()
    
    # Stop the progress bar and update the status
    progress_bar.stop()
    status_label.config(text="Face saved successfully! You can now log in.")
    
    save_button.config(state=tk.DISABLED)  # Disable save button after saving face
    login_button.config(state=tk.NORMAL)  # Enable login button

# Function to login by detecting and recognizing the face
def login_face():
    cap = cv2.VideoCapture(0)
    
    # Load the saved face data
    recognizer.read(face_data)
    
    # Hide the progress bar and change the status label
    progress_bar.start()
    status_label.config(text="Logging in... Please look at the camera.")
    
    while True:
        ret, frame = cap.read()
        
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        detected_faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in detected_faces:
            face = gray[y:y+h, x:x+w]
            label, confidence = recognizer.predict(face)  # Predict the face
            
            # If the face matches the saved face
            if label == 1 and confidence < 100:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, "Login Successful!", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                
                # Stop the progress bar and show the success message
                progress_bar.stop()
                status_label.config(text="System Unlocked! Welcome!")
                messagebox.showinfo("System Unlocked", "Face Detected: System Unlocked!")
                break  # Exit if login is successful
            
        # Display the frame with the detected face
        cv2.imshow("Face Login", frame)
        
        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Function to delete the owner's face data
def delete_owner_face():
    owner_name = simpledialog.askstring("Delete Owner Face", "Enter the owner's name or ID to delete:")
    
    if owner_name:
        if os.path.exists(face_data):
            os.remove(face_data)  # Delete the saved face data file
            messagebox.showinfo("Success", "Owner face deleted successfully!")
            status_label.config(text="Please click 'Save Face' to start")
            save_button.config(state=tk.NORMAL)  # Re-enable save button
            login_button.config(state=tk.DISABLED)  # Disable login button
        else:
            messagebox.showwarning("Error", "No face data found for the given owner!")
    else:
        messagebox.showwarning("Input Error", "Please enter a valid name or ID!")

# Add the 'Delete Owner Face' button
delete_button = tk.Button(window, text="Delete Owner Face", font=("Arial", 12), command=delete_owner_face, bg="#F44336", fg="white", relief="raised")
delete_button.pack(pady=10)

# Create a button to save the owner's face
save_button = tk.Button(window, text="Save Owner Face", font=("Arial", 12), command=save_owner_face, bg="#4CAF50", fg="white", relief="raised")
save_button.pack(pady=10)

# Create a button to login with the saved face (initially disabled)
login_button = tk.Button(window, text="Login with Face", font=("Arial", 12), command=login_face, state=tk.DISABLED, bg="#2196F3", fg="white", relief="raised")
login_button.pack(pady=10)

# Run the main window loop
window.mainloop()
