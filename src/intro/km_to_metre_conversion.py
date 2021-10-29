def km_per_hour_to_metre_per_seconds(speed):
    speed_in_metres_per_seconds = speed*(1000/3600)
    return speed_in_metres_per_seconds


def metre_per_seconds_to_km_per_hour(speed):
    km_per_hour = speed*(3600/1000)
    return km_per_hour


speed_in_metre_per_second = float(input('Enter the speed in M/S: '))
print(metre_per_seconds_to_km_per_hour(speed_in_metre_per_second), 'Km/hr')


speed_in_km_per_hour = float(input('Enter the speed in KM/H: '))
print(km_per_hour_to_metre_per_seconds(speed_in_km_per_hour), "m/s")
