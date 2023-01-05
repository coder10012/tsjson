import json

# 1. neue datei json.py
# 2. Import json 
# 3. print json
# 4. upload to github

fp = open("accounts.json")
obj = json.loads(fp.read())
print (str(obj))
