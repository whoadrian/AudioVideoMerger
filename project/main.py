import os.path
import shutil
import tkinter as tk
from pathlib import Path
from tkinter import filedialog
import ffmpeg

root = tk.Tk()
root.withdraw()

print("Welcome to the Sound Designers Challenger Helper!")
print("video file + audio files = <3 multiple video files, each with an audio file")
print("output folder: directory of video file")

input("Press Enter to continue...")

try:
    # Video selection
    video_path = filedialog.askopenfilename(parent=root, title="Select a video file")
    if len(video_path) > 0 & os.path.isfile(video_path):
        print(f"video path: {video_path}")
        input_video = ffmpeg.input(video_path)
        video_extension = Path(video_path).suffix
        video_name = Path(video_path).stem

        print(f"video name: {video_name}")
        print(f"video extension: {video_extension}")

        # Audio selection
        audio_paths = filedialog.askopenfilenames(parent=root, title="Select the audio files")
        if len(audio_paths) > 0:

            # Set up output folder
            output_folder = Path(video_path).parent.absolute() / "output_folder"
            if os.path.isdir(output_folder):
                shutil.rmtree(output_folder)
            os.mkdir(output_folder)

            print(f"created output folder at {output_folder}")

            # Generate output
            print("generating...")
            print("")
            for path in audio_paths:
                audio_name = Path(path).stem
                output_path = output_folder / f'{video_name}_{audio_name}.mp4'
                input_audio = ffmpeg.input(path)

                print(f"audio path: {path}")
                print(f'output path: {output_path}')

                c = ffmpeg.concat(input_video, input_audio, v=1, a=1).output(filename=output_path).run(overwrite_output=True)

                print("done.")

        else:
            print("audio selection empty!")

    else:
        print("video path selection empty!")

except Exception as e:
    print(f"(!) Error: {e}")
    print("Errors detected!")

finally:
    input("Press Enter to exit...")
    print("exiting...")

