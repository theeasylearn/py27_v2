l1= ['asad','uig','fbf','hjfgd',123,54,3,8,9,54,15.5]
l2 = [123,54,3,8,9,54,15.5]
l1.append(True)
print('append(True)',l1) # append()  #Add an element to the end of the list    
l1.extend(l2)
print('extend(l2)',l1)    # extend(list)  #Add  set of values(list) at the end of list. 
l1.insert(5,l2)
print('insert(l2)',l1)    # insert(position,item)  #Insert an item at the defined position  
l1.remove(123)  
print('remove(123)',l1)    # remove(item)  #Removes given item from the list    
print(l1.pop(4))
print(l1)    # pop(position)  #Removes and returns an element at the given position
print(l1.index(123))   # index()  #Returns the index of the first matched item    
print(l1.count(3))    # count(item)  #Returns the count of the number of items passed as an argument    
print(l2)
l2.sort()
print(l2)# sort()  #Sort items in a list in ascending order if all items are of same type    
l1.reverse()
print(l1)   # reverse()  #Reverse the order of items in the list    
l3 = l1.copy()    
print(l3)# copy()  #Returns a shallow copy of the list
l3[5] = True
print(l3) # l3 is a copy of l1, so changing l3 does not
print(l1)
l3.clear()    # clear()  #Removes all items from the list
print(l3)
del l3
print(l3)