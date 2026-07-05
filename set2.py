fruits={"apple","banana","mango"}
print(fruits)#creating a set using curly braces
a=set()#creating empty set
print(type(a))#type function(set type)
a={}
print(a)#None
print(type(a))#type is dict
num=set([1,2,3,4])
print(num)#creating a set using list
Nums={1,2,2,2,3,4,3,5}
print(Nums)#duplicate values are not allowed
data={"python",1,23.3,True}
print(data)#different data types
#unordered sets 
#accessing set elements
fruits={"watermelon","melon","dragon fruit","blueberry"}
for fruit in fruits:
 print(fruit)#accessing elements in correct way usong for loop
number={1,22,33,4,5,6,7}
for num in number:
 print(num)
 print(1 in number)# in function
 print(33 not in number)#not in function
#Adding Element
fruit={"apple","mango","grapes"}
fruit.add("blueberry")
print(fruit)#add method
fruit.update(["jammun","dragon fruit"])
print(fruit)#update function
#Removing function
num={1,2,3,4,5,6,7,8,9}
num.remove(2)
print(num)#remove function
num.discard(4)
print(num)#discard function
x=num.pop()
print(x)
print(num)#pop function
num.clear()
print(num)#clear function
del num#delete function
a={1,2,3}
b=a.copy()
print(b)#copying a set
number={1,2,3,4}
print(len(number))

#SET OPERATIONS
A={1,2,3}
B={4,5,6}
print(A|B)
print(A.union(B))#Union operation(combined all unique elements)

a={1,2}
b={2,8}
print(a&b)
print(a.intersection(b))
print(a.difference(b))#common values
print(a-b)#difference(element in A but not in B)
print(a^b)
print(a.symmetric_difference(b))#symmetric difference(elements in either set but not both)

#Set Methods:
A={1,2,3}
B=A.copy()
print(B)#Copy method
print(len(A))#LENGTH METHOD
print(max(A))#maximum number
print(min(A))#minumum number
print(sum(A))#Sum of all data

#SET COMPARSION METHODS
a={1,2,3,4}
b={1,2,3}
print(a.issubset(b))#issubset method(all elements of one set are present in another set)
print(a.issuperset(b))#issuperset method(set contains all the elements of anotherr set)
print(a.isdisjoint(b))#isdisjoint method(two sets have no common elements)

#Frozen Set
A=frozenset([1,2,3])
print(A)




