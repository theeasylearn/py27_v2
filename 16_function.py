#define function
def getsquare(n):
    result = n**2
    return result

number = int(input("Enter the number to find out square"))

# call function
x =getsquare(number)
print(f"square of {number} is {x}")