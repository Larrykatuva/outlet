import threading
from django.core.mail import EmailMessage


class EmailThreading(threading.Thread):

    def __init__(self, email: str):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=False)


class Email:

    @staticmethod
    def send(email_subject: str, email_body: str, send_to: str) -> None:
        email = EmailMessage(
            email_subject,
            email_body,
            'noreply@gmail.com',
            send_to,
        )
        EmailThreading(email).start()
