import cv2
import mediapipe as mp

# Initialize Mediapipe Hand Solution
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

#CHANGE  THE DICTIONARY---step 1
# Custom messages for finger counts
finger_messages = {
    0: "No fingers detected.",
    1: "You’re holding up 1 finger!",
    2: "You’re holding up 2 fingers!",
    3: "You’re holding up 3 fingers!",
    4: "You’re holding up 4 fingers!",
    5: "Wow! All fingers are up!"
}

# Start Webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Reduce frame size and flip for real-time display
    frame = cv2.flip(cv2.resize(frame, (640, 480)), 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    result = hands.process(rgb_frame)

    # Display detected hand landmarks and count fingers
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract finger tip states
            finger_tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
            finger_states = []
            for tip_id in finger_tips:
                tip = hand_landmarks.landmark[tip_id]
                base = hand_landmarks.landmark[tip_id - 2]
                finger_states.append(tip.y < base.y)  # True if finger is up

            #STEP--2
            # Count the number of fingers raised
            num_fingers = sum(finger_states)


            #STEP-3
            # Display the number of fingers and the corresponding message
            message = finger_messages.get(num_fingers, "Unknown Gesture")
            cv2.putText(frame, f"Fingers: {num_fingers}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, message, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the video frame
    cv2.imshow("Finger Counter", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
