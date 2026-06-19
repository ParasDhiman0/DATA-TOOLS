# cleanup_noface.py
import os, random

folder  = "D:\\my_face_ai\\dataset\\noface"
target  = 2000          # how many to keep
files   = os.listdir(folder)
current = len(files)

print(f"Current noface images: {current}")
print(f"Deleting {current - target} random images...")

# Randomly delete extras
to_delete = random.sample(files, current - target)
for f in to_delete:
    os.remove(os.path.join(folder, f))

print(f"Done! Remaining: {len(os.listdir(folder))} images")