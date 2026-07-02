#Set in python
#it has used{}syntax
#it is an unordered and it is mutable
# duplicate words are not allowed
# it is a unique set
# it cannot change the items when its added
# when we assign 1 and true then print only one element

Name={"Jiya","Mahak","Moni"}
print(Name)#set syntax example
Data={"Python",12,13.2,True}
print(Data)#multiple types of data are stored
print(len(Data))#Length method
print(type(Data))#Type function
print(int(13.2))#convert float into int
marks=[10,20,30,40]
print(set(marks))#list changed into set
print(type(marks))
Num=[1,2,3,4,5,6]
Num1=set(Num)
print(Num1)#List convert into set
print(type(Num1))

Data=(10,20,30,40,50)
print(Data)
Values=set(Data)
print(Values)#Tuple convert into set
print(type(Values))

Data={}
print(Data)#for dict
print(type(Data))

Data={1,2,3,4,5}
Data.remove(1)
print(Data)#remove function

empty=set()
print(empty)
print(type(empty))#for empty set

data={"jiya","Mahak",1,True,False,0}
print(data)
print("jiya" in data)#present in variable(in keyword)

print("HELLO"not in data)#not present in variable(not in keyword)

data={1,2,3,4,5}
for a in data:
    print(a)#for loop
print(2 in data)
print(6 not in data)

hobby={"dance","listening music"}
hobby.add("Travelling")
print(hobby)

set1={"JIYA","MAHAK","mONI"}
set2={"Jangra","Rajput","Rao"}
set1.update(set2)#update method for adding two sets
print(set1)

Text=["i am a python learner"]
Text1={"i am a python language programmer"}
print(Text)

Data={1,2,3,4,5}
data.remove(4)
print(data)

data.discard(6)
print(data)#discard function

set={1,2,34,5,4}
set2={221,34,54,75}
del set
print(set2)#delete method



