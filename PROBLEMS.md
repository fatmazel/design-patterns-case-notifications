# Proje Tasarım Sorunları (Faz 0)

Bu dosyada, başlangıç kodundaki temel tasarım kusurları listelenmiştir.

1. **Açık/Kapalı Prensibi (OCP) İhlali:** Yeni bir bildirim türü (örneğin WhatsApp) eklemek istediğimizde mevcut `NotificationManager` sınıfını değiştirmek zorundayız.
2. **Tek Sorumluluk Prensibi (SRP) İhlali:** Sınıf hem e-posta hem de SMS gönderim detaylarını aynı anda yönetiyor.
3.**Spagetti Kod Riski:** `if-else` blokları arttıkça kod okunamaz ve bakımı zor hale gelecek.
4. **Sıkı Bağlılık (Tight Coupling):** Gönderim mantıkları merkezi bir sınıfa gömülü olduğu için değişiklikler tüm sistemi etkileyebilir.
5. **Genişletilebilirlik Sorunu:** Farklı parametreler (dosya eki, öncelik vb.) gerektiren bildirimler bu yapıya kolayca entegre edilemez.

# AI Refleksiyonu ve Karşılaştırmalı Analiz
1. Uzun if-else zinciri → Strategy Pattern
send_notification metodu, her bildirim tipini if-elif blokları ile ele alıyor. Yeni bir tip eklemek ya da mevcut birini değiştirmek bu zincirinbirini büyütmek demek. Strategy pattern ile her tip (EmailNotifier, SMSNotifier, PushNotifier) kendi sınıfına taşınır; yönetici sadece arayüze konuşur.
2. Kapalı genişleme → Open/Closed Principle + arayüz
Yeni bir bildirim kanalı (WhatsApp, Slack…) eklemek için NotificationManager'ın mevcut kodunu değiştirmek gerekiyor. OCP'ye göre sınıflar genişlemeye açık, değişime kapalı olmalı. Bir Notifier arayüzü tanımlayıp somut sınıfları dışarıdan enjekte etmek yeterli.
3. İş mantığı karışımı → Factory Method
SMS'in 160 karakter kırpması, e-postanın gönderim adımları gibi kanal-özel kurallar send_notification içine gömülmüş. Factory Method ile nesne üretimi ve kanal-özel iş mantığı ilgili sınıflara taşınır; yönetici bunlardan haberdar olmak zorunda kalmaz.
4. Tek sorumluluk ihlali → SRP + Strategy
NotificationManager hem hangi kanalın kullanılacağına karar veriyor hem de her kanalın nasıl çalıştığını biliyor. Her sınıfın tek bir değişme sebebi olmalı; strateji sınıfları kendi kanalını bilir, yönetici sadece doğru stratejiyi seçip çalıştırır.