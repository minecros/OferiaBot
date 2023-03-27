import time
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from seleniumpagefactory.Pagefactory import PageFactory, ElementNotFoundException


class LoginPage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

        self.locators = {
            'inputEmail': ('ID', 'login_login'),
            'inputPassword': ('ID', 'login_password'),
            'captacha': ('ID', 'login_captcha'),
            'buttonLogin': ('CLASS_NAME', 'btn-submit')
        }
        self.captacha_id = 'login_captcha'
        self.login_page_url = 'https://www.oferia.pl/moja_oferia'

    def login_page(self):
        self.driver.get(self.login_page_url)

    def login_user(self, email_password):
        self.inputEmail.set_text(email_password[0])
        self.inputPassword.set_text(email_password[1])

        try:
            self.timeout = 0
            self.driver.find_element(By.ID, self.captacha_id)
            self.captacha.click_button()
            time.sleep(5)
        except (NoSuchElementException, ElementNotFoundException):
            self.timeout = 10
            pass

        self.buttonLogin.click_button()
