import time
from EmailLogic import EmailLogic
from selenium.common import NoSuchElementException
from seleniumpagefactory.Pagefactory import PageFactory, ElementNotFoundException
from selenium.webdriver.common.by import By
from CaptchaSolver import CaptchaSolver


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
            'captcha': ('ID', 'register_captcha')
        }
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
            self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div[1]/div/div/div[4]/div[2]/img').screenshot('captcha.png')
            captcha = CaptchaSolver('captcha.png')
            self.captcha.set_text(captcha.get_captcha())

        except (NoSuchElementException, ElementNotFoundException):
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
