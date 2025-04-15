def travel_details():
    start_location = input("Enter starting location: ")
    destination = input("Enter destination: ")
    mode_of_transport = input("Enter mode of transport (e.g., Car, Bus, Motorcycle): ")

    distance = float(input("Enter distance in kilometers: "))
    speed = float(input("Enter speed in km/h: "))

    travel_time = distance / speed

    takes_longer_than_5_hours = travel_time > 5

    print("\n--- Travel Details ---")
    print(f"Starting Location: {start_location}")
    print(f"Destination: {destination}")
    print(f"Mode of Transport: {mode_of_transport}")
    print(f"Distance: {distance} km")
    print(f"Speed: {speed} km/h")
    print(f"Estimated Travel Time: {travel_time:.2f} hours")

    if takes_longer_than_5_hours:
        print("Warning: Your trip takes more than 5 hours.")
        print("Recommendation: A rest stop is advised.")
    else:
        print("Your trip is under 5 hours. No rest stop is necessary.")

travel_details()