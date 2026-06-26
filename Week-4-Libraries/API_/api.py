import requests
import json
def main():
    response = requests.get("https://api.artic.edu/api/v1/artworks/search")
    content = response.json()
    print(content)
    for i in content["data"]:
        print(f"{i['title']}")