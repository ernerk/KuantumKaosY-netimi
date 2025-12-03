# Kuantum Kaos Yönetimi Sistemi - Geliştirme Raporu

## Ödev Hazırlama Yöntemi

Bu ödev, Nesne Yönelimli Programlama prensiplerini 4 farklı programlama dilinde (C#, Java, Python, JavaScript) uygulayarak geliştirilmiştir. Geliştirme sürecinde öncelikle ödevin gereksinimlerini analiz ettim ve her dil için aynı mantığı koruyarak farklı syntax ve özelliklerle implement ettim. 

**Abstract Class & Encapsulation** prensibi için KuantumNesnesi soyut sınıfını oluşturdum ve tüm dillerde private/protected alanlar ile getter/setter metodları kullandım. **Interface Segregation** için IKritik arayüzünü tasarladım ve kritik nesnelerin özel metodlarını ayırdım. **Inheritance & Polymorphism** prensipleri ile Ambar ve Metot sınıflarını KuantumNesnesi'nden türettim ve her birinin kendine özgü davranışlarını override metodlarla gerçekleştirdim. 

Her dilde aynı çıktıyı üretecek şekilde test senaryoları oluşturdum ve farklı stabilite seviyelerindeki nesnelerle sistem davranışlarını doğruladım. C# ve Java'da explicit interface kullanırken, Python ve JavaScript'te duck typing yaklaşımını tercih ettim. Tüm kodlar çalışır durumda olup, her dil için gerekli proje dosyaları (csproj, pom.xml, package.json, requirements.txt) da oluşturulmuştur.

---

**Tarih:** 3 Aralık 2025  
**Öğrenci:** [Öğrenci Adı]  
**Ders:** Nesne Yönelimli Programlama
