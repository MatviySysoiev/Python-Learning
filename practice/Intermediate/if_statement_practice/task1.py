def route_info(dictionary):
    distance = dictionary.get('distance')
    speed = dictionary.get('speed')
    time = dictionary.get('time')
    if distance and isinstance(distance, int):
        return f"Distance to your destination is {distance}"
    elif (speed and isinstance(speed, (int, float))) and (time and isinstance(time, (int, float))):
        return f"Distance to your destination is {speed * time}"
    else:
        return "No distance info is available"


car_one = {
    'model': 'AUDI Q7',
    'speed': 15,
    'time': 3.5
}

car_two = {
    'model': 'BMW X5',
    'distance': 100
}

car_three = {
    "model": 'MERCEDES GLE',
}

print(route_info(car_one))  # Distance to your destination is 52.5
print(route_info(car_two))  # Distance to your destination is 100
print(route_info(car_three))  # No distance info is available
