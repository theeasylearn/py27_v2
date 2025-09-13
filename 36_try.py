number= ['the',23,5,76,9,3,5,7]
sum = 0
count = 0
for i in number:
    try:
        sum = sum + i
        count += 1
    except:
        print("No")

print(f"sum of number is {sum}, count of number {count}")
print(f"Average of list {(sum/count)}")