import cv2
import os

# ==========================
# SETTINGS
# ==========================
INPUT_FOLDER = r"D:\DATA TOOLS\FRAME_SEPARATOR\Input data"
OUTPUT_FOLDER = r"D:\DATA TOOLS\FRAME_SEPARATOR\Output data"

# Images to save per second
SAVE_FPS = 999

VIDEO_EXTENSIONS = (
    ".mp4",
    ".avi",
    ".mov",
    ".mkv",
    ".wmv",
    ".flv",
    ".webm",
    ".m4v"
)
# ==========================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

video_count = 0

for root, dirs, files in os.walk(INPUT_FOLDER):

    for file in files:

        if not file.lower().endswith(VIDEO_EXTENSIONS):
            continue

        video_path = os.path.join(root, file)

        print(f"\nProcessing: {video_path}")

        cap = cv2.VideoCapture(video_path)

        fps = cap.get(cv2.CAP_PROP_FPS)

        if fps <= 0:
            fps = 30

        frame_interval = max(1, round(fps / SAVE_FPS))

        relative_path = os.path.relpath(root, INPUT_FOLDER)

        video_name = os.path.splitext(file)[0]

        output_dir = os.path.join(
            OUTPUT_FOLDER,
            relative_path,
            video_name
        )

        os.makedirs(output_dir, exist_ok=True)

        frame_number = 0
        saved_count = 0

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            if frame_number % frame_interval == 0:

                frame_file = os.path.join(
                    output_dir,
                    f"frame_{saved_count:08d}.jpg"
                )

                cv2.imwrite(
                    frame_file,
                    frame,
                    [cv2.IMWRITE_JPEG_QUALITY, 95]
                )

                saved_count += 1

            frame_number += 1

        cap.release()

        print(
            f"Saved {saved_count} frames "
            f"from {frame_number} video frames"
        )

        video_count += 1

print(f"\nFinished! Processed {video_count} videos.")