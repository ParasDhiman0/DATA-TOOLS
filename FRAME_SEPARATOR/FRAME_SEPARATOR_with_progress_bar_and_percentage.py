import cv2
import os
from tqdm import tqdm

# ==========================
INPUT_FOLDER = r"D:\DATA TOOLS\FRAME_SEPARATOR\Input data"
OUTPUT_FOLDER = r"D:\DATA TOOLS\FRAME_SEPARATOR\Output data"
SAVE_FPS = 15
# ==========================

VIDEO_EXTENSIONS = (
    ".mp4", ".avi", ".mov", ".mkv",
    ".wmv", ".flv", ".webm", ".m4v"
)

# Find all videos first
video_files = []

for root, dirs, files in os.walk(INPUT_FOLDER):
    for file in files:
        if file.lower().endswith(VIDEO_EXTENSIONS):
            video_files.append(os.path.join(root, file))

print(f"Found {len(video_files)} videos")

# Progress bar for videos
for video_path in tqdm(video_files, desc="Videos"):

    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 30

    frame_interval = max(1, round(fps / SAVE_FPS))

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    relative_path = os.path.relpath(
        os.path.dirname(video_path),
        INPUT_FOLDER
    )

    video_name = os.path.splitext(
        os.path.basename(video_path)
    )[0]

    output_dir = os.path.join(
        OUTPUT_FOLDER,
        relative_path,
        video_name
    )

    os.makedirs(output_dir, exist_ok=True)

    frame_number = 0
    saved_count = 0

    # Progress bar for frames
    with tqdm(
        total=total_frames,
        desc=video_name,
        leave=False,
        unit="frame"
    ) as pbar:

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            if frame_number % frame_interval == 0:

                filename = os.path.join(
                    output_dir,
                    f"frame_{saved_count:08d}.jpg"
                )

                cv2.imwrite(
                    filename,
                    frame,
                    [cv2.IMWRITE_JPEG_QUALITY, 95]
                )

                saved_count += 1

            frame_number += 1
            pbar.update(1)

    cap.release()

print("Finished!")