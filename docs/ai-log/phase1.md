Phase 1: Creational Patterns - AI Log

### 1. AI'ya Sorulan Soru (Prompt)
Elimdeki bildirim sisteminde nesne yaratma işlemleri tek bir sınıfta if-else bloklarıyla yapılıyor. Bu bağımlılığı azaltmak için hangi Creational örüntüyü kullanmalıyım ve Python örneği verebilir misin?

### 2. AI Yanıtının Özeti
AI şu şekilde çözüm önerisinde bulundu:

**Factory Method Tasarım Örüntüsü ile Nesne Yönetimi**
Mevcut yapıdaki karmaşık if-else bloklarını temizlemek ve kodu genişletilebilir hale getirmek için Factory Method (Fabrika Metodu) örüntüsünün kullanılması önerilmiştir.Ai verdiği örnekte soyut arayüzler , somut sınıflar ve özel yaratıcılar aracılığıyla if else bloklarını temizlemiş ve kodu genişletebilir bir hale getirmiştir. Ai if else yapısından tamamen kurtulmak için Registry (Kayıt) yapısı kurulması tavsiye edilmiştir.Ai ın önerdiği kayıt yapısı da uygulama başlangıcında tüm yaratıcı sınıflar bit sözlük yapısına kaydedilmesi yeni bir bildirim gönderileceği zaman, sistem ilgili kanalı sözlükten bulur ve nesneyi otomatik olarak oluşturulmasını öneriyor.Sonuç olarak yeni bir bildirim türü eklemek için mevcut kodda tek bir satır bile değiştirilmez; sadece yeni bir sınıf yazılır ve sisteme kaydedilir.


### 3. Uygulama ve Kararlar
AI destekli analiz sonucunda, sistemin hem mevcut hem de gelecekteki ihtiyaçlarını karşılamak için iki katmanlı bir yapıya geçildi.
İlk adımda, dağınık if-else bloklarını temizlemek için Factory Method örüntüsü benimsendi. Nesne üretim mantığı, soyut arayüzler ve somut sınıflar aracılığıyla iş akışından ayrıştırıldı.
İkinci adımda ise fabrika içindeki if-else kalıntılarından da kurtulmak için Registry yapısı kuruldu. Uygulama başlarken tüm bildirim sınıfları bir sözlüğe kaydedilir; yeni bildirim gönderilmesi gerektiğinde sistem ilgili kanalı bu sözlükten bularak nesneyi otomatik oluşturur.
Bunun en somut faydası şu: sisteme WhatsApp veya Slack gibi yeni bir kanal eklemek için mevcut koda dokunmak gerekmez. Yeni sınıfı yazıp kaydetmek yeterli. Açık/Kapalı Prensibi böylece pratikte tam olarak hayata geçirilmiş oldu.