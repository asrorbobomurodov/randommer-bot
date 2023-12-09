from settings import URL, API_KEY
import requests

def getUpdates():
    url = f"{URL}/getUpdates"
    headers = {
        "X-Api-Key": API_KEY
    }

    r = requests.get(url, headers=headers)
    return r.json()['result'][-1]

# print(getUpdates())