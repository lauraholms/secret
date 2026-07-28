def search(notes, keyword):

    return [

        note

        for note in notes

        if keyword.lower() in note.lower()

    ]
