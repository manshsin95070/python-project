student={"name":"manash",
         "age":23,
         "subject":[23,89,90,50]
         }
print(student)
print(type(student))

print(len(student))

print(student["age"])

student["age"]=25
print(student)


student.pop("age")
print(student)

print(list(student.keys()))

print(list(student.items()))

print(list(student.values()))