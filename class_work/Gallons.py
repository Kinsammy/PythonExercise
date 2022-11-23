import math

if __name__ == '__main__':
    diameter = int(input("Enter value for diameter: "))
    radius = diameter / 2
    feet = int(input("Enter value for feet: "))
    square_feet = (radius * radius) * math.pi
    # square per acre is 43560
    acres = square_feet / 43560
    # gallons per acre/foot 32581
    total_gallons = acres * feet * 325851
    print("The total gallons is ", total_gallons)
