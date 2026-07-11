marks=[20,30,10,90,10,"mansh"]
 #print(marks)
print(type(marks))
print(marks.index(10))
print(marks[3])
print(marks.count(10)) #count
print(len(marks)) #length
print(marks[1:3])  #sllicing
marks.append("singh") #add value
print(marks)
marks.insert(3,100) # add value on specific position
print(marks)
marks.remove(10) #remove special value
print(marks)
marks.pop()  # remove last value
print(marks)
marks[5]="manash" #update
print(marks)