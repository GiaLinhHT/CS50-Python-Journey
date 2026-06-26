import requests
import json
import sys
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument.")
elif !(sys.argv[1].isnumeric):
    sys.exit("Command-line argument is not a number.")

