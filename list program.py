fruits=["apples","Mango","Watermelon"]
print(fruits)#list is used in square brackets
print(fruits[0])
print(fruits[2])#ordered list(items have fixed position)
fruits[1]="orange"
print(fruits)#mutable(changed after creation)
numbers=[1,2,2,3,3,4]
print(numbers)#duplicate allowed
mixed=["python",23,5.67,True]
print(mixed)#stored different types
#TYPES OF LISTS
NUMBER=[12,13,14,15]
print(NUMBER)#Integer list
Name=["Jiya","Mahak","Moni","Neha"]
print(Name)#String list
price=[12.4,33.7,56.7]
print(price)#Float list
Flags=[True,False,True]
print(Flags)#Boolean list
Mixed=["Python",23,56.7,True]
print(Mixed)#Mixed list
Matrix=[
    [1,2,3],

    [4,5,6],
    [7,8,9]
]
print(Matrix)#Nested List
print(Matrix[1][2])#Access matrix elements
#Creating list
my_list=[1,2,3]
print(my_list)#Using Square Brackets
my_lists=((4,5,6))
print(my_lists)#Using list()Constructor
#List Indexing(index start from 0)
Color=["red","Blue","green"]
print(Color[0])
print(Color[1])
print(Color[2])
#   Negative inexing
Colors=["yellow","Orange","purple"]
print(Colors[-0])
print(Colors[-1])
print(Colors[-2])
#List Slicing
Number=[12,23,34,45]
print(Number[1:4])
print(Number[1:])
print(Number[:4])
print(Number[-4:-1])
#IMPORTANT LIST METHODS
fruit=["Apple","Banana","Lichi"]
fruit.append("Mango")
print(fruit)#Add an item in an list(append)
fruit.insert(1,"orange")
print(fruit)#insert(add item at a specific position)
fruit=["apple""banana","Mango"]
fruit.extend(["Watermelon","Jamuna"])
print(fruit)#extend(add multiple items)
fruit=["Apple","Watermelon","Banana","Lichi"]
fruit.remove("Banana")
print(fruit)#removes a specific items
fruit.pop(1)#Removes an item by index
print(fruit)
fruit.clear()
print(fruit)#removes all items(clear)
numbers=[50,10,69,58]
numbers.sort()
print(numbers)#sorts the list(Sort)
numbers.reverse()
print(numbers)
#reverse the list(reverse)
nums=[1,2,2,3,3,4,5,2]
print(nums.count(2))#counts occurrences(count)
fruits=["jamun","apples","Mango","Oranges"]
print(fruits.index("apples"))#(index)
language=["java","c","c++","python","js"]
mixed=["priya",25,70.5,[11,12,13],25]
numbers=[1,2,3,4,5,6,7,8,9,10]
print(type(mixed))
print(len(mixed))
print("mixed")
print(numbers[2:])
print("java" in language)
name=input("Enter your name:")
print("welcome",name)
language[2]="jiya","deepika"
print(language)
language.insert(3,"langchain")
print(language)
#List of Operators
List1=[1,2]
List2=[3,4]
print(List1+List2)#Concentration String
print([1]*5)#Repitation String
#Using loop
Fruits=["Mango","Banana","Watermelon","Orange"]
for fruit in Fruits:
 print(Fruits)#Using for loop
 Squares=[x*x for x in range(1,6)]
print(Squares)
numbers=[1,2,3,4,5,6]
numbers[:4]
print(numbers)