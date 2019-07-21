## Built By [Emmanuel Muchiri](https://github.com/emmanuelmuchiri/)

## Description
Password Locker is a python CLI (command line interface) application that manages login credentials for various accounts that require passwords i.e. usernames and passwords.
Store-Passwords also generates randomn fully-encrypted alphanumeric mixed with special characters password(s) that the user can copy and paste into their accounts upon signup.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like:
* To create an account with his or her details i.e log in and password
* Store my existing login credentials
* Generate a password for a new credential/account
* Copy my credentials to the clipboard

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Abbreviations for navigation | **On The terminal: $./app.py** | Welcome, choose an option: ca-Create Account and li-Log In|
| Display prompt for creating an account | **Enter: ca** | Enter your prefered user name and password |
| Display prompting user to login in | **Enter: li** | Enter your username and password |
| Abbreviations for navigation | **Checked In** | Choose an option: cc - Create Credential, dc - Display Credentials, cp- Copy password, ex - exit, gp- generate password ,delete credential |
| Display prompting user to create a credential | **Enter: cc** | Enter the Account name, your username and password |
| Display a list of credentials | **Enter: dc** | Displays all saved credentials |
| Display prompting for which credential to copy password | **Enter: cp** | Enter the Account name of the credential you wish to copy. |
| Generate Password | **Enter: gp** | Here is your password : EVK£mm6bP |
| search by Account Name the credential that you wish to delete | **Enter: del** | Account Deleted Successfully!!!|
| Exit application | **Enter: ex** | Exit the Application |

## SetUp / Installation Requirements

### You Need to Install the Following in order for the application to work
* python3.6
* pip
* pyperclip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/emmanuel/store-passwords/
        $ cd store-passwords

## Running the Application
* To run the application, in your terminal:

        $ chmod +x app.py
        $ ./app.py
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 password_locker_test.py
        
## Technologies Used
* Python3.6

## License
MIT &copy;2019 [Emmanuel Muchiri](https://github.com/emmanuelmuchiri/)

 Emmanuel Muchiri