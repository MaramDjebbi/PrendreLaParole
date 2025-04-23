import os
import subprocess

base_path = "/home/maram/Downloads/Videos_résidents/Cropped"
residents = ["resident1", "resident2", "resident3"]
output_base = "/home/maram/Downloads/Videos_résidents/newnewFPS"
target_fps = 25

os.makedirs(output_base, exist_ok=True)

for resident in residents:
    input_folder = os.path.join(base_path, resident)
    output_folder = os.path.join(output_base, resident)
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".mp4")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            cmd = [
                "ffmpeg",
                "-i", input_path,
                "-filter:v", f"fps={target_fps}",
                "-c:a", "copy",
                output_path
            ]

            print(f"Converting {filename} to {target_fps} FPS...")
            subprocess.run(cmd)
