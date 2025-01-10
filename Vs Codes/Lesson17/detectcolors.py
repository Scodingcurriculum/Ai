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

# Step 1: Upload an image
print("Welcome to the AI Color Detective Game!")
print("Upload a colorful image and guess how many colors were used to paint it.")
image_path = input("Enter the file path of the image: ")
image = Image.open(image_path)
image = image.resize((100, 100))  # Resize for faster processing
plt.imshow(image)
plt.axis("off")
plt.title("Original Image")
plt.show()

# Step 2: Guess the number of colors
print("How many colors do you think are in the image?")
guess = int(input("Your guess: "))

# Step 3: Prepare the data
image_data = np.array(image)
pixels = image_data.reshape(-1, 3)  # Flatten the image into (pixels x RGB)

# Step 4: Determine the actual number of distinct colors
unique_colors = np.unique(pixels, axis=0)
num_colors = len(unique_colors)
print(f"\nAI detected {num_colors} distinct colors in the image!")

# Step 5: Show how close the guess was
if abs(num_colors - guess) <= 3:
    print("🎉 Great job! Your guess was very close!")
elif abs(num_colors - guess) <= 10:
    print("😊 Nice try! Your guess was close, but you can do better!")
else:
    print("😅 Keep practicing! You'll get better at guessing colors!")

# Step 6: Apply K-Means to reduce colors (just for fun visualization)
k = min(10, num_colors)  # Limit to a maximum of 10 clusters for simplicity
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(pixels)

cluster_centers = np.uint8(kmeans.cluster_centers_)
labels = kmeans.labels_
segmented_image = cluster_centers[labels]
segmented_image = segmented_image.reshape(image_data.shape)

# Step 7: Show the clustered image
plt.imshow(segmented_image)
plt.axis("off")
plt.title(f"Image with {k} Reduced Colors")
plt.show()


#ADDITIONAL ACTIVITY 1

# Step 8: Display the clustered colors and their names
print("\nAI-Generated Color Palette:")
color_names = []

palette_image = np.zeros((50, len(cluster_centers) * 50, 3), dtype=np.uint8)
for i, color in enumerate(cluster_centers):
    name = get_color_name(tuple(color))
    color_names.append(name)
    print(f"Color {i + 1}: RGB = {color}, Name = {name}")
    palette_image[:, i * 50:(i + 1) * 50] = color

# Step 9: Show the color palette
plt.imshow(palette_image)
plt.axis("off")
plt.title("Color Palette")
plt.show()

# Step 10: Save results
segmented_path = "clustered_image.png"
palette_path = "color_palette.png"
Image.fromarray(segmented_image).save(segmented_path)
Image.fromarray(palette_image).save(palette_path)

print(f"Clustered image saved as {segmented_path}")
print(f"Color palette saved as {palette_path}")


#ADDITIONAL ACTIVITY 2
# Display all images together
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Original Image
axes[0].imshow(image)
axes[0].axis("off")
axes[0].set_title("Original Image")

# Clustered Image
axes[1].imshow(segmented_image)
axes[1].axis("off")
axes[1].set_title(f"Clustered Image\n({k} Colors)")

# Color Palette
axes[2].imshow(palette_image)
axes[2].axis("off")
axes[2].set_title("AI-Generated Palette")

plt.tight_layout()
plt.show()
