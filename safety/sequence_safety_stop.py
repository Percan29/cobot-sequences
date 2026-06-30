temperature = 85

def safety_stop(temp):
    if temp > 80:
        print("Temperature too high! Emergency stop activated.")
    else:
        print("Temperature normal. Continuing operation.")

safety_stop(temperature)

# Note:
# Safety logic used in cobots and industrial robots.
# Emergency stop conditions are critical in automated environments.
