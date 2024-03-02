def get_travel_time_ms(distance, speed):
    return distance / speed # this is the bug: output in secs instead of millisecs

if __name__ == "__main__":
    distance = 100 # m
    speed = 1 # m/s
    print("travel distance:", distance)
    print("travel speed:", speed)
    print("travel time:", get_travel_time_ms(distance, speed) * 100.0, " ms") # temp fix applied
