import json

def save_dict(object, filename):
  with open(filename, "w") as f:
    json.dump(object, f)

def load_dict(filename):
  with open(filename, "r") as f:
    object = json.load(f)
    print(object)