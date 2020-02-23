import kismet_rest
from pymongo import MongoClient 
def get_alert_generator():
    alerts = kismet_rest.Alerts(username="slyracoon23", password="12345678")
    for alert in alerts.all(ts_sec=1546300800):
        yield alert

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

user = db.alert

for alert in get_alert_generator():
    formated_alert = change_keys(alert, convert)
    user.insert_one(formated_alert)
    #break 

