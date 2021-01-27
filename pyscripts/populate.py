import json
import sys

fs = open('Resources/DropdownItems.json')
jsonFile = json.load(fs)
print(json.dumps(jsonFile))

sys.stdout.flush()