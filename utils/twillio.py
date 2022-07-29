import os
import time

from dotenv import load_dotenv
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure


class SmsFromTwillio:
    def __init__(self, dotenv=load_dotenv()):
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(self.account_sid, self.auth_token)

    def read_sms(self, message_sent_after, timeout_ms=20000):
        start = time.time()
        while True:
            messages = self.client.messages.list(to=os.environ['phone'],
                                                 date_sent_after=message_sent_after,
                                                 limit=1)
            if len(messages) == 1:
                return messages[0].body
            else:
                elapsed_ms = (time.time() - start) * 1000
                remaining = timeout_ms - elapsed_ms
                if remaining <= 0:
                    raise AssertionError('Не удалось получить последнее сообщение!')
