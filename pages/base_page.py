class BasePage:  #this is the base page class which will contain all the common methods that we can use in all the page classes, so that we don't have to write the same code again and again in each page class, we can just inherit the BasePage class in each page class and use the methods of the BasePage class in those page classes without writing the code again

    def __init__(self, page): #here page is came from 
        self.page = page

    def click(self, locator):
        self.page.click(locator)

    def fill(self, locator, value):
        self.page.fill(locator, value)

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()