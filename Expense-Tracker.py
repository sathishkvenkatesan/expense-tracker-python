#Expense Tracker
#created by Sathish Kumar

balance = 0

while True:
    d = int(input("1.Add income \n2.Add Expense \n3.View Balance \n4.Exit\n"))

    if d == 1:
        income = int(input("Add income: "))
        balance = balance + income
        print("Balance is:", balance)
    
    elif d == 2:
        expense = int(input("Add Expense: "))

        if expense > balance:
            print("Insufficient Balance")
        else:
             balance = balance - expense
             print("Balance is:", balance)
       
    
    elif d == 3:
        print("Balance is:", balance)
    
    elif d == 4:
        print("Exit Program")
        break

    else:
        print("Invalid Value")