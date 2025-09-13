try:
    a = int(input("Enter the value of a"))
    b = int(input("Enter the value of b"))
    x = a/b
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("division by 0 is not possible")
except Exception as e:
    print("Something went wrong:", e)
else:
    print(f"value of a is {a} b is {b} division of a/b is {x}")