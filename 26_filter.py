l1 = [1,9,7,8,56,54,35,62,84,2,7]
a =[]
for i in l1:
    if i<40:
        a.append(i)
print(a)

x= filter(lambda x:x<40,l1)
print(list(x))
