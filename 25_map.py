l1 = [1,9,7,8,56,54,35,62,84,2,7]
x = []
for i in l1:
    x.append(i*10)
print(x)

x =map(lambda a:a*10,l1)
print(list(x))