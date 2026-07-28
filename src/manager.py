from storage import load_notes

def run():

    notes = load_notes()

    print("Secure Notes Manager")

    print(f"Loaded {len(notes)} notes.")
