
class NotificationManager:
    def send_notification(self, notification_type, message, recipient):
        # Tip kontrolü için if-else zincirleri (İstenen sorunlu yapı)
        if notification_type == "email":
            print(f"E-posta gönderiliyor: {recipient}")
            print(f"İçerik: {message}")
            print("E-posta başarıyla gönderildi.\n")
        
        elif notification_type == "sms":
            # SMS için karakter sınırı kontrolü gibi ek mantıklar buraya gömülmüş
            if len(message) > 160:
                message = message[:157] + "..."
            print(f"SMS gönderiliyor: {recipient}")
            print(f"İçerik: {message}")
            print("SMS başarıyla gönderildi.\n")
            
        elif notification_type == "push":
            print(f"Push bildirimi gönderiliyor: {recipient}")
            print(f"İçerik: {message}")
            print("Push bildirimi gönderildi.\n")
            
        else:
            print("Hata: Bilinmeyen bildirim tipi!")

# Test Kullanımı
if __name__ == "__main__":
    manager = NotificationManager()
    manager.send_notification("email", "Ödev teslimine az kaldı!", "fatmazehra@example.com")
    manager.send_notification("sms", "Bu bir test mesajıdır ve oldukça uzun bir mesaj olduğu için kırpılması gerekebilir.", "+90555...")