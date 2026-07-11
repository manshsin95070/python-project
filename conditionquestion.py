# question no.1
""" Username =input("enter the user id :")
Password =input("enter the password :")
if Username=="mansh" and Password==123:

    print("the succefully login")
else:
    print("login denied") """


    # question no. 2
balence = int(input("enter your balence:"))
amount = int(input("enter your amount:"))
if amount <= balence:
        print("transaction succesfully")
        balence=balence - amount
        print("remaining ballence is:",balence)
else:
        print("Insufficient Balance")