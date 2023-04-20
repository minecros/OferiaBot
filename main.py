from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=options)
driver.highlight = True
driver.mobile_test = False

oferia = RegisterPage(driver)
oferia.register_page()
oferia.make_user()
oferia.activate_account()
email_password = oferia.get_email_password()

oferia = LoginPage(driver)
oferia.login_page()
oferia.login_user(email_password=email_password)

