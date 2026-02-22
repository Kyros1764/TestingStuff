from logging import warning
import requests
import json
import customtkinter as ctk

url = "https://pastebin.com/raw/MKdkTECb"

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
    
class frame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill="both", expand=True)
        self.populate()

    def populate(self):
        events = fetchEventsList()
        for event in events:
            radioBtn = ctk.CTkRadioButton(self, text=event)
            radioBtn.pack(pady=5)