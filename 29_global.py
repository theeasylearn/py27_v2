amount = int(input("Enter the amount "))

def deposit():
    global amount
    a= 10000
    a= a+amount
    print(f"balance of your account {a}")

deposit()