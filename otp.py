import random 

def getotp(k):
    if k<4:
        return "otp is not possible less then 4 digit"
    else:
        if k==8:
            otp = str(random.randint(10,99))+str(random.randint(10,99))+str(random.randint(10,99))+str(random.randint(10,99))
            return otp
        elif k==6:
            otp = str(random.randint(100000, 999999))
            return otp
        elif k==4:
            otp = str(random.randint(10,99))+str(random.randint(10,99))
            return otp
        else:
            return "invalid input"