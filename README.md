# 🔔 Evolutionary Notification System

> Bir bildirim sisteminin "legacy" koddan tasarım örüntüleriyle nasıl evrimleştiğini adım adım gösteren eğitim projesi.

## 📖 Proje Hakkında

Bu proje, tasarım örüntülerinin bir yazılım sisteminin evrimindeki rolünü somut olarak göstermek amacıyla geliştirilmiştir.

Yazılım geliştirmede sıkça karşılaşılan **if-else yığınları** ve **katı bağımlılıklar**; Creational, Structural ve Behavioral örüntüler uygulanarak adım adım esnek ve sürdürülebilir bir yapıya dönüştürülmektedir.

Her faz, bir öncekinin sorunlarını tespit edip çözer — böylece örüntülerin *neden* gerekli olduğu, soyut kalmak yerine doğrudan gözlemlenebilir.

---

## 🗺️ Faz Yol Haritası

| Faz | Konu | Örüntüler | Durum |
|-----|------|-----------|-------|
| **Faz 0** | Legacy Kod | — | ✅ Tamamlandı |
| **Faz 1** | Nesne Yaratma | Factory, Singleton, Builder | 🔜 Bekleniyor |
| **Faz 2** | Yapısal | Adapter, Decorator, Facade | 🔜 Bekleniyor |
| **Faz 3** | Davranışsal | Observer, Strategy, Chain of Responsibility | 🔜 Bekleniyor |

---

## 🏗️ Mimari Diyagramlar

Faz geçişlerinde üretilen diyagramlar `docs/diagrams/` dizinine eklenmektedir.

```
docs/
└── diagrams/
    ├── faz0_legacy.png
    ├── faz1_creational.png   ← bekleniyor
    ├── faz2_structural.png   ← bekleniyor
    └── faz3_behavioral.png   ← bekleniyor
```

---

## 🚀 Kurulum ve Çalıştırma

**Gereksinimler:** Python 3.10+

```bash
# 1. Projeyi klonlayın
git clone https://github.com/kullanici-adi/evolutionary-notification-system.git

# 2. Proje dizinine gidin
cd evolutionary-notification-system

# 3. (Opsiyonel) Sanal ortam oluşturun
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

# 4. Bağımlılıkları yükleyin
pip install -r requirements.txt

# 5. İstediğiniz fazı çalıştırın
python faz0_legacy/main.py
```

---

## 📁 Proje Yapısı

```
evolutionary-notification-system/
│
├── faz0_legacy/
│   ├── main.py
│   └── notifier.py
│
├── faz1_creational/          ← bekleniyor
├── faz2_structural/          ← bekleniyor
├── faz3_behavioral/          ← bekleniyor
│
├── docs/
│   └── diagrams/
│
├── requirements.txt
└── README.md
```

---

## 🎯 Öğrenme Hedefleri

- **SOLID prensiplerinin** ihlal edildiği noktaları tespit etmek
- Her tasarım örüntüsünün **hangi sorunu çözdüğünü** anlamak
- Aynı sistemi farklı örüntülerle yeniden yazarak **etkiyi karşılaştırmak**

---

## 🤝 Katkı

Katkılarınızı memnuniyetle karşılarım. Lütfen önce bir `issue` açarak değişikliği tartışalım.

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.