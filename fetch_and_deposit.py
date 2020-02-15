import requests
import json

request = requests.get('https://api.github.com/repos/torproject/tor/commits')

# function takes an endpoint request plus an array nmber
# and returns a python object
def get_obj(endpoint, listnum):
    string = json.dumps(endpoint.json(), indent=1)
    json_python_obj = json.loads(string)
    return(json_python_obj[listnum])

def listify_one_entry(json_single):
    return(json_single["sha"], json_single["committer"]["login"], json_single["commit"]["committer"]["date"])

entry_object = get_obj(request, 0)
#print(listify_one_entry(entry_object))

def loop_through_entries(url_request):
    list_of_lists = ()
    for i in range(21):
        jsn_obj = get_obj(url_request, i)
        listified = listify_one_entry(jsn_obj)
        list_of_lists = (list_of_lists,  listified)
    return(list_of_lists)

print(loop_through_entries(request))
