# question no.1
""" Username =input("enter the user id :")
Password =input("enter the password :")
if Username=="mansh" and Password==123:

    print("the succefully login")
else:
    print("login denied") """


# question no. 2
"""balance = int(input("enter your balance:"))
amount = int(input("enter your amount:"))
if amount <= balance:
        print("transaction succesfully")
        balance=balance - amount
        print("remaining balance is:",balance)
else:
        print("Insufficient Balance") """

# question no.3

pin = int(input("enter your pin:"))
if pin == 1234 :
    print("login successfully")
    balance = int(input("enter your balance:"))
    if balance < 5000:
        print("low balance:",balance)
    else:
        print("your balance is:",balance)
else:
   print("incorrect pin")
