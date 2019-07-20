#!/usr/bin/env python3.6
import pyperclip  # Importing the pyperclip module
from password_locker import Credentials  # Importing the Credentials class
######Create functions to implement what the behaviours we have created####

def create_credential(account_Name,user_Name,user_Password):
    """
    Function to create a new contact
    """
    new_credential = Credentials(account_Name,user_Name,user_Password)  # create contact object
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
    password_locker.delete_contact()

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
@classmethod
def copy_password(cls, account_Name):
    """
    A funct that copies the email using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    credential_found = Credentials.search_credential(account_Name)
    pyperclip.copy(credential_found.user_Password)
    
# @classmethod
def gen_password(password_locker):
    """
    Function to delete a contact
    """
    Credentials.generate_Password()


def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}.Welcome To PassWord Locker Manager")
    print('\n')
    print("what would you like to do?")
    print('\n')
   
    while True:
                    print('''
                          Use these short codes : 
                          cc - Create a new credential,
                          dc - Display Credential(s), 
                          fc - Find a credential, 
                          ex - Exit the application,
                          del- Delete credential, 
                          pwd- Generate password
                          ''')

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Credential")
                            print("-"*10)

                            print("Account name ....")
                            account_Name = input().capitalize()

                            print("Your Account name ...e.g LinkedIn username")
                            user_Name = input()

                            print("Enter Password ...")
                            user_Password = input()

                            # create and save new contact.
                            save_credentials(create_credential(account_Name,user_Name,user_Password))
                            print('\n')
                            print(f"New Credential : {account_Name} UserName: {user_Name}  created")
                            print('\n')

#                     elif short_code == 'dc':

#                             if display_contacts():
#                                     print("Here is a list of all your contacts")
#                                     print('\n')

#                                     for contact in display_contacts():
#                                             print(
#                                                 f"{contact.first_name} {contact.last_name} {e_address} {contact.phone_number}")

#                                     print('\n')
#                             else:
#                                     print('\n')
#                                     print(
#                                         "You dont seem to have any contacts saved yet")
#                                     print('\n')

#                     elif short_code == 'fc':

#                             print("Enter the number you want to search for")

#                             search_number = input()
#                             if check_existing_contacts(search_number):
#                                     search_contact = find_contact(
#                                         search_number)
#                                     print(
#                                         f"{search_contact.first_name} {search_contact.last_name}")
#                                     print('-' * 20)

#                                     print(
#                                         f"Phone number.......{search_contact.phone_number}")
#                                     print(
#                                         f"Email address.......{search_contact.email}")
#                             else:
#                                     print("That contact does not exist")

#                     elif short_code == "del":
#                          print("Enter the number of the contact you want to delete")
#                          search_number = input()
#                          if check_existing_contacts(search_number):
#                              search_contact = find_contact(search_number)
#                              print(
#                                  f"{search_contact.first_name} {search_contact.last_name}")
#                              print("_"*20)
#                              contact.delete_contact()
#                         #  if contact.delete_contact():
#                              print('\n')
#                              print(
#                                  f'{f_name} {e_address} Successfully deleted!!')
#                              print('\n')

#                     elif short_code == 'pwd':
#                          print("Enter the number of the contact you want to delete")
#                          search_number = input()
#                          if check_existing_contacts(search_number):
#                              search_contact = find_contact(search_number)
#                              print(
#                                  f"{search_contact.first_name} {search_contact.last_name}")
#                              print("_"*20)
#                              contact.generate_Password()
#                     #  if contact.delete_contact():
#                              print('\n')
#                              print(
#                                  f'{f_name} {e_address} password Successfully generated!!')
#                              print('\n')
                             
#                     elif short_code == "ex":
#                                 print("Bye .......")
#                                 break
#                     else:
#                             print(
#                                 "I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
