#!/usr/bin/env python3.6
import pyperclip
import random,string  # Importing the pyperclip module
from password_locker import Users,Credentials  # Importing the Credentials class
######Create functions to implement what the behaviours we have created####
def create_user(user_name,password):
    '''
    Function to add a new user to our users_list
    '''
    new_User=Users(user_name,password)
    
    return new_User


def create_credential(account_Name, user_Name, user_Password):
    """
    Function to create a new contact
    """
    new_credential = Credentials(
        account_Name, user_Name, user_Password)  # create contact object
    return new_credential

###We create a function called create_contact(), that takes in four arguments###

#####Save Contacts #####


def save_credentials(password_locker):
    """
    Function to save contact
    """
    password_locker.save_account()

### we create save contact function that takes in a contact object and then calls the save_contact method to save the contact. ####

#####Delete Contact


def del_credential(password_locker):
    """
    Function to delete a contact
    """
    password_locker.delete_account()

### We create a del_contact function that takes in a contact object and then calls the delete_contact() method on the contact object deleting it from the contact list####

##Fininding a contact ##


def find_credential(account_Name):
    """
    Function that finds a contact by number and returns the contact
    """
    return Credentials.search_credential(account_Name)

### We create a func that takes in a number and calls the Contact class method find_by_number that returns the contact. ###

### Check if a contact exists ###


def check_existing_credendtials(account_Name):
    """
    Function that check if a contact exists with that number and return a Boolean
    """
    return Credentials.credential_exist(account_Name)

### The function check_existing_contacts takes in a number as an argument and calls the class method contact_exist which returns a boolean.###

## Displaying all contacts ##


def display_credentials():
    """
    Func that rteturns all the saved contacts
    """
    return Credentials.display_credentials()
## Copy Password ##
# @classmethod


def copy_password(account_Name):
    """
    A funct that copies the email using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    Credentials.copy_password(account_Name)


def generate_Password():
        '''
        generates a 9 digit randomn password
        '''
        auto_Generic_Password=Credentials.generate_Password()
        return auto_Generic_Password


def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}.Welcome To PassWord Locker Manager")
    print('\n')
    print("what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - Create a new credential, dc - Display Credential(s), fc - Find a credential,ex - Exit the application, gp- Generate A randomn password, del- Delete credential,cp-Copy Password")
                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Credential")
                            print("-"*10)

                            print("Account name ....")
                            account_Name = input().capitalize()

                            print("Your Account name ...e.g LinkedIn username")
                            user_Name = input()
                            while True:
                                print(" For Type/Paste Password type TP ; For generate_Password type gp")
                                password_Choice = input("Enter").lower()
                                if password_Choice == 'tp':
                                    user_Password = input("Enter Password")
                                    break
                                elif password_Choice == 'gp':
                                    user_Password = generate_Password()
                                    break
                                elif password_Choice != 'tp' or 'gp':
                                    print("Invalid password please try again")
                                    break
                                else:
                                    print("Invalid password please try again")
                            save_credentials(create_credential(account_Name,user_Name,user_Password))
                            print('\n')
                            print(f"New Credential : {account_Name} UserName: {user_Name}  created")
                            print('\n')

                    elif short_code == 'dc':

                            if display_credentials():
                                    print("Your Account(s) Credential(S) are as follows :")
                                    print('\n')
                                    for password_locker in display_credentials():
                                            print(f"Account Name :{password_locker.account_name} ; UserName: {password_locker.user_name} ; PassWord :{password_locker.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print(
                                        "Oops !!! You dont seem to have any Credentials saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the Account Name you want to search for")
                            search_name = input().capitalize()
                            if check_existing_credendtials(search_name):
                                    search_credential = find_credential(
                                        search_name)
                                    print(f"Account Name : {search_credential.account_name}")
                                    print('-' * 100)
                                    print(f"Account Name: {search_credential.account_name} PassWord :{search_credential.password}")
                            else:
                                    print("That Credential does not exist")
                                    print('\n')
					
                    elif short_code == 'cp':

                        	print("Enter the number of the contact you want to generate password for")
                        	search_name = input().capitalize()
                        	if check_existing_credendtials(search_name):
                            		search_credential = find_credential(search_name)
                            		print(f"{search_credential.account_name}")
                            		print("_"*20)
                            		user_Password=copy_password(search_name)
                            		print('\n')
                            		print(f"New Credential : {account_Name} UserName: {user_Name}  You can proceed and paste to your account")
                                             
                    elif short_code == "del":
                         print("Enter the number of the contact you want to delete")
                         search_name = input().capitalize()
                         if check_existing_credendtials(search_name):
                             search_credential = find_credential(search_name)
                             print(
                                 f"{search_credential.account_name}")
                             print("_"*20)
                             password_locker.delete_account()
                             print('\n')
                             print(f"New Credential : {account_Name} UserName: {user_Name}  successfully deleted!!!")
                             print('\n')
                         else:
                                    print("That Credential does not exist")
                                     
                    elif short_code == 'gp':
                    		user_Password = generate_Password()
                    else:
                            print("Invalid Response Kindly use use the short codes provided in the menu")
                            break


if __name__ == '__main__':

    main()


