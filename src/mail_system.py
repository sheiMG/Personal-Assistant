from smtplib import *
from dotenv import load_dotenv
import os

load_dotenv()


class MailSystem:
    def __init__(self, subject, body):
        self.email = os.environ['MAIL_SEND']
        self.address = os.environ['MAIL_ADDR']
        self.password = os.environ['MAIL_PASS']
        self.subject = subject
        self.body = body

    def send_email(self):
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(from_addr=self.email,
                                to_addrs=self.address,
                                msg=f"Subject:{self.subject}\n\n{self.body}".encode('utf-8')
                                )



