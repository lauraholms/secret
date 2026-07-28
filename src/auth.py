import os
from getpass import getpass
from dotenv import load_dotenv

load_dotenv()

def authenticate():

    password = getpass("Master password: ")

    return password == os.getenv("MASTER_PASSWORD")
