from logging import warning
import requests
import json

url = "https://raw.githubusercontent.com/Kyros1764/TestingStuff/refs/heads/master/Manifests/manifests.json"

def fetchEventsList():
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        print(data)
        return [i["ManifestName"] for i in data["Manifests"]]
    except requests.RequestException as e:
        warning(f"Network error fetching list: {e}")
        return []
    except (KeyError, ValueError) as e:
        warning(f"Error parsing response: {e}")
        return []

if __name__ == "__main__":
    print(fetchEventsList())