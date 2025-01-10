import cv2
import mediapipe as mp
import pyttsx3
import threading
import time

# Gesture Recognition Function
def recognize_gesture(finger_states):
    gesture_dict = {
        (True, False, False, False, False): "Thumbs Up",
        (False, True, False, False, False): "Pointing",
        (True, True, False, False, False): "Hello",
        (False, True, True, False, False): "Help",
        (True, True, True, True, True): "Hi Five",
    }
    return gesture_dict.get(tuple(finger_states), "Unknown Gesture")

