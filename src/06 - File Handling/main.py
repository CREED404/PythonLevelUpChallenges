import pickle

def save_dict(object, filename):
  with open(filename, "wb") as f:
    pickle.dump(object, f)

def load_dict(filename):
  with open(filename, "rb") as f:
    object = pickle.load(f)
    return object