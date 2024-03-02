def get_travel_time_ms(distance, speed):  
    return distance / speed * 100.0 # bug fixed

if __name__ == "__main__":
    distance = 100 # m
    speed = 1 # m/s
    print("travel distance:", distance)
    print("travel speed:", speed)
    print("travel time:", get_travel_time_ms(distance, speed) * 100.0, " ms") # temp fix applied
