import os
import sys
import shutil
from datetime import datetime

def backup_files(src, dest):
    if not os.path.isdir(src):
        print("Source directory does not exist:", src)
        return

    if not os.path.exists(dest):
        os.makedirs(dest)

    for filename in os.listdir(src):
        src_file = os.path.join(src, filename)
        if os.path.isfile(src_file):
            dest_file = os.path.join(dest, filename)

            # Add timestamp if file exists in destination
            if os.path.exists(dest_file):
                name, ext = os.path.splitext(filename)
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                dest_file = os.path.join(dest, f"{name}_{timestamp}{ext}")

            shutil.copy2(src_file, dest_file)
            print(f"Copied: {filename}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python python_assignment_Q3.py <source_dir> <destination_dir>")
        return

    backup_files(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
