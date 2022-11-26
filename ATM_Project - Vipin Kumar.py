# Name : Vipin Kumar
# Section : KOC26
# Roll no. : 71


# -------------------------------


# 4-Digit PIN : 1234

import time as t
userName="Mr.John"
userBalance=10000.0
userPin=1234
while True:
    

    print("Welcome to Your Bank Account", userName)
    t.sleep(1.5)
    def balance():
        if userBalance<5000:
            print("Your Current Balance is Rs.", userBalance, "(Low Balance)\n")
        else:
            print("Your Current Balance is Rs.", userBalance,"\n")
    balance()
    t.sleep(1.5)
    print("*          ATM Services           *")
    print("\t1. Withdraw Cash")
    print("\t2. Deposit Cash")
    print("\t3. Change PIN")
    print("\t4. Logout and Exit")

    userInput=int(input("Enter number to proceed: "))

    if userInput==4:
        
        t.sleep(1.5)
        print("You have been logged out. Thank you!\n")
        t.sleep(1.5)
        print("Exiting...")
        t.sleep(1.5)
        break
    
    
    elif userInput==1:
        tries=3
        while tries!=0:
            inputPin=int(input("\nPlease Enter Your 4-Digit PIN: "))
            if inputPin==userPin:
                print("\nOpening Cash Withdrawal...")
                t.sleep(1.5)
                amtWithdraw=float(input("\nEnter the amount you wish to withdraw: "))
                if amtWithdraw>userBalance:
                    print("Can't withdraw", amtWithdraw)
                    print("Enter a lower amount\n")
                    continue
                else:
                    print("Withdrawing Rs.", amtWithdraw,"\n")
                    confirm=input("Confirm? Y/N: ")
                    if confirm in ('Y','y'):
                        print("Cash is withdrawing...")
                        t.sleep(1.5)
                        userBalance-=amtWithdraw
                        print("\nAmount withdrawn - Rs.", amtWithdraw)
                        print("Remaining Balance - Rs.", userBalance,"\n       Have a Nice Day!       \n")
                        print("-------------------------------------------\n")
                    else:
                        print("Canceling Transaction...\n\n-------------------------------------------\n")
                        t.sleep(1.5)
                break
                                    
            else:
                tries-=1
                print("PIN incorrect! Number of tries left -", tries,"\n") 
                print("-------------------------------------------\n")           
                continue
    
    elif userInput==2:
        print("\nLoading Cash Depositing...")
        t.sleep(1.5)

        amtDeposit=float(input("\nEnter the amount you wish to deposit: "))
        confirm=input("Confirm? Y/N: ")
        if confirm in ('Y','y'):
            print("\nCash is depositing...")
            t.sleep(1.5)
            userBalance+=amtDeposit
            print("\nAmount Deposited - Rs.",amtDeposit)
            print("Updated Balance - Rs.", userBalance,"\n       Have a Nice Day!       \n")
            print("-------------------------------------------\n")
        else:
            print("Canceling Transaction...\n\n-------------------------------------------\n")
            t.sleep(1.5)   
        continue
    elif userInput==3:
        tries=3
        while tries!=0:
            inputPin=int(input("\nPlease Enter Your 4-Digit PIN: "))
            if inputPin==userPin:
                print("\nLoading PIN Change...")
                t.sleep(1.5)

                newPin=int(input("Enter your new PIN: "))
                print("\nChanging PIN to", newPin)
                confirm=input("Confirm? Y/N: ")
                if confirm in ('Y','y'):
                    userPin=newPin
                    print("PIN changed successfully!\n")
                    print("-------------------------------------------\n")
                else:
                    print("Cancelling PIN change...")
                    t.sleep(1)
                    print("Process Cancelled\n")
                    print("-------------------------------------------\n") 
                break 
            else:
                tries-=1
                print("PIN incorrect! Number of tries left -", tries,"\n") 
                print("-------------------------------------------\n")           
                continue          
    else:
        t.sleep(1.5)
        print("Invalid Number, Try Again!\n")
        print("-------------------------------------------\n")
        t.sleep(1.5)
        continue
        
            