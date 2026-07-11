list1=[]
for i in range (5):
    num=input("enter the product:")
    list1.append(num) 
print(list1)
delete_product=(input("delete your product : "))
list1.remove(delete_product)
print(list1)
print(len(list1))