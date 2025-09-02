def factorial(a):
    if a==1:
        return 1
    else:
        return (a*factorial(a-1))

a= int(input("Enter the value of a "))
b = factorial(a)
print(f"Factorial of a ={b}")