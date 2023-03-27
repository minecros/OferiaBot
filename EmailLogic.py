import re
from TempMail import TempMail
from bs4 import BeautifulSoup


class EmailLogic:

    def __init__(self):
        self.activation_url = ''
        self.inbox = TempMail.generateInbox()
        self.email_address = self.inbox.address
        self.token = self.inbox.token

    def get_emails(self):
        while True:
            emails = TempMail.getEmails(self.inbox)
            if emails:
                only_html = emails[0].html
                soup = BeautifulSoup(only_html, 'html.parser')
                activation_url = soup.find(href=re.compile('rejestracja'))['href']
                self.activation_url = activation_url
                break

    def get_activation_url(self):
        return self.activation_url
