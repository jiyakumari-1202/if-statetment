items={
    "home":"Decorative items",
    "Furniture":"Table",
    "vegetable":"carrot"
}
# print(len(items))#length of items
student=dict(name="Jiya",
             age=19,
             height=5.1)
print(student)#using constructor
print(type(student))#type method
num=[("a",1),("b",2),("c",3)]
d=dict(num)
print(d)#tuple convert into dict
Data=[("lang","Python"),      
      ("num",12),
      ("price",23.4),
      ("status",True)]
d=dict(Data)
print(d)