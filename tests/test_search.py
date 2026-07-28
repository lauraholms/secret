from src.search import search

def test_search():

    notes = ["crypto wallet", "shopping"]

    assert len(search(notes, "crypto")) == 1
