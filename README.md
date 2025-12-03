# Kuantum Kaos Yönetimi Sistemi

Bu proje, Nesne Yönelimli Programlama prensiplerini kullanarak 4 farklı programlama dilinde (C#, Java, Python, JavaScript) geliştirilmiş bir Kuantum Kaos Yönetimi sistemidir.

## 📋 Proje Özeti

"Omega Sektörü'ndeki Kuantum Veri Ambarı"nın yeni vardiya amirsiniz. Bu ambar, evrenin en kararsız ve tehlikeli maddelerini dijital ortamda saklar. Göreviniz basit ama süreç: Depoyu gelen maddeleri kabul etmek, onları analiz etmek ve patlamadan gün sonuna getirmek.

## 🎯 Teknik Gereksinimler

Projede aşağıdaki OOP prensipleri uygulanmıştır:

### A. Temel Yapı (Abstract Class & Encapsulation)
- **KuantumNesnesi** abstract sınıfı
- **Özellikler (Properties):**
  - ID (string): Nesnenin kimliği
  - Stabilite (double): 0 ile 100 arasında olmalıdır (Encapsulation)
- **Metodlar:**
  - AnalizTipi(): Soyut (abstract) metot
  - DurumBilgisi(): Alt sınıflar tarafından override edilebilir metot

### B. Arayüz (Interface Segregation)
- **IKritik** arayüzü
- **Metot:** AcilDurumSogutmasi()

### C. Nesne Çeşitleri (Inheritance & Polymorphism)
- **Ambar** sınıfı: KuantumNesnesi'nden türetilir ve IKritik'i implement eder
- **Metot** sınıfı: KuantumNesnesi'nden türetilir

## 🚀 Kurulum ve Çalıştırma

### Ön Gereksinimler (macOS)
Gerekli araçları Homebrew ile kurabilirsiniz:
```bash
brew install dotnet maven node python
```

### C# (.NET 9.0)
```bash
cd CSharp
dotnet run
```

### Java (Maven)
```bash
cd Java
mvn clean compile exec:java
```

### Python (3.8+)
```bash
cd Python
python3 kuantum_kaos_yonetimi.py
```

### JavaScript (Node.js 14+)
```bash
cd JavaScript
npm start
```

## 📁 Proje Yapısı

```
nesneödev2/
├── CSharp/
│   ├── Program.cs
│   └── KuantumKaosYonetimi.csproj
├── Java/
│   ├── src/main/java/com/kuantum/
│   │   ├── IKritik.java
│   │   ├── KuantumNesnesi.java
│   │   ├── Ambar.java
│   │   ├── Metot.java
│   │   └── KuantumKaosYonetimi.java
│   └── pom.xml
├── Python/
│   ├── kuantum_kaos_yonetimi.py
│   └── requirements.txt
├── JavaScript/
│   ├── kuantum-kaos-yonetimi.js
│   └── package.json
└── README.md
```

## 🔧 Özellikler

### Encapsulation (Kapsülleme)
- Tüm sınıflarda private/protected alanlar
- Getter/Setter metodları ile kontrollü erişim
- Stabilite değeri 0-100 arasında sınırlandırılmış

### Inheritance (Kalıtım)
- KuantumNesnesi abstract sınıfından türetilmiş Ambar ve Metot sınıfları
- Ortak özelliklerin ve metodların paylaşımı

### Polymorphism (Çok Biçimlilik)
- Aynı interface üzerinden farklı nesne türlerinin yönetimi
- Override edilmiş metodlar ile farklı davranışlar

### Interface Segregation (Arayüz Ayrımı)
- IKritik arayüzü ile kritik nesnelerin özel metodları
- Duck typing (Python/JavaScript) ve explicit interface (C#/Java)

## 📊 Sistem Raporu

Program çalıştırıldığında:
- Farklı stabilite seviyelerinde nesneler oluşturulur
- Tehlike seviyeleri analiz edilir
- Kritik nesneler için acil durum soğutması uygulanır
- Sistem durumu raporlanır

## 🎓 Eğitim Amaçları

Bu proje aşağıdaki konuları öğretmeyi amaçlar:
- Abstract sınıflar ve interface'ler
- Encapsulation ve data hiding
- Inheritance ve method overriding
- Polymorphism ve dynamic binding
- Farklı programlama dillerinde OOP implementasyonu

## 📝 Notlar

- Her dil kendi özelliklerine uygun olarak implement edilmiştir
- Aynı mantık ve yapı tüm dillerde korunmuştur
- Kod yorumları Türkçe olarak eklenmiştir
- Hata yönetimi ve input validation uygulanmıştır

## 👨‍💻 Geliştirici

Bu proje Nesne Yönelimli Programlama dersi kapsamında geliştirilmiştir.

---

**Not:** Tüm kodlar çalışır durumda olup, her dil için gerekli bağımlılıklar ve çalıştırma talimatları yukarıda belirtilmiştir.
