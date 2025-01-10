# Import libraries
from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import webcolors  # To name the colors!

# Function to get color name from RGB
def get_color_name(rgb):
    try:
        return webcolors.rgb_to_name(rgb)
    except ValueError:
        return "Unknown Color"

# Function to calculate guess accuracy
def calculate_accuracy(actual, guess):
    return abs(actual - guess)

# Step 1: Upload an image
print("Welcome to the AI Color Detective Game - 2-Team Edition!")
print("Upload a colorful image and guess how many colors were used to paint it.")
image_path = input("Enter the file path of the image: ")
image = Image.open(image_path)
image = image.resize((100, 100))  # Resize for faster processing
plt.imshow(image)
plt.axis("off")
plt.title("Original Image")
plt.show()

# Step 2: Prepare the data for analysis
image_data = np.array(image)
pixels = image_data.reshape(-1, 3)  # Flatten the image into (pixels x RGB)

# Step 3: Determine the actual number of distinct colors
unique_colors = np.unique(pixels, axis=0)
num_colors = len(unique_colors)
print(f"\nAI detected {num_colors} distinct colors in the image!")

# Step 4: Start the Game
print("\nIt's time for the game! Each team will take turns guessing the number of colors.")
team_1_score = 0  # Initialize Team 1 score
team_2_score = 0  # Initialize Team 2 score

# Number of turns per team
turns = 3  # You can change this based on the class size

# Game Loop for Team 1 and Team 2
for turn in range(1, turns + 1):  # Loop for each turn
    print(f"\nTurn {turn}!")
    
    # Team 1's guess
    print("Team 1, it's your turn to guess!")  # Prompt for Team 1
    guess_1 = int(input("How many colors do you think are in the image? "))
    accuracy_1 = calculate_accuracy(num_colors, guess_1)
    print(f"Team 1's guess: {guess_1} -> Accuracy: {accuracy_1}")
    if accuracy_1 <= 3:  # If the guess is within 3 colors
        team_1_score += 1  # Award a point to Team 1
        print("🎉 Team 1 gets 1 point!")
    
    # Team 2's guess
    print("\nTeam 2, it's your turn to guess!")  # Prompt for Team 2
    guess_2 = int(input("How many colors do you think are in the image? "))
    accuracy_2 = calculate_accuracy(num_colors, guess_2)
    print(f"Team 2's guess: {guess_2} -> Accuracy: {accuracy_2}")
    if accuracy_2 <= 3:  # If the guess is within 3 colors
        team_2_score += 1  # Award a point to Team 2
        print("🎉 Team 2 gets 1 point!")

# Step 5: Announce the winner
print("\nGame Over!")  # End of the game
print(f"Team 1's score: {team_1_score}")  # Display Team 1 score
print(f"Team 2's score: {team_2_score}")  # Display Team 2 score

if team_1_score > team_2_score:  # Check if Team 1 wins
    print("🎉 Team 1 wins!")
elif team_1_score < team_2_score:  # Check if Team 2 wins
    print("🎉 Team 2 wins!")
else:  # If there's a tie
    print("It's a tie! 😄")

# Step 6: Show the clustered image with reduced colors for fun
k = min(10, num_colors)  # Limit to a maximum of 10 clusters for simplicity
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(pixels)

cluster_centers = np.uint8(kmeans.cluster_centers_)
labels = kmeans.labels_
segmented_image = cluster_centers[labels]
segmented_image = segmented_image.reshape(image_data.shape)

# Show the clustered image
plt.imshow(segmented_image)
plt.axis("off")
plt.title(f"Image with {k} Reduced Colors")
plt.show()

# Step 7: Display the clustered colors and their names
print("\nAI-Generated Color Palette:")
color_names = []

palette_image = np.zeros((50, len(cluster_centers) * 50, 3), dtype=np.uint8)
for i, color in enumerate(cluster_centers):
    name = get_color_name(tuple(color))
    color_names.append(name)
    print(f"Color {i + 1}: RGB = {color}, Name = {name}")
    palette_image[:, i * 50:(i + 1) * 50] = color

# Show the color palette
plt.imshow(palette_image)
plt.axis("off")
plt.title("Color Palette")
plt.show()

# Step 8: Save results
segmented_path = "clustered_image.png"
palette_path = "color_palette.png"
Image.fromarray(segmented_image).save(segmented_path)
Image.fromarray(palette_image).save(palette_path)

print(f"Clustered image saved as {segmented_path}")
print(f"Color palette saved as {palette_path}")
