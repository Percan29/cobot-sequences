sensor_ok = True

def sensor_check():
    if sensor_ok:
        print("Sensor OK. Starting sequence.")
    else:
        print("Error: part not detected. Stopping robot.")

sensor_check()

# Note:
# Typical decision logic in cobots using digital sensors.
