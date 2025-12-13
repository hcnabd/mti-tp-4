# `UserNotification` directly creates an instance of `EmailService`, creating **tight coupling**.  
# - Hard to replace `EmailService` with another channel (SMS, Push).  
# - Hard to test `UserNotification` independently.  
# - Violates the **Dependency Inversion Principle**: high-level module depends on low-level concrete class.

# ------------------------------------------------------------

from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message): pass

class EmailService(NotificationService):
    def send(self, message):
        print(f"Sending email: {message}")

class SMSService(NotificationService):
    def send(self, message):
        print(f"Sending SMS: {message}")

class PushService(NotificationService):
    def send(self, message):
        print(f"Sending push notification: {message}")

class UserNotification:
    def __init__(self, service: NotificationService):
        self.service = service

    def notify(self, user, message):
        self.service.send(message)

email_notifier = UserNotification(EmailService())
email_notifier.notify("Alice", "Welcome!")

sms_notifier = UserNotification(SMSService())
sms_notifier.notify("Bob", "Your code is ready!")

push_notifier = UserNotification(PushService())
push_notifier.notify("Carol", "You have a new message!")