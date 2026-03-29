# class LoginPage:

#     def __init__(self, page): # here page is from conftest.py which is a fixture and it will be executed before the test case and after the test case it will close the browser 
#         self.page = page    # it will assign the page object to the instance variable self.page, so that we can use it in other methods of this class

#         #locators of login page

#        # Locators
#         self.username_input = "#username"
#         self.password_input = "#password"
#         self.login_button = "#submit"
#         self.success_message = "text=Logged In Successfully"
#         self.errormsg="#error"


#         #Add the user actions

#     def enter_username(self, username):
#         self.page.fill(self.username_input, username)

#     def enter_password(self, password):
#         self.page.fill(self.password_input, password)

#     def click_login(self):
#         self.page.click(self.login_button)


#         #now create re usable logn 

#     def login(self, username, password):
#         self.enter_username(username)
#         self.enter_password(password)
#         self.click_login()


# #this method will check if the login is successful or not by checking the visibility of the success message
#     def is_login_successful(self):
#         return self.page.locator(self.success_message).is_visible() #this will return true if the success message is visible and false if it is not visible
    
#     def error_message(self):
#         return self.page.locator(self.errormsg).inner_text() #this will return the error message text which we can use in our test case to assert the error message
    





#----------------------After implementing step -7 clean framework and utilities with base_page.py file----------------------

from pages.base_page import BasePage

# LoginPage gets all methods from BasePage (inheritance)
class LoginPage(BasePage): #it will inherit the methods of the BasePage class which we have created in the pages/base_page.py file, so that we can use those methods in this class without writing the code again


    def __init__(self, page):

        # Calls parent class constructor and Gives access to self.page
        super().__init__(page)   #it will call the constructor of the BasePage class and pass the page object to it, so that we can use the methods of the BasePage class in this class

        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "#submit"
        self.error_message = "#error"
        self.success_message = "text=Logged In Successfully"

    def login(self, username, password):
        self.fill(self.username_input, username) #self.fill from the BasePage class which will fill the username input field with the value of username and self.password_input is the locator of the password input field which we have defined in the constructor of this class, so it will
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def get_error_message(self):
        return self.get_text(self.error_message)

    def is_login_successful(self):
         return self.page.locator("text=Logged In Successfully").is_visible()


