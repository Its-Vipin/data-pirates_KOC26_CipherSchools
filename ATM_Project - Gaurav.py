import time as a



User_Pin = 3452
User_Balance = 187432
User_Name = "Mr. Gaurav Siwach"
print("Welcome to your bank account", User_Name, end = "\a\a")

choice = 5

while (True):
    print("\a\a0. Logout and exit")
    print("\a\a1. View account balance")
    print("\a\a2. Deposit Cash")
    print("\a\a3. change PIN")
    print("\a\a4. Return card")
    print("\a\a5. Withdraw Cash")

    choice = int(input("Enter num. to proceed > "))
    print("\a\a")


    if choice == 0:
        print("Exiting....")
        
        print("You have been logged out. Thank You!\a\a")
        break

    elif choice in (1,2,3,4,5,6):
        num_of_tries = 5
        while ("num_of_tries! = 0"):
            Input_Pin = int(input("Enter your 4-digit PIN >"))

            if Input_Pin == User_Pin:
                print("Account auhtorized! \a\a")

                if choice == 1:
                    print("Loading Account Balance....")

                    print("Your current acount balance is Rs. ", User_Balance, end = "\a\a")
                    break
                elif choice == 5:
                    print("Opening Cash Withdrawl....")


                    while(True):
                        Withdraw_Ammount = float(input("Enter Ammount you Withdraw > "))

                        if Withdraw_Ammount>User_Balance:
                            print("Not Withdraw Rs.", Withdraw_Ammount)
                            print("Please enter less Ammount!")
                            continue

                        else:
                            print("Withdraw Rs.", Withdraw_Ammount)
                            confirm = input("Confirm? Y/A >  ")
                            if confirm in ('Y', 'y'):
                                User_Balance -= Withdraw_Ammount
                                print("Ammount  Withdrawn - Rs. " , Withdraw_Ammount)
                                print("Remaining Balance - Rs. " , User_Balance , end = "a\a")
                                break

                            else:
                                print("Cancelling transaction...")

                                print("Transaction Cancelled!\a\a")
                                break

                    break

                elif choice == 2:
                    print("Loading Cash Deposited...")



                    Deposit_Ammount = float("Enter the ammount to Deposit > ")
                    print("Depositing Rs.", Deposit_Ammount)
                    confirm = input("Confirm? Y/A >")
                    if confirm in ('Y', 'y'):
                        User_Balance+=Deposit_Ammount 
                        print("Ammount Deposited - Rs. ", Deposit_Ammount)
                        print("Updated Balance - Rs.", User_Balance, end = "\a\a")
                    else:
                        print("Cancelling Transaction....")

                        print("Transaction Cancelled!\a\a")


                    break



                elif choice == 3:
                    print("Loading PIN Change...")


                    Pin_new = int(input("Entre new PIN > "))
                    print("Changing PIN to ", Pin_new)
                    confirm = input("Confirm? Y/A > ")
                    if confirm in ('Y' , 'y'):
                        User_Pin = Pin_new
                        print("PIN changed successfully! \a\a")
                    else:
                        print("Cancelling PIN change....")

                        print("Process Cancelled!\a\a")

                    break
                else:
                    print("Loading Card Return....")


                    print("Returning ATM Card")
                    confirm = input("Confirm? Y/A > ")
                    if confirm in ('Y' , 'y'):
                        print("Card Return successfully! \a\a")
                    else:
                        print("Cancelling process....")


                        print("Process Cancelled!\a\a")


                    break


        else:
            num_of_tries-=1
            print("PIN incorrect! Number of tries left -" , num_of_tries, end = "\a\a")


    else:
        print("Exiting....")

        print("You logged out. Thank you!\a\a")

        break

else:
        print("Invalid input!")
        print("\a\a0. Enter 0 to Logout and Exit!")
        

    