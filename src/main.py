from abc import ABC, abstractmethod

# ==========================================
# 1. TEMEL ARAYÜZ VE SOMUT SINIFLAR
# ==========================================
class Notification(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass

class EmailNotification(Notification):
    def send(self, recipient: str, message: str) -> None:
        print(f"[Email] Alıcı: {recipient} | Mesaj: {message}")

class SMSNotification(Notification):
    def send(self, recipient: str, message: str) -> None:
        print(f"[SMS] Alıcı: {recipient} | Mesaj: {message}")


# ==========================================
# 2. ADAPTER PATTERN (UYUMSUZ SİSTEM ENTEGRASYONU)
# ==========================================
class LegacySmsLibrary:
    """Hayali dış kütüphane — metod isimleri sistemimize uymuyor."""
    def push_msg(self, text: str, phone: str) -> None:
        print(f"[Legacy SMS Library] {phone} numarasına gönderiliyor: {text}")

class SmsAdapter(Notification):
    """
    Adaptör: LegacySmsLibrary'nin push_msg(text, phone) metodunu,
    bizim send(recipient, message) arayüzümüze bağlar.
    """
    def __init__(self):
        self._legacy = LegacySmsLibrary()

    def send(self, recipient: str, message: str) -> None:
        # send(recipient, message) → push_msg(text, phone) dönüşümü
        self._legacy.push_msg(message, recipient)


# ==========================================
# 3. DECORATOR PATTERN (DİNAMİK ÖZELLİK EKLEME)
# ==========================================
class NotificationDecorator(Notification):
    """Temel Decorator — sarılan nesneye delege eder."""
    def __init__(self, wrapped: Notification):
        self._wrapped = wrapped

    def send(self, recipient: str, message: str) -> None:
        # FIX: return yerine doğrudan çağrı; alt sınıflar super() ile zinciri sürdürür
        self._wrapped.send(recipient, message)


class EncryptionDecorator(NotificationDecorator):
    """Mesajı şifreleyip alt katmana iletir."""
    def send(self, recipient: str, message: str) -> None:
        encrypted_message = message[::-1]            # Basit simülasyon
        print(f"[SİSTEM] Mesaj şifrelendi.")
        # FIX: şifrelenmiş mesajı super()'a geçiriyoruz (orijinal kod bunu yapıyordu
        #      ama NotificationDecorator.send'de return eksikliği zinciri kırıyordu)
        super().send(recipient, f"ENC({encrypted_message})")


class LoggingDecorator(NotificationDecorator):
    """Gönderimi gerçekleştirip ardından loglar."""
    def send(self, recipient: str, message: str) -> None:
        # FIX: Önce gönder, sonra logla — "gönderildi" logu gönderimden SONRA atılmalı
        super().send(recipient, message)
        print(f"[LOG] '{recipient}' adresine bildirim başarıyla gönderildi.")


# ==========================================
# 4. FACTORY & REGISTRY
# ==========================================
class NotificationFactory:
    _registry: dict = {}

    @classmethod
    def register(cls, type_name: str, class_ref) -> None:
        cls._registry[type_name] = class_ref

    @classmethod
    def create(cls, type_name: str) -> Notification:
        class_ref = cls._registry.get(type_name)
        if not class_ref:
            raise ValueError(f"Bilinmeyen bildirim tipi: '{type_name}'")
        return class_ref()

# Kayıt işlemleri
NotificationFactory.register("email",      EmailNotification)
NotificationFactory.register("sms",        SMSNotification)
NotificationFactory.register("legacy_sms", SmsAdapter)


# ==========================================
# 5. FACADE PATTERN
# ==========================================
class NotificationServiceFacade:
    """
    İstemciden tüm karmaşıklığı gizler:
    factory → encryption decorator → logging decorator → send
    """
    # FIX: factory bir instance değil, class method'larla çalışan bir sınıf;
    #      self.factory = NotificationFactory() yazmak yanlış değil ama
    #      gereksiz — doğrudan sınıf üzerinden çağırıyoruz.

    def send_secure_notification(
        self, type_name: str, recipient: str, message: str
    ) -> None:
        """Fabrikadan nesne üretir, şifreler, loglar ve gönderir."""

        # 1. Ham bildirici nesnesini oluştur
        notifier: Notification = NotificationFactory.create(type_name)

        # 2. Şifreleme katmanını sar  (iç katman — önce şifrele)
        encrypted_notifier = EncryptionDecorator(notifier)

        # 3. Loglama katmanını sar    (dış katman — en son logla)
        #    Doğru zincir: LoggingDecorator → EncryptionDecorator → ConcreteNotifier
        logged_notifier = LoggingDecorator(encrypted_notifier)

        # 4. Gönder
        logged_notifier.send(recipient, message)


# ==========================================
# TEST KULLANIMI
# ==========================================
if __name__ == "__main__":
    facade = NotificationServiceFacade()

    print("=" * 50)
    print("Örnek 1: Şifreli + Loglu E-posta")
    print("=" * 50)
    facade.send_secure_notification("email", "fatma@edu.tr", "Merhaba Faz 2!")

    print()
    print("=" * 50)
    print("Örnek 2: Şifreli + Loglu Normal SMS")
    print("=" * 50)
    facade.send_secure_notification("sms", "0532 111 22 33", "SMS testi.")

    print()
    print("=" * 50)
    print("Örnek 3: Adaptör ile Eski SMS Sistemi")
    print("=" * 50)
    facade.send_secure_notification("legacy_sms", "0555 000 00 00", "Adaptör testi.")

    print()
    print("=" * 50)
    print("Örnek 4: Bilinmeyen tip → ValueError")
    print("=" * 50)
    try:
        facade.send_secure_notification("push", "user123", "Bu tip kayıtlı değil.")
    except ValueError as e:
        print(f"[HATA] {e}")