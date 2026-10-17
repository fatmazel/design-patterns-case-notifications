# 🔔 Evolutionary Notification System

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

> Bir bildirim sisteminin "legacy" koddan tasarım örüntüleriyle nasıl evrimleştiğini adım adım gösteren eğitim projesi.

## 📖 Proje Hakkında

Yazılımda sık görülen **if-else yığınları** ve **sıkı bağımlılıklar**, bu projede Creational, Structural ve Behavioral tasarım örüntüleri uygulanarak adım adım esnek ve genişletilebilir bir yapıya dönüştürülüyor.

Her faz, bir öncekinin sorunlarını tespit edip çözüyor. Böylece örüntülerin *neden* gerekli olduğu soyut kalmadan, kodun kendi geçmişi üzerinden gözlemlenebiliyor. Her fazın kodu ayrı bir commit olarak saklandığı için commit geçmişi projenin evrim günlüğü işlevi görüyor.

---

## 🗺️ Faz Yol Haritası

| Faz | Konu | Uygulanan Örüntüler | Durum |
|-----|------|---------------------|-------|
| **Faz 0** | Legacy kodun analizi | — ([PROBLEMS.md](PROBLEMS.md)) | ✅ Tamamlandı |
| **Faz 1** | Nesne yaratma (Creational) | Factory Method + Registry | ✅ Tamamlandı |
| **Faz 2** | Yapısal (Structural) | Decorator, Adapter, Facade | ✅ Tamamlandı |
| **Faz 3** | Davranışsal (Behavioral) | Observer, Strategy, Chain of Responsibility | 🔜 Planlandı |

---

## 🏗️ Mevcut Mimari (Faz 2)

İstemci yalnızca `NotificationServiceFacade` ile konuşur; nesne üretimi, şifreleme ve loglama katmanları arka planda birleştirilir.

```
İstemci
  │
  ▼
NotificationServiceFacade            ← Facade: tek ve basit arayüz
  │
  ├── NotificationFactory.create()   ← Factory Method + Registry
  │      ├── "email"      → EmailNotification
  │      ├── "sms"        → SMSNotification
  │      └── "legacy_sms" → SmsAdapter → LegacySmsLibrary   ← Adapter
  │
  └── LoggingDecorator(EncryptionDecorator(notifier))        ← Decorator zinciri
```

Yeni bir bildirim kanalı (ör. WhatsApp) eklemek için mevcut koda dokunmak gerekmez: yeni sınıfı yazıp `NotificationFactory.register(...)` ile kaydetmek yeterlidir.

Örüntülerin nerede, neden kullanıldığı ve ne kazandırdığı [src/PATTERNS.md](src/PATTERNS.md) dosyasında ayrıntılı olarak anlatılıyor.

---

## 🚀 Çalıştırma

**Gereksinimler:** Python 3.10+ (harici bağımlılık yok, yalnızca standart kütüphane kullanılıyor)

```bash
git clone https://github.com/fatmazel/design-patterns-case-notifications.git
cd design-patterns-case-notifications
python src/main.py
```

Örnek çıktı:

```
==================================================
Örnek 1: Şifreli + Loglu E-posta
==================================================
[SİSTEM] Mesaj şifrelendi.
[Email] Alıcı: fatma@edu.tr | Mesaj: ENC(!2 zaF abahreM)
[LOG] 'fatma@edu.tr' adresine bildirim başarıyla gönderildi.
```

> Şifreleme, örüntünün işleyişini göstermek için basit bir simülasyondur (metni ters çevirir); gerçek bir şifreleme algoritması değildir.

---

## 📁 Proje Yapısı

```
design-patterns-case-notifications/
├── src/
│   ├── main.py          # Güncel faz kodu ve örnek kullanım
│   └── PATTERNS.md      # Uygulanan örüntülerin gerekçeleri ve kazanımları
├── docs/
│   └── ai-log/          # Her fazda yapay zekâ ile yapılan analiz ve verilen kararlar
│       ├── phase1.md
│       └── phase-2.md
├── PROBLEMS.md          # Faz 0: legacy koddaki tasarım sorunları
├── LICENSE
└── README.md
```

---

## 🤖 Yapay Zekâ Kullanımı

Her fazda yapay zekâdan öneri alındı; sorulan soru, alınan yanıtın özeti ve hangi önerilerin neden kabul edildiği ya da değiştirildiği `docs/ai-log/` altında belgelendi. Örneğin Faz 2'deki **Facade** katmanı, yapay zekânın önerdiği yapıların kullanımını sadeleştirmek için bireysel bir tasarım kararı olarak eklendi.

---

## 🎯 Öğrenme Hedefleri

- **SOLID prensiplerinin** ihlal edildiği noktaları tespit etmek
- Her tasarım örüntüsünün **hangi sorunu çözdüğünü** anlamak
- Aynı sistemi farklı örüntülerle yeniden yazarak **etkiyi karşılaştırmak**

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.
