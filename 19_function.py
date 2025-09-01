def getMerit(maths,science,english,computer,history,drawing):
    print(maths,science,english,computer,history,drawing)
    total = maths + science + english
    return	total
    
maths = 80
science = 90
english = 100
computer = 50
history = 45
drawing = 40
#bad way to call function because it creates wrong merit because arguments are passed in wrong sequence
print (getMerit(computer,history,drawing,maths,science,english))

#perfect way to call function (keyword argument style)
print (getMerit(computer=computer,history=history,drawing=drawing, maths=maths,science=science,english=english))