import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from PIL import Image as PILImage
from kivy.graphics.texture import Texture
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment with new categories
def analyze_emotion(entry):
    sentiment = analyzer.polarity_scores(entry)  # Get polarity scores
    compound_score = sentiment['compound']  # Compound score (overall sentiment)

    # Check for the new sentiment levels
    if compound_score > 0.7:
        return "😄 Very Positive", "Awesome! You're having a fantastic day!", "very_happy.jpeg"
    elif compound_score >= 0.3:
        return "😊 Positive", "Great to hear you had a good day! Keep spreading positivity!", "happy.jpeg"
    elif compound_score <= -0.3:
        return "😔 Negative", "It seems like today was tough. Take a break, talk to a loved one, or try relaxing activities.", "sad.jpeg"
    elif compound_score > 0.1:
        return "😲 Surprised", "Wow, it looks like you had a surprising day! Keep it up!", "surprised.jpeg"
    else:
        return "😐 Neutral", "It seems like your day was average. Try doing something fun or relaxing tomorrow!", "neutral.jpeg"

# Function to analyze and update the feedback
def analyze(entry):
    emotion, suggestion, image_path = analyze_emotion(entry)

    # Update feedback label
    feedback_label.text = f"Emotion: {emotion}\nFeedback: {suggestion}"

    # Update image based on sentiment
    img = PILImage.open(image_path)
    img = img.resize((100, 100))  # Resize image to fit the label
    img = img.rotate(180)  # Rotate image by 180 degrees
    texture = Texture.create(size=(img.width, img.height), colorfmt='rgb')
    texture.blit_buffer(img.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
    image_feedback.texture = texture

    # Rotate image in the widget itself (optional)
    image_feedback.angle = 180

# ADDED: Function to save the diary entry to a file
def save(entry):
    if entry:
        # Save the entry to a file (Optional)
        with open("diary_entries.txt", "a", encoding="utf-8") as file:
            file.write(f"Entry: {entry}\n{'-' * 40}\n")
    else:
        # Show popup if the entry is empty
        popup = Popup(title="Input Error",
                      content=Label(text="Please write something in your diary."),
                      size_hint=(0.6, 0.2))
        popup.open()

# Function to handle save and analyze action
def save_and_analyze(instance):
    entry = diary_entry_input.text.strip()
    save(entry)  # Save entry
    analyze(entry)  # Analyze sentiment

    # Clear the input field
    diary_entry_input.text = ""

# Main Kivy App
def build_app():
    root = BoxLayout(orientation='vertical', padding=20, spacing=10)

    # Label for diary prompt
    title_label = Label(text="How was your day? Write about it below:", size_hint_y=None, height=40, font_size=20)
    root.add_widget(title_label)

    # Scrollable text input for diary entry
    global diary_entry_input
    diary_entry_input = TextInput(hint_text="Write your day here...", font_size=18, size_hint=(1, 0.4), multiline=True)
    root.add_widget(diary_entry_input)

    # Save and Analyze Button
    save_button = Button(text="Save & Analyze", size_hint_y=None, height=50, background_color=(0.2, 0.6, 0.2, 1))
    save_button.bind(on_press=save_and_analyze)
    root.add_widget(save_button)

    # Feedback label
    global feedback_label
    feedback_label = Label(text="Feedback will appear here.", font_size=16, size_hint_y=None, height=50)
    root.add_widget(feedback_label)

    # BoxLayout to place the image horizontally
    image_layout = BoxLayout(size_hint_y=None, height=100, orientation='horizontal')
    
    global image_feedback
    image_feedback = Image(size_hint=(None, None), size=(100, 100))
    image_layout.add_widget(image_feedback)

    root.add_widget(image_layout)

    return root

# Run the Kivy App
class DiaryApp(App):
    def build(self):
        return build_app()

if __name__ == "__main__":
    DiaryApp().run()
