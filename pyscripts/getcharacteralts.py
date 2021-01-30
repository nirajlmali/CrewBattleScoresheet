import sys,os,json

paths = {
    "paths" : []
}
for root, dirs, files in os.walk("./Resources/CharacterIcons/Mario"):
    for filename in files:
        paths["paths"].append(filename)

print(json.dumps(paths))
sys.stdout.flush()