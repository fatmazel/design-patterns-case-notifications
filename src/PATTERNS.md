# Uygulanan Tasarım Örüntüleri

Bu dosya, projenin evrim süreci boyunca sisteme dahil edilen tasarım örüntülerinin mantığını ve kazanımlarını içermektedir.

## Faz 1: Creational (Yaratımsal) Örüntüler

### 1. Factory Method & Registry
- **Nerede:** `NotificationFactory` sınıfında.
- **Neden:** Bildirim nesnelerinin (Email, SMS, Push) oluşturulma mantığını istemci koddan ayırmak ve sisteme yeni türler eklemeyi kolaylaştırmak için kullanıldı.
- **Kazanım:** Nesne yaratma süreci merkezi bir noktaya toplandı ve "Open/Closed" prensibi sağlandı.

## Faz 2: Structural (Yapısal) Örüntüler

### 1. Decorator (Süsleyici)
- **Nerede:** Şifreleme (Encryption) ve Loglama işlemlerinde.
- **Neden:** Mevcut bildirim sınıflarının kodunu değiştirmeden, onlara dinamik olarak yeni özellikler ekleyebilmek için seçildi.
- **Kazanım:** Kod tekrarı önlendi ve özellikler birbirine karıştırılmadan eklenebildi.

### 2. Adapter (Adaptör)
- **Nerede:** Üçüncü taraf (Legacy) SMS servisinin entegrasyonunda.
- **Neden:** Sistemdeki standart `send()` metodunu, dış kütüphanenin farklı metod isimleriyle uyumlu hale getirmek için kullanıldı.
- **Kazanım:** Uyumsuz arayüzler sisteme zarar vermeden entegre edildi.

### 3. Facade (Cephe) - [Bireysel Karar]
- **Nerede:** `NotificationServiceFacade` sınıfında.
- **Neden:** Factory, Decorator ve Adapter yapılarının karmaşıklığını gizlemek ve kullanıcıya tek bir basit arayüz sunmak için tasarımıma dahil ettim.
- **Kazanım:** İstemci kodun iç yapıdaki karmaşıklığı bilme zorunluluğu ortadan kaldırılarak kullanım kolaylığı sağlandı.