
def Bank_App():
    email_dictionary = {"Saoban@gmail.com":['0000',100]}
    print('press 1 to Create an Account')
    print('press 2 to make Transactions')
    Input = int(input('What did you want to do? : \t'))

    if int(Input) == 1:
        
        def Create_Account():
            while True:
                email = input('Enter a valid email: \t')
                if '@' in email:
                    indx = email.index('@')
                    extension = email[indx:]
                    if extension != '@gmail.com':
                        print("Invalid email, pls input a valid email")
                        continue
                else:
                    print('Invalid email, pls enter a valid email')
                    continue
                if email_dictionary.get(email):
                    print("There is a user with this email, Pls enter another email")
                else:
                    password = input("Enter a your Password here: \t")
                    email_dictionary[email] = []
                    email_dictionary[email].append(password)
                    email_dictionary[email].append(100)
                    print("Account Created successfully")
                    break
        Create_Account()

        
    elif int(Input) == 2:
        def Transactions():
            Password = input("Pls input your Password: \t")
            
            for Value in email_dictionary.values():
                if (Password in Value):
                    print("Press 1 to Check Balance")
                    print("Press 2 to Deposit")
                    print("Press 3 to Withdraw")
                    print("Press 4 to Transfer")
                    Next = int(input("What next did you want to do: \t"))

                    if Next == 1:
                        def Check_Balance():
                            for Value in email_dictionary.values():
                                print(Value[1])
                        
                        Check_Balance()

                    elif Next == 2:
                        def Deposit():
                            Amount = int(input("Pls Input Amount You want to deposit: \t $"))
                            for Value in email_dictionary.values():
                                Add = (Value[1] + Amount)
                                #Value[1] == Add 
                                #email_dictionary.update(str(Value[1]))
                                print(f'RECEIPT : Your balance now is ${Add}.')

                        Deposit()

                    elif Next == 3:
                        def Withdraw():
                            Amount = int(input("How much do you want to withdraw: \t $"))
                            for Value in email_dictionary.values():
                                if Value[1] < Amount:
                                    print("You do not have sufficient Amount, Pls deposit into the account")
                                    Deposit()
                                elif Value[1] > Amount:
                                    Subtract = (Value[1] - Amount)
                                    print(f'Your new Account Balance is ${Subtract} ')
                        
                        Withdraw()
                    
                    elif Next == 4:
                        def Transfer():
                            Email_transferred_to = input('Which Email do you want to taransfer to: \t')

                            while True:

                                if Email_transferred_to not in email_dictionary.keys():

                                    print('This email does not exist')
                                    Transfer()
                                    
                            
                                else:

                                    Amount = int(input("How much do you want to transfer: \t"))
                                    for Value in email_dictionary.values():
                                        if Value[1] < Amount :
                                            print("Insufficient Account Balance")
                                        else:
                                            Remove = (Value[1] - Amount)
                                            
                                            #email_dictionary[Email_transferred_to(Value[1])] = Value[1] + Amount
                                            print("Transfer Successful")
                                            print(f'RECEIPT: Your remaining Account Balance is {Remove}')
                                break

                                
                            

                        Transfer()
                            


                else:
                    print('This password is not Authorized')
                    #Create_Account()
                
                
        
               
                        
                        
                


        
        
        Transactions()
        




Bank_App()

        