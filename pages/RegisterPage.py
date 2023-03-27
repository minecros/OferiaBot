import time
from EmailLogic import EmailLogic
from selenium.common import NoSuchElementException
from seleniumpagefactory.Pagefactory import PageFactory, ElementNotFoundException
from selenium.webdriver.common.by import By


class RegisterPage(PageFactory):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

        self.locators = {
            'inputEmail': ('ID', 'register_email'),
            'inputPassword': ('ID', 'register_pass'),
            'inputReplyPassword': ('ID', 'register_passRepeat'),
            'checkboxAllPermission': ('CLASS_NAME', 'acceptAllAgreements'),
            'buttonRegister': ('CLASS_NAME', 'btn-submit'),
            'captacha': ('ID', 'register_captcha')
        }
        self.captacha_id = 'register_captcha'
        self.inbox = EmailLogic()
        self.email_address = self.inbox.email_address
        self.password = ''

    def register_page(self):
        self.driver.get('https://www.oferia.pl/rejestracja')

    def make_user(self, password='Password123'):
        self.password = password
        self.inputEmail.set_text(self.email_address)
        self.inputPassword.set_text(password)
        self.inputReplyPassword.set_text(password)
        self.checkboxAllPermission.click_button()

        try:
            self.timeout = 0
            self.driver.find_element(By.ID, self.captacha_id)
            self.captacha.click_button()
            time.sleep(5)
        except (NoSuchElementException, ElementNotFoundException):
            self.timeout = 10
            pass

        self.buttonRegister.click_button()

    def activate_account(self):
        self.inbox.get_emails()
        activation_url = self.inbox.get_activation_url()
        self.driver.get(activation_url)
        file = open('users.txt', 'a')
        file.write(self.email_address + ':' + self.password + '\n')
        file.close()

    def get_email_password(self):
        return [self.email_address, self.password]
