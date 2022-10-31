def palindrome(numbers):
    temp = numbers
    count = 0
    while numbers > 0:
        each_number = numbers % 10
        count = count * 10 + each_number
        numbers = numbers // 10
    if temp == count:
        return "The number is a palindrome!"
    else:
        return "The number is not a palindrome"


if __name__ == '__main__':
    number = int(input("Enter a number: "))
    print(palindrome(number))
