import os
import subprocess

new_path = r"ffmpeg-7.0.2-full_build\bin"
current_path = os.environ.get('PATH', '')

updated_path = current_path + ";" + new_path

try:
    subprocess.run(f'setx /M PATH "{updated_path}"', check=True, shell=True)
    print("DONE")
except subprocess.CalledProcessError:
    print("ERROR")
