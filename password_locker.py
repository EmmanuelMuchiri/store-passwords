import pyperclip,random,string

class Users:
    
    users_list=[] # created an empty users list where users will be appended
    
    def __init__(self,u_Name, pswd):
        '''
        Created an instance of a user 
        '''
        self.u_Name = u_Name
        self.pswd = pswd
        
    def save_user(self):
        '''
        save_user method saves users in our class Users inside the users_list
        '''
        Users.users_list.append(self)

class Credentials:

    """
    Class that generates new instances of the credentials for the various accounts.
    """

    credentials_list = []  # Empty credentials list
    @classmethod
    def confirm_User(cls,u_Name, pswd):
        '''Created a gunction to confirm 
        whether the active user is in our users list or not
        '''
        active_user = ''
        for user in Users.users_list:
            if(user.u_Name == u_Name and user.pswd == pswd):
                    active_user == user.u_Name
        return active_user

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
        chars = char=string.ascii_uppercase+string.ascii_lowercase+string.digits
        length = 9
        print('here is  are your password:')
        password = ''.join(random.choice(chars) for _ in range(-1,length))
        print(password)
        return password
    # generate_Password()

    
    