from src.storage import load_notes

def test_storage():

    assert isinstance(load_notes(), list)
