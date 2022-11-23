def is_leap_year(year):
    if year % 4 == 0:
        return f"The {year} is a leap year!"
    else:
        return f"The {year} is not a leap year!"


if __name__ == '__main__':
    current_year = int(input("Enter the year to know if is leap year or not: "))
    print(is_leap_year(current_year))