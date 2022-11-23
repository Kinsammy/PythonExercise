import math

if __name__ == '__main__':
    radius = int(input("Enter a value for radius: "))
    diameter = radius * 2
    circumference = radius * radius * math.pi
    print("diameter is: %d\nand the circumference:  %.2f" %(radius, circumference))