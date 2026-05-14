# Faz 2: Yapısal (Structural) Örüntüler - AI Günlüğü

**Tarih:** 14 Mayıs 2026

# 1. AI'ya Sorulan Soru 
"Mevcut bildirim sistemindeki temel sınıfları değiştirmeden, bildirimlere 'Şifreleme' ve 'Loglama' gibi ek özellikler kazandırmak istiyorum. Ayrıca, farklı metod isimlerine sahip üçüncü taraf bir SMS servisini sisteme nasıl entegre edebilirim? Hangi yapısal örüntüleri kullanmalıyım?"

# 2. AI Yanıtının Özeti
AI, bildirim nesnelerini çalışma zamanında yeni özelliklerle sarmalamak için **Decorator** örüntüsünü önerdi. Uyumsuz arayüze sahip dış kütüphaneleri sisteme dahil etmek için ise bir dönüştürücü görevi gören **Adapter** örüntüsünü tavsiye etti.

# 3. Uygulama ve Kararlar 
AI, Decorator ve Adapter örüntülerini teknik gereksinimler için önerdi. Ancak, sistemin kullanım kolaylığını (usability) artırmak adına **Facade** örüntüsünü eklemeye bizzat karar verdim.

AI'nın önerdiği Decorator ve Factory yapıları sistemi çok güçlü kılıyor ama kullanımı karmaşıklaştırıyor. İstemcinin (main) şifreleme nesnesini ayrı, fabrika nesnesini ayrı yönetmesi yerine; tüm bu süreci tek bir merkezden kontrol etmenin daha profesyonel bir yaklaşım olacağını düşündüm.
