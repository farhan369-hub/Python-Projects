# Base class
class Notification:
    def send_message(self):
        print("Sending a general notification")


# Subclass 1
class EmailNotification(Notification):
    def send_message(self):
        print("Sending notification via Email...")
        print("Email sent successfully!\n")


# Subclass 2
class SMSNotification(Notification):
    def send_message(self):
        print("Sending notification via SMS...")
        print("SMS delivered successfully!\n")


# Subclass 3
class AppNotification(Notification):
    def send_message(self):
        print("Sending notification via Mobile App...")
        print("Push notification sent!\n")


# Creating objects
notifications = [
    EmailNotification(),
    SMSNotification(),
    AppNotification()
]

# Demonstrating polymorphism
for notification in notifications:
    notification.send_message()