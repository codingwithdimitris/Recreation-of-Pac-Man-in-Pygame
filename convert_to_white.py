import pygame
import os

# Set dummy video driver for headless operation (no window)
os.environ["SDL_VIDEODRIVER"] = "dummy"

# Initialize Pygame
pygame.init()
pygame.display.set_mode((1, 1))  # Minimal display to allow surface operations

# Input and output folders
input_folder = "images/maze"    # <-- Change this to your folder
output_folder = "images/maze"
os.makedirs(output_folder, exist_ok=True)

# Get all PNG files in folder
png_files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith('.png')])

start_index = 36

for i, file_name in enumerate(png_files):
    file_path = os.path.join(input_folder, file_name)
    
    # Load image with alpha channel
    image = pygame.image.load(file_path).convert_alpha()
    width, height = image.get_size()
    
    # Create new surface with alpha
    new_image = pygame.Surface((width, height), pygame.SRCALPHA)
    
    # Replace non-transparent pixels with white
    for x in range(width):
        for y in range(height):
            color = image.get_at((x, y))
            if color.a != 0:
                new_image.set_at((x, y), pygame.Color(255, 255, 255, color.a))
    
    # Save with sequential filename
    output_file = os.path.join(output_folder, f"{start_index + i}.png")
    pygame.image.save(new_image, output_file)
    print(f"Saved {output_file}")

pygame.quit()
print("All images processed successfully!")