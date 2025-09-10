import random 

print(f"return random float number between 0 &1 is= {random.random()}")
print(f"return random float number between given range start,end ={random.uniform(10, 99)}")
print(f"return random integer number between given range ={random.randint(1,100)}")
print(f"return random integer number between given range ={random.randrange(1,100,5)}")

countries= ['India','usa','UK','Canada','Australia'] 
print(f"return random value from given list {random.choice(countries)}")
print(f"return random given number of value from list {random.choices(countries,k=7)}")

number = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
print(f"return before shuffle list {number}")
random.shuffle(number)
print(f"return after shuffle list {number}")

print(f"give sample from given data {random.sample(number,k=3)}")

