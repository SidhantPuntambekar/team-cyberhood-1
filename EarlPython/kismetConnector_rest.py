import kismet_rest
import requests
import time
conn = kismet_rest.KismetConnector(username="slyracoon23", password="12345678")
for device in conn.device_summary():
    print(device['kismet.device.base.manuf'])
    r = requests.get(url = "http://www.google.com")
    print(r)
    time.sleep(0.5)

