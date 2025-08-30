# default argument
# (x+y)**2 = x**2+ 2*x*y +y**2

def square(x=0,y=0):
    squ = x*x +2*x*y +y**2
    return(squ)

# x = int(input("Enter the value of x "))
# y = int(input("Enter the value of y "))

# s = square(x,y)
s = square(y=2)
print(s)