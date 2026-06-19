import cv2
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

# ==========================
INPUT_FOLDER = r"D:\"
OUTPUT_FOLDER = r"D:\"
SAVE_FPS = 2
MAX_WORKERS = 8 # Number of concurrent threads
# ==========================

VIDEO_EXTENSIONS = (
    ".mp4", ".avi", ".mov", ".mkv",
    ".wmv", ".flv", ".webm", ".m4v"
)


def process_video(video_path):
    try:
        cap = cv2.VideoCapture(video_path)

        fps = cap.get(cv2.CAP_PROP_FPS)
        if fps <= 0:
            fps = 30

        frame_interval = max(1, round(fps / SAVE_FPS))

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

        cap.release()

        return f"{video_name}: {saved_count} frames"

    except Exception as e:
        return f"ERROR in {video_path}: {e}"


def main():

    video_files = []

    for root, dirs, files in os.walk(INPUT_FOLDER):
        for file in files:
            if file.lower().endswith(VIDEO_EXTENSIONS):
                video_files.append(os.path.join(root, file))

    print(f"\nFound {len(video_files)} videos\n")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:

        results = list(
            tqdm(
                executor.map(process_video, video_files),
                total=len(video_files),
                desc="Processing Videos"
            )
        )

    print("\nFinished!\n")

    for r in results:
        print(r)


if __name__ == "__main__":
    main()
