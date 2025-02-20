def launch_sequence():
    print("Initiating countdown...")
    print("3... 2... 1... lift off!")
launch_sequence()
def travel_time_to_mars(distance, speed):
    time= distance/speed
    print("Travel time to mars is:", time, "Hours")
    travel_time_to_mars(225000000, 25000)
    def travel_tim_to_mars(Distance,speed): 
        time= distance/speed
        if speed < 20000:
            print("Warning: Speed is too slow for a timly arrival!")
        print("Travel time to mars is:", time, "hours")
    travel_time_to_mars(225000000, 15000) #Too slow
    travel_time_to_mars(225000000, 55000) #Too fast
    travel_time_to_mars(225000000, 30000) #Just right
def mars_mission(Distance, speed, fuel, crew_ready):
    if speed < 20000:
        print("Warning: Speed is too slow for a timely arrival!")
    elif speed > 50000:
        print("Warning: Speed is too fast, risk of over shooting mars!")
    else:
        print("Speed is optimal for mara mission.")

    if fuel < 500000:
        print("Warning:Not enough fuel for the journey!")
    else:
        print("Fuel levels are sufficent.")
    
    if crew_ready:
        print("Crew is ready for the mission.")
    else:
        print("Crew is not ready. Mission delayed.")

    print("Estimated travel time to Mars:", travel_time_to_mars, "Hours.")
mars_mission(225000000,25000,600000,True)
mars_mission(225000000,15000,400000,True)
mars_mission(225000000,30000,700000,False)
