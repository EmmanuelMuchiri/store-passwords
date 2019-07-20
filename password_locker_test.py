import unittest  # Importing the unittest module
import pyperclip # Importing the pyperclip module
from password_locker import Credentials  # Importing the Credentials class


class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the Credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials(
            "Linkedin", "EmmanuelMuchiri", "Emmanuel@7127")  # create contact object

    def test_init(self):
        self.assertEqual(self.new_credential.account_name, "Linkedin")
        self.assertEqual(self.new_credential.user_name, "EmmanuelMuchiri")
        self.assertEqual(self.new_credential.password, "Emmanuel@7127")

    def save_account(self):
        '''
        test_save_account test case to test if the crential object is saved into
         the credentials list
        '''
        self.new_credential.save_account()  # saving the new credential
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []

    def test_save_multiple_accounts(self):
            '''
            test_save_multiple_accounts to check if we can save multiple contact
            objects to our Credentials_list
            '''
            self.new_credential.save_account()
            test_credential = Credentials(
            "Linkedin", "EmmanuelMuchiri", "Emmanuel@7127")  # new credential
            test_credential.save_account()
            self.assertEqual(len(Credentials.credentials_list), 2)

    # def test_delete_contact(self):
    #         '''
    #         test_delete_contact to test if we can remove a contact from our contact list
    #         '''
    #         self.new_credential.save_contact()
    #         test_contact = Contact(
    #             "Test", "user", "0712345678", "test@user.com")  # new contact
    #         test_contact.save_contact()

    #         self.new_credential.delete_contact()  # Deleting a contact object
    #         self.assertEqual(len(Contact.contact_list), 1)

#     def test_find_contact_by_number(self):
#         '''
#         test to check if we can find a contact by phone number and display information
#         '''

#         self.new_credential.save_contact()
#         test_contact = Contact("Test", "user", "0711223344",
#                                "test@user.com")  # new contact
#         test_contact.save_contact()

#         found_contact = Contact.find_by_number("0711223344")

#         self.assertEqual(found_contact.email, test_contact.email)

#     def test_contact_exists(self):
#         '''
#         test to check if we can return a Boolean  if we cannot find the contact.
#         '''

#         self.new_credential.save_contact()
#         test_contact = Contact("Test", "user", "0711223344",
#                                "test@user.com")  # new contact
#         test_contact.save_contact()

#         contact_exists = Contact.contact_exist("0711223344")

#         self.assertTrue(contact_exists)

#     def test_display_all_accounts(self):
#         self.assertEqual(Contact.display_contacts(), Contact.contact_list)

#     def test_copy_email(self):
#         '''
#         Test to confirm that we are copying the email address from a found contact
#         '''

#         self.new_credential.save_contact()
#         Contact.copy_email("0712345678")

#         self.assertEqual(self.new_credential.email, pyperclip.paste())

#     def test_generate_Password(self):
#         self.new_credential.save_contact()
#         test_contact = Contact(
#             "Test", "user", "0712345678", "test@user.com")  # new contact
#         test_contact.save_contact()

#         self.new_credential.generate_Password()  # Deleting a contact object
#         self.assertEqual(len(Contact.contact_list), 1)


# if __name__ == '__main__':import unittest  # Importing the unittest module
# import pyperclip
# from contact import Contact  # Importing the contact class


# class TestContact(unittest.TestCase):

#     '''
#     Test class that defines test cases for the contact class behaviours.

#     Args:
#         unittest.TestCase: TestCase class that helps in creating test cases
#     '''

#     def setUp(self):
#         '''
#         Set up method to run before each test cases.
#         '''
#         self.new_credential = Contact(
#             "James", "Muriuki", "0712345678", "qGRn2Y7@£")  # create contact object

#     def test_init(self):
#         self.assertEqual(self.new_credential.first_name, "James")
#         self.assertEqual(self.new_credential.last_name, "Muriuki")
#         self.assertEqual(self.new_credential.phone_number, "0712345678")
#         self.assertEqual(self.new_credential.email, "qGRn2Y7@£")

#     def test_save_contact(self):
#         '''
#         test_save_contact test case to test if the contact object is saved into
#          the contact list
#         '''
#         self.new_credential.save_contact()  # saving the new contact
#         self.assertEqual(len(Contact.contact_list), 1)

#     def tearDown(self):
#             '''
#             tearDown method that does clean up after each test case has run.
#             '''
#             Contact.contact_list = []

#     def test_save_multiple_contact(self):
#             '''
#             test_save_multiple_contact to check if we can save multiple contact
#             objects to our contact_list
#             '''
#             self.new_credential.save_contact()
#             test_contact = Contact(
#                 "Test", "user", "0712345678", "test@user.com")  # new contact
#             test_contact.save_contact()
#             self.assertEqual(len(Contact.contact_list), 2)

#     def test_delete_contact(self):
#             '''
#             test_delete_contact to test if we can remove a contact from our contact list
#             '''
#             self.new_credential.save_contact()
#             test_contact = Contact(
#                 "Test", "user", "0712345678", "test@user.com")  # new contact
#             test_contact.save_contact()

#             self.new_credential.delete_contact()  # Deleting a contact object
#             self.assertEqual(len(Contact.contact_list), 1)

#     def test_find_contact_by_number(self):
#         '''
#         test to check if we can find a contact by phone number and display information
#         '''

#         self.new_credential.save_contact()
#         test_contact = Contact("Test", "user", "0711223344",
#                                "test@user.com")  # new contact
#         test_contact.save_contact()

#         found_contact = Contact.find_by_number("0711223344")

#         self.assertEqual(found_contact.email, test_contact.email)

#     def test_contact_exists(self):
#         '''
#         test to check if we can return a Boolean  if we cannot find the contact.
#         '''

#         self.new_credential.save_contact()
#         test_contact = Contact("Test", "user", "0711223344",
#                                "test@user.com")  # new contact
#         test_contact.save_contact()

#         contact_exists = Contact.contact_exist("0711223344")

#         self.assertTrue(contact_exists)

#     def test_display_all_contacts(self):
#         self.assertEqual(Contact.display_contacts(), Contact.contact_list)

#     def test_copy_email(self):
#         '''
#         Test to confirm that we are copying the email address from a found contact
#         '''

#         self.new_credential.save_contact()
#         Contact.copy_email("0712345678")

#         self.assertEqual(self.new_credential.email, pyperclip.paste())

#     def test_generate_Password(self):
#         self.new_credential.save_contact()
#         test_contact = Contact(
#             "Test", "user", "0712345678", "test@user.com")  # new contact
#         test_contact.save_contact()

#         self.new_credential.generate_Password()  # Deleting a contact object
#         self.assertEqual(len(Contact.contact_list), 2)


if __name__ == '__main__':

    unittest.main()


    unittest.main()
