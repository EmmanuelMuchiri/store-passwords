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

        Credentials.credentials_list.remove(self)
             
    @classmethod
    def search_credential(cls, account_name):
        '''
        Method that takes in a account_name and returns a credential that matches that account_name.
        Args:
            account_name: account_name to search for
        Returns :
            Credential of account name that matches the account_name.
        '''

        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def credential_exist(cls, account_name):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            number: account_name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return True

        return False

    @classmethod
    def display_credential(cls):
        '''
        method that returns the contact list
        '''
        return cls.credentials_list


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
