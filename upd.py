import requests
import sys,os
import time

version = 1000

def upd():
 req = requests.get("https://raw.githubusercontent.com/kallibr44/Sattelite-tracker/master/version")
 raw = req.content
 if (int(raw) != version):
     print("New version detected! Loading...")
     time.sleep(1)
     print("Downloading new version...")
     time.sleep(1)
     os.system("git clone https://github.com/kallibr44/sattelite-tracker")
     print("Download complete!")
     time.sleep(1)
     print("Copying new files...")
     os.system("sudo cp -rf ./sattelite-tracker ../")
     print("Copying complete!")
     time.sleep(1)
     os.system("sudo rm -r ./sattelite-tracker && rm version")
     print("All done! Reloading...")
     os.system("python sattrack.py")
