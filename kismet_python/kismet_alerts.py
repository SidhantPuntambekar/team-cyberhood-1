import kismet_rest
alerts = kismet_rest.Alerts(username="slyracoon23", password="12345678")
for alert in alerts.all(ts_sec=1546300800):
    print(alert)
