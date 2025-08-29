# Hollow square with single asterisk in center
r = int(input("Enter the number of row"))  # Size of the square (odd number for center)
c = int(input("Enter the number of column"))
if (r%2 == 0 or c%2 == 0):
    print("Even number is not valid")
else:
    for i in range(r):
        for j in range(c):
            # Print asterisk for border or center
            if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                print("*", end=" ")
            elif i == r // 2 and j == c // 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()