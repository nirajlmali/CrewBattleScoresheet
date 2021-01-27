import json
import sys

fs = open('Resources/CrewList.json')
jsonFile = json.load(fs)
print(json.dumps(jsonFile))

sys.stdout.flush()