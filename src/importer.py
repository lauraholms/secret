import shutil

def restore(path):

    shutil.copy(

        path,

        "data/notes.enc"

    )
