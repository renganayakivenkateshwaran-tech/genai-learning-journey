from abc import ABC,abstractmethod
class Notification(ABC):
    def __init__(self,type,recipient):
        self.type = type
        self.recipient = recipient
    @abstractmethod
    def send(self,message):
        pass
    def show_type(self):
        print(f"Notification type: {self.type}")
class EmailNotification(Notification):
    def send(self,message):
        print(f"Sending {message} to {self.recipient}")
class SMSNotification(Notification):
    def send(self,message):
        print(f"Sending {message} to {self.recipient}")
class PushNotification(Notification):
    def send(self,message):
        print(f"Sending {message} to {self.recipient}")
def send_notification(notification,message):
    notification.send(message)
email = EmailNotification("Email","achu2008@gamil.com")
sms = SMSNotification("SMS","+91XXXXXXXXXX")
email.show_type()
send_notification(email,"Your order has been shipped")
sms.show_type()
send_notification(sms,"Your order has been shipped")
