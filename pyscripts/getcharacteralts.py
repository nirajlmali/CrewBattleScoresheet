import sys,os,json
from pathlib import Path

paths = {
    "paths" : []    
}

data = sys.stdin.readlines()
char = data[0].replace('"', '').rstrip()
path = "./Resources/CharacterIcons/" + char

alternate = True

for root, dirs, files in os.walk(path):
    for filename in files:
        if alternate == True:
            paths["paths"].append(filename)
        alternate = not alternate

print(json.dumps(paths))

sys.stdout.flush()