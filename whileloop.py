#question1
num=1
while num<=10:
    print(num)
    num+=1
#question no.2

attempt=1
while attempt<=3:
    pin=(int(input("enter your atm pin :")))
    if pin==12345:
        print("login successfully")
        break
    else:
        print("wrong pin  try again")
    attempt+=1
if attempt>3:    
        print("system blocked")
    