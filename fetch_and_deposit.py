import requests
import json

request = requests.get('https://api.github.com/repos/torproject/tor/commits')

# function takes an endpoint request plus an array nmber
# and returns a python object
def get_obj(endpoint, listnum):
    string = json.dumps(endpoint.json(), indent=1)
    json_python_obj = json.loads(string)
    return(json_python_obj[listnum])

entry_object = get_obj(request, 0)
print(entry_object)
print(entry_object["sha"])
