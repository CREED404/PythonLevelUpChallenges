def save_dict(dictionary: dict, newFilename):
    "-".join([x+","+y for x, y in dictionary.items()])
    with open(newFilename, "w") as f:
        f.write("-".join([x+","+y for x, y in dictionary.items()]))

    

def load_dict(filename):
    with open(filename, "r") as f:
        return dict([(item.split(",")[0], item.split(",")[1]) for item in f.read().split("-")])

"""
  The above solution only works if The Dict's Keys & values are strings, the method below is highly recommended
"""
import pickle

def save_dict(object, filename):
  with open(filename, "wb") as f:
    pickle.dump(object, f)

def load_dict(filename):
  with open(filename, "rb") as f:
    object = pickle.load(f)
    return object
