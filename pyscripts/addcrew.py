import sys,json
data = sys.stdin.readlines()

print(data[0])

# Edit JSON object then write to file
fs = open('Resources/DropdownItems.json')
jsonFile = json.load(fs)
jsonFile["crew_list"].append(data[0].replace('"', '').rstrip())
fs.close()

with open('Resources/DropdownItems.json', 'w', encoding='utf-8') as f:
    json.dump(jsonFile, f, ensure_ascii=False, indent=4)

print(jsonFile["crew_list"])
sys.stdout.flush()