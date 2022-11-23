if __name__ == '__main__':

    total_gallons = 0.0
    total_mile = 0.0
    counter = 0

    gallon = float(input("Enter the gallons or -1 to quit: "))
    mile = float(input("Enter the float or -1 to quit: "))
    while gallon != -1 and mile != -1:
        mile_per_gallon = mile / gallon
        print("The miles / gallon is:",mile_per_gallon)
        total_gallons += gallon
        total_mile += mile

        gallon = float(input("Enter the gallons or -1 to quit: "))
        mile = int(input("Enter the float or -1 to quit: "))
        counter += 1

    if counter != 0:
        average = total_mile / total_gallons
        print("The trip is: " ,counter)
        print("The overall average miles / gallon is: ", average)
    else:
        print("No trip!")