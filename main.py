from os import path
PATH=path.dirname(path.realpath(__file__))+'/'
with open(f"{PATH}config.json", "r", encoding="utf-8-sig") as f:
	config = json.load(f)
print(config)
