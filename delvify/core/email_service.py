from abc import ABC, abstractmethod

from delvify.schemas import Email

from .logger import LoggerMixin


class EmailService(ABC):
    @abstractmethod
    def send_email(self, email: Email):
        pass


class StdoutEmailService(EmailService, LoggerMixin):
    def send_email(self, email: Email):
        self.log.info(f"Email was sent! Details: {str(email)}")
