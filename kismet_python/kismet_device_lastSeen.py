import kismet_rest
devices = kismet_rest.Devices()
for device in devices.all(ts=1546300800):
    print(device)
