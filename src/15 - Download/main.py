import os
import re
from urllib.parse import urlparse
import requests

def download_files(url, save_path):
  parsed_url = urlparse(url)
  base_path = parsed_url.scheme + "://" + parsed_url.netloc
  count = int(re.findall(r"\d+", parsed_url.path)[0])

  save_path = os.path.expanduser(save_path)
  os.makedirs(save_path, exist_ok=True)
    
  next = True
  while next:
    current_resource_name = f"image{str(count).zfill(3)}.jpg"
    
    try:
      source_url = f"{base_path}/{current_resource_name}"
      destination_path = os.path.join(save_path, current_resource_name)

      response = requests.get(source_url)
      response.raise_for_status()
      
      with open(destination_path, "wb") as f:
        f.write(response.content)

      print(f"Successfully download: {source_url}")
      count += 1
    except Exception as e:
      print(e)
      next = False
