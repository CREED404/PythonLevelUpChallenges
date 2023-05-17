import os
from zipfile import ZipFile

def zip_all(folder_path, extensions, output_filename):
  with ZipFile(output_filename, "w") as f:
    for root, _, files in os.walk(folder_path):
      for file in files:
        file_path = os.path.join(root, file)

        if file.lower().endswith(tuple(ext.lower() for ext in extensions)):
          rel_path = os.path.relpath(file_path, folder_path)
          f.write(file_path, rel_path)