import otp
n= int(input("Enter the number for otp "))
x=otp.getotp(n)
print(x)