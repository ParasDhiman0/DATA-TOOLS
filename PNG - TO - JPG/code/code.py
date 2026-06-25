# this code will convert all png images
# in a folder to jpg only and save them in a separate output 
# folder without deleting the original files
from PIL import Image
import os

input_folder = r"D:\input_images"
output_folder = r"D:\output_jpg"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".webp")):
        input_path = os.path.join(input_folder, file)

        img = Image.open(input_path).convert("RGB")

        output_name = os.path.splitext(file)[0] + ".jpg"
        output_path = os.path.join(output_folder, output_name)

        img.save(output_path, "JPEG", quality=95)

print("Conversion completed. All images have been saved as JPEG in the output folder.")