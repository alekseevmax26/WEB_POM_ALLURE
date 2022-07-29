import email
import imaplib
import os
import time

import bs4 as bs4


class imap:

    def __init__(self):
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')

    def get_link_for_mail(self):
        time.sleep(10)
        self.mail.login(os.environ['mail'], os.environ['password_google'])
        self.mail.list()
        self.mail.select("inbox")

        result, data = self.mail.search(None, "ALL")

        ids = data[0]
        id_list = ids.split()
        latest_email_id = id_list[-1]

        result, data = self.mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')

        email_message = email.message_from_string(raw_email_string)
        if email_message.is_multipart():
            for payload in email_message.get_payload():
                body = payload.get_payload(decode=True).decode('utf-8')

        else:
            body = email_message.get_payload(decode=True).decode('utf-8')

        soup = bs4.BeautifulSoup(body, 'html.parser')
        link = soup.find('a', text='VERIFY EMAIL')['href']
        return link
