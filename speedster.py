speed_limit = int(input("Enter speed limit km/h:"))
speed_in_km = int(input("Enter your speed in km/h:"))
points = (speed_in_km - speed_limit) / 5

# If speed is less than or equal to 60


if speed_in_km <= 60:
    print("OK")
    # Give demerits to every km over the speed limit


elif speed_in_km > speed_limit:
    if points < 12:
        print("Demerit points:" + str(points))
    elif points > 12:
        print("You are going to jail. Demerit points:" + str(points))
