
Storm = True

print("Hi welcome to the storm categoriser!")
input("When your ready to start click any button!")

while Storm == True:
    raining = 1 
  
    while not raining == 0:
        storm_category = int(input("Please input a number for the category of a tropical storm: "))
        
        if storm_category >= 5 and storm_category <= 7:
            print("A category " + str(storm_category) + " storm is dangerous!")

        elif storm_category == 3 or storm_category == 4:
            print("A category " + str(storm_category) + " storm is quite bad!")

        elif storm_category >= 0 and storm_category <= 2:
            print("A category " + str(storm_category) + " storm is not terrible!")

        if not (storm_category >= 0 and storm_category <= 7):
            print("A category " + str(storm_category) + " storm does not exist!")

        sea_level = input("Sea Levels are rising I would recommend you try again: yes or no? ")

        if sea_level == 'yes':
            print("storm simulation beginning again!!!")

        else:
            raining = 0
            Storm = False
            print("storm simulation has ended.")
