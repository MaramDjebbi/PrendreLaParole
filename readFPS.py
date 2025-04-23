import cv2
import os

# Parent folder containing the resident folders
base_path = "/home/maram/Downloads/Videos_résidents/newFPS"
residents = ["resident1", "resident2", "resident3"]

for resident in residents:
    folder_path = os.path.join(base_path, resident)
    print(f"\n--- {resident} ---")
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".mp4"):
            video_path = os.path.join(folder_path, filename)
            cap = cv2.VideoCapture(video_path)

            if not cap.isOpened():
                print(f"Failed to open {filename}")
                continue

            fps = cap.get(cv2.CAP_PROP_FPS)
            frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            duration = frame_count / fps if fps > 0 else 0

            print(f"  {filename}: {fps:.2f} FPS | {duration:.2f} seconds")

            cap.release()
