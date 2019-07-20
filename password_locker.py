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
    def display_credentials(cls):
        '''
        method that returns the contact list
        '''
        return cls.credentials_list


# ......................
    @classmethod
    def copy_password(cls,account_name):
        credential_found = Credentials.search_credential(account_name)
        pyperclip.copy(credential_found.password)
 
    # @classmethod
    def generate_Password():
        '''
        Password Generator
        ==================
        it generates a random 9-digit alphanumeric password with characters as well.
        Example :EVK£mm6bP
        '''
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
        length = 9
        print('here is  are your password:')
        password = ''.join(random.choice(chars) for _ in range(length))
        print(password)            
        return password
    generate_Password()
