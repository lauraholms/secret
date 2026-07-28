from auth import authenticate
from manager import run

if authenticate():

    run()

else:

    print("Authentication failed.")
