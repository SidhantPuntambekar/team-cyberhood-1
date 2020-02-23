import kismet_rest
from pymongo import MongoClient

def get_device_json_generator():
    conn = kismet_rest.KismetConnector(username="slyracoon23", password="12345678")
    for device in conn.device_summary():
        #print(device)
        yield device
'''
def print_dict(d):
    new = {}
    for k, v in d.items():
        if isinstance(v, dict):
            v = print_dict(v)
        elif isinstance(v, list):
            for elem in v:
                if isinstance(elem, dict):
                    
        try:
            new[k.replace('.', '-')] = v.replace('.','-')
        except AttributeError:
            new[k.replace('.', '-')] = v
    return new
'''
def convert(k):
    return k.replace('.','-')


def change_keys(obj, convert):
    """
    Recursively goes through the dictionary obj and replaces keys with the convert function.
    """
    if isinstance(obj, (str, int, float)):
        return obj
    if isinstance(obj, dict):
        new = obj.__class__()
        for k, v in obj.items():
            new[convert(k)] = change_keys(v, convert)
    elif isinstance(obj, (list, set, tuple)):
        new = obj.__class__(change_keys(v, convert) for v in obj)
    else:
        return obj
    return new



client = MongoClient('mongodb+srv://EarlPotters:cyberhood12345@hackcu-cyberhood-kismet-data-phlpm.gcp.mongodb.net/test?retryWrites=true&w=majority')

db = client.get_database('cyberhood')

user = db.user

for device in get_device_json_generator():
    formated_device = change_keys(device, convert)
    user.insert_one(formated_device)
    break 



