import cv2
import mediapipe as mp
import pyttsx3
import threading
import time

# Initialize Mediapipe Hand Solution
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Initialize Text-to-Speech engine
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)
tts_engine.setProperty('volume', 1)

# TTS Function in a Separate Thread
def speak_text(text):
    def tts_task():
        tts_engine.say(text)
        tts_engine.runAndWait()

    threading.Thread(target=tts_task).start()

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

#ADDITIONAL ACTIVITY TTS --step1
# Cooldown Mechanism for TTS
last_gesture = None
last_time_spoken = 0

#ADDITIONAL ACTIVITY TTS --step2
def should_speak(gesture):
    global last_gesture, last_time_spoken
    current_time = time.time()
    if gesture != last_gesture or (current_time - last_time_spoken > 2):
        last_gesture = gesture
        last_time_spoken = current_time
        return True
    return False

# Start Webcam
cap = cv2.VideoCapture(0)
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Reduce frame size and flip for real-time display
    frame = cv2.flip(cv2.resize(frame, (640, 480)), 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process every 3rd frame for faster execution
    frame_count += 1
    if frame_count % 3 != 0:
        continue

    # Process the frame to detect hands
    result = hands.process(rgb_frame)

    # Display recognized gestures
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract finger tip states
            finger_tips = [4, 8, 12, 16, 20]
            finger_states = []
            for tip_id in finger_tips:
                tip = hand_landmarks.landmark[tip_id]
                base = hand_landmarks.landmark[tip_id - 2]
                finger_states.append(tip.y < base.y)

            # Recognize gesture
            gesture = recognize_gesture(finger_states)
            cv2.putText(frame, f"Gesture: {gesture}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            #ADDITIONAL ACTIVITY TTS --step3
            # Speak the gesture if allowed
            if gesture != "Unknown Gesture" and should_speak(gesture):
                speak_text(gesture)

    # Display the video frame
    cv2.imshow("Sign Language Interpreter", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
