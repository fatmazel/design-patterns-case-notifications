from abc import ABC, abstractmethod

# 1. Soyut Arayüz (Abstract Base Class)
class Notification(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass

# 2. Somut Sınıflar (Concrete Implementations)
class EmailNotification(Notification):
    def send(self, recipient, message):
        print(f"E-posta gönderiliyor: {recipient}")
        print(f"İçerik: {message}")
        print("E-posta başarıyla gönderildi.\n")

class SMSNotification(Notification):
    def send(self, recipient, message):
        if len(message) > 160:
            message = message[:157] + "..."
        print(f"SMS gönderiliyor: {recipient}")
        print(f"İçerik: {message}")
        print("SMS başarıyla gönderildi.\n")

class PushNotification(Notification):
    def send(self, recipient, message):
        print(f"Push bildirimi gönderiliyor: {recipient}")
        print(f"İçerik: {message}")
        print("Push bildirimi gönderildi.\n")

# 3. Factory ve Registry Yapısı
class NotificationFactory:
    _registry = {}

    @classmethod
    def register_notification(cls, type_name, notification_class):
        cls._registry[type_name] = notification_class

    @classmethod
    def create_notification(cls, type_name):
        notifier_class = cls._registry.get(type_name)
        if not notifier_class:
            raise ValueError(f"Bilinmeyen bildirim tipi: {type_name}")
        return notifier_class()

# 4. Sisteme Türlerin Kaydedilmesi (Initialization)
NotificationFactory.register_notification("email", EmailNotification)
NotificationFactory.register_notification("sms", SMSNotification)
NotificationFactory.register_notification("push", PushNotification)

# 5. Client Code (İstemci Kodu) - Artık if-else yok!
if __name__ == "__main__":
    try:
        # Factory üzerinden nesne üretimi
        email_notifier = NotificationFactory.create_notification("email")
        email_notifier.send("fatmazehra@example.com", "Ödev teslimine az kaldı!")

        sms_notifier = NotificationFactory.create_notification("sms")
        sms_notifier.send("+90555...", "Bu bir test mesajıdır.")
        
    except ValueError as e:
        print(f"Hata: {e}")