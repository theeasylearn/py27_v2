# default argument
# (x+y)**2 = x**2+ 2*x*y +y**2

def square(x=0,y=0):
    squ = x*x +2*x*y +y**2
    print(x,y)
    return(squ)

# x = int(input("Enter the value of x "))
# y = int(input("Enter the value of y "))

# s = square(x,y)
s= square(3)
s = square(y=2)
s = square(y=2,x=3)
print(s)