
import os
import random
from PIL import Image

folder = r"D:\my_face_ai\dataset\face"

for file in random.sample(os.listdir(folder), 20):
    print(file)