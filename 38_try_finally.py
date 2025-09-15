try:
    age = int(input("Enter your age when you starting job"))
    if age<18 or age>60:
        raise ValueError 
    else:
        y = 60-age
except ValueError:
    print("you are not valid for doing job")
else:
    print(f"your age is {age} you have remaining {y} year to do work")

finally:
    print("thank you for trying")
