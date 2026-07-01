#List in python
Fruits=["mango","banana","Orange"]
print(Fruits)#collection of ordered items that can be modified

Data=["Python",12,4.5,True]
print(Data)# can stored different data types

numbers=[10,20,30]
numbers[1]=34
print(numbers)#Modifying a list

# Adding Elements
Name=["Jiya","Mahak","Moni"]
Name.append("Priti")
print(Name)#append(adding element at last position)

Num=[10,20,30,40]
Num.insert(1,15)
print(Num)#insert(adding an element at a specific position)

#Removing Elements
Num=[10,20,30,40]
Num.remove(20)
print(Num)#remove

Num=[10,20,30]
Num.pop()
print(Num)#pop(removing an element)

items=[21,34,2,12,56,43,23]
items.sort()
print(items)#sort(arranged in ascending order)

items.reverse()
print(items)#reverse(arranged in descending order)

items.clear()
print(items)#clear(removed all items)

items=[12,12,12,13,23,45,54,657]
items.copy()
print(items)#copy list

items=[11,12,13,14,15,16]
print(items.count(12))#count occurences

print(items.index(11))

#TUPLE IN PYTHON
name=("Jiya","Mahak","Moni")
print(Name)#Tuple 

student=("Student",12,12.3)
print(student)#different data types

numbers=(10,20,30,40)
print(numbers)
##Tuple Methods
# Tuples have only two methods
numbers=(1,2,3,3,3,4,5)
print(numbers.count(3))#Count Methods

Num=(10,20,30,40)
print(Num.index(20))#Index method

#Example Comparing List and Tuple
fruits=["Apple","Banana","Mango"]
fruits.append("Orange")
print(fruits)

colors=("Red","Blue","Green","white")
print(colors)

data=(1,2,[3,4])
print(data)##Can a tuple contain a list

data=[1,2,(3,4)]
print(data)#Can a list contain tuple