import json
import kismetdb
kismet_log_file = "Kismet-20200223-02-25-07-1.kismet" 
devices = kismetdb.Devices(kismet_log_file)

# Get alert metadata
all_devices_meta = devices.get_meta()
for device in all_devices_meta:
    print(device)

# Get payload from all alerts
#all_alerts = alerts.get_all()
#for alert in all_alerts:
#    print(json.loads(alert["json"])["kismet.alert.text"])
