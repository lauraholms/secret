import os

FILE = "data/notes.enc"

def load_notes():

    if not os.path.exists(FILE):

        return []

    with open(FILE, "rb") as f:

        return [f.read()]
