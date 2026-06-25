#this code will convert all png images 
# in a folder to jpg and delete the original png files

from PIL import Image
import os

folder = r"D:\images"

for file in os.listdir(folder):
    if file.lower().endswith(".png"):
        png_path = os.path.join(folder, file)
        jpg_path = os.path.splitext(png_path)[0] + ".jpg"

        try:
            img = Image.open(png_path).convert("RGB")
            img.save(jpg_path, "JPEG", quality=95)
            img.close()

            os.remove(png_path)  # Delete original PNG

            print(f"Converted: {file}")

        except Exception as e:
            print(f"Error with {file}: {e}")

print("Done!")