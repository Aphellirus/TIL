import urllib.request

import json

api=urllib.request.urlopen("https://api.quotable.io/random")

api_data=api.read()

api_data_info=api_data.decode()

a = json.loads(api_data_info)

print("Topic - {}".format(a["tags"][0]))

print("---------------------------------\n")

print(a["content"])

print("\n---------------------------------\n")

print("-- By {}".format(a["author"]))
