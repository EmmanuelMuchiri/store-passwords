import pyperclip,random

class Credentials:

    """
    Class that generates new instances of the credentials for the various accounts.
    """

    credentials_list = []  # Empty credentials list

    def __init__(self,account_name,user_name, password):
        self.account_name = account_name
        self.user_name = user_name
        self.password = password

    def save_account(self):
        '''
        save_account method saves accounts credentials credentials_list
        '''

        Credentials.credentials_list.append(self)

    def delete_account(self):
        '''
        delete_account method deletes a saved account from the credentials_list
        '''

        Contact.contact_list.remove(self)
    
    # def delete_contacts():
    #     '''
    #     delete_contact method deletes a saved contact from the contact_list
    #     '''

    #     Contact.contact_list.remove()
        
    @classmethod
    def find_by_number(cls, number):
        '''
        Method that takes in a number and returns a contact that matches that number.
        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact

    @classmethod
    def contact_exist(cls, number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                    return True

        return False

    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list


# ......................
    @classmethod
    def copy_email(cls,number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)
 
    @classmethod
    def delete_contacts(cls):
        
        '''
        method that returns the contact list
        '''
        return cls.contact_list
    # @classmethod
    def generate_Password():
        print('''
        Password Generator
        ==================
        ''')

        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

        length = 9

        print('\nhere are your passwords:')
        password = ''
        for c in range(0, length):
                password += random.choice(chars)
            print(password)
            pass

            generate_Password()
