#TUPLE IN PYTHON
Tuple=(10,20,30,40,50,60,70,80)
a=list(Tuple)
print(a)
a[5]=98
print(a)
Tuple=tuple(a)
print(Tuple)


Matrix=[
    [1,2,3],
    [2,3,4],
    [3,4,5]
]
print(Matrix)
print(len(Matrix))

#Creating a new tuple
t=(10,20,30)
t=(t[1],25,t[2])
print(t)

#Types of tuple
t=()
print(t)#Empty tuple

t=(10,)
print(type(t))#Single tuple element(print tuple)

t=(12)
print(type(t))#without the commas(print int)

t=(1,2,3,4,5,6)
print(t)#multiple tuple

t=("jiya",12,12.4,True)
print(t)#Mixed data type tuple

t=((1,2),(3,4),(5,6))
print(t)#Nested Tuple
print(t[1])

numbers=1,2,3,4
print(numbers)#Without parenthese

Text=("JIYA",11,56.5,(1,2),(4,5),[23,87],True)#Tuple
print(Text)
text1=list(Text)#convert into list

print(text1)
text1.pop()#pop operation
print()

Text=tuple(text1)#list convert into tuple
print(Text)

number=(1,2,3,4,5,6,7,8,9,10)
print(number)
number1=list(number)


number=tuple(number1)
print(number)

t1=(2,3)
t2=(4,5)
print(t1+t2)#Concatenation method

name=("Jiya","mahak","priti")
a,b,c=name
print(a)
print(b)
print(c)#unpacking method

#different types of unpacking method
student=("Jiya",19,"BCA")
name,age,course=student
print(name)
print(age)
print(course)

number=(10,(20,30),(40,50),60,70,80)
#n1,n2,n3,n4,*n5=number
#print(n1)
# print(n2)
# print(n3)
# print(n4)
# print(*n5)

Num=(12,13,14,15,16)
num1=list(Num)

del Num
print(Num)

