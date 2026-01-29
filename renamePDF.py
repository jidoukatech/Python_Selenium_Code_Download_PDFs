import os
import re



for i in range(1,22):
    filename = rf"chapter-{i}.pdf"
    #print(filename)
    base_name, extension = os.path.splitext(filename)
    pattern = r"chapter-(\d+)"
    replacement = f"Lesson_{i}"
    new_base = re.sub(pattern, replacement, base_name)
    new_filename = new_base + extension

    if os.path.exists(filename):
        os.rename(filename, new_filename)
        print(f"Renamed: {filename} -> {new_filename}")
    else:
        print(f"Error: {filename} not found.")