try:
    number = int(input("Enter the number to find out cube "))
    if number <0:
        print("Number is negative")
        number = 0-number
    cube = number**3
    print(cube)
except ValueError:
    print("Invalid Input enter valid input")