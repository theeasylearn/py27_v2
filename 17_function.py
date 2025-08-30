# with argument with return

def getsum(a,b):
    sum= a+b
    return sum

# without argument without return
def setdate():
    print('Date is 30/08/2025')

# without argument with return
def getpi():
    pi =3.1415
    return pi

# with argument without return
def getday(a):
    if int(a)>7 or int(a)==0:
        print("Invalid input only 7 days in week")
    else:
        if a=='1':
            print('Monday')
        if a=='2':
            print('Tuesday')
        if a=='3':
            print('Wednesday')
        if a== '4':
            print('Thursday')
        if a== '5':
            print('Friday')
        if a== '6':
            print('Saturday')
        if a=='7':
            print('Sunday')

x = int(input("Enter the value of a "))
y = int(input("Enter the value of b "))

sum1 = getsum(x,y)
print(f"value of x={x}, y={y} sum of x+y={sum1}")


setdate()

p=getpi()
print("value of pi =",p)

d = input("Enter the number of Day")
getday(d)
