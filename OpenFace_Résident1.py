import os
import subprocess
import pandas as pd

base_path = "/home/maram/Downloads/PrendreLaParole/newFPS/resident1"
emotions = ["happiness", "fear", "surprise", "anger", "disgust", "sadness"]

openface_cmd = "/home/maram/OpenFace/build/bin/FeatureExtraction"

for emotion in emotions:
    emotion_path = os.path.join(base_path, emotion)

    video_file = next((f for f in os.listdir(emotion_path) if f.endswith(".mp4")), None)

    if video_file:
        video_path = os.path.join(emotion_path, video_file)

        cmd = [
            openface_cmd,
            "-verbose",
            "-f", video_path,
            "-out_dir", os.path.join(emotion_path, "OpenFaceOutput")
        ]

        print(f"Processing {emotion}: {video_file}")
        subprocess.run(cmd)

        # Now process the generated CSV
        csv_name = video_file.replace(".mp4", ".csv")
        csv_path = os.path.join(emotion_path,"OpenFaceOutput", csv_name)

        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)

            # Keep only AU columns + essential info columns
            selected_columns = [col for col in df.columns if col.startswith("AU") or col in ["frame", "face_id", "timestamp", "confidence", "success"]]
            filtered_df = df[selected_columns]

            output_csv_path = os.path.join(emotion_path, f"OpenFace_AU_only_{csv_name}")
            filtered_df.to_csv(output_csv_path, index=False)
            print(f"Saved AU-only CSV for {emotion} to {output_csv_path}")
        else:
            print(f"CSV not found for {emotion}: {csv_path}")
    else:
        print(f"No video found in {emotion_path}")
