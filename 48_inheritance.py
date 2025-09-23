class Base1: 
	def __init__(self):  #constructor
		self.name = "saprem" #instance variable
		print("Base1 class constructor called…..")
class Base2: 
	def __init__(self): #constructor
		self.surname = "Donda"		
		print("Base2 class constructor called…")
class Derived(Base1, Base2):  #multiple inheritance.
	def __init__(self): #constructor
		# Calling constructors of Base1 
		# and Base2 classes 
		Base1.__init__(self) #calling parent class 
		Base2.__init__(self) #calling parent class 
		print("Derived class constructor called")
	def printStrs(self): 
		print(self.name, self.surname) 
d1 = Derived() 
d1.printStrs() 

