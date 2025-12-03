using System;
using System.Collections.Generic;

namespace KuantumKaosYonetimi
{
    // Interface Segregation - IKritik arayüzü
    public interface IKritik
    {
        void AcilDurumSogutmasi();
    }

    // Abstract Class & Encapsulation - KuantumNesnesi
    public abstract class KuantumNesnesi
    {
        // Encapsulation - Private fields with public properties
        private string id;
        private double stabilite;

        public string ID 
        { 
            get { return id; } 
            set { id = value; } 
        }

        public double Stabilite 
        { 
            get { return stabilite; } 
            set 
            { 
                if (value >= 0 && value <= 100)
                    stabilite = value;
                else
                    throw new ArgumentException("Stabilite 0-100 arasında olmalıdır!");
            } 
        }

        // Constructor
        protected KuantumNesnesi(string id)
        {
            this.ID = id;
            this.Stabilite = 50.0; // Varsayılan stabilite
        }

        // Abstract method - Alt sınıflar tarafından implement edilmeli
        public abstract void TehlikeSeviyesi();

        // Virtual method - Override edilebilir
        public virtual void DurumBilgisi()
        {
            Console.WriteLine($"Nesne ID: {ID}, Stabilite: {Stabilite}%");
        }
    }

    // Inheritance & Polymorphism - Ambar sınıfı
    public class Ambar : KuantumNesnesi, IKritik
    {
        private string yerVardiyaAmirsiniz;

        public string YerVardiyaAmirsiniz 
        { 
            get { return yerVardiyaAmirsiniz; } 
            set { yerVardiyaAmirsiniz = value; } 
        }

        public Ambar(string id, string amir) : base(id)
        {
            this.YerVardiyaAmirsiniz = amir;
        }

        public override void TehlikeSeviyesi()
        {
            if (Stabilite < 30)
                Console.WriteLine($"UYARI: {ID} ambarı kritik seviyede! Stabilite: {Stabilite}%");
            else if (Stabilite < 60)
                Console.WriteLine($"DİKKAT: {ID} ambarı orta risk seviyesinde. Stabilite: {Stabilite}%");
            else
                Console.WriteLine($"GÜVENLİ: {ID} ambarı güvenli seviyede. Stabilite: {Stabilite}%");
        }

        public void AcilDurumSogutmasi()
        {
            Console.WriteLine($"{ID} ambarı için acil durum soğutması başlatıldı!");
            Stabilite = Math.Min(100, Stabilite + 20);
        }

        public override void DurumBilgisi()
        {
            base.DurumBilgisi();
            Console.WriteLine($"Vardiya Amiri: {YerVardiyaAmirsiniz}");
        }
    }

    // Inheritance & Polymorphism - Metot sınıfı
    public class Metot : KuantumNesnesi
    {
        private string analizTipi;
        private bool durumBilgisi;

        public string AnalizTipi 
        { 
            get { return analizTipi; } 
            set { analizTipi = value; } 
        }

        public bool DurumBilgisiAktif 
        { 
            get { return durumBilgisi; } 
            set { durumBilgisi = value; } 
        }

        public Metot(string id, string analizTipi) : base(id)
        {
            this.AnalizTipi = analizTipi;
            this.DurumBilgisiAktif = true;
        }

        public override void TehlikeSeviyesi()
        {
            if (Stabilite < 20)
                Console.WriteLine($"KRİTİK: {ID} metodu çökme riski altında! Stabilite: {Stabilite}%");
            else if (Stabilite < 50)
                Console.WriteLine($"UYARI: {ID} metodu kararsız. Stabilite: {Stabilite}%");
            else
                Console.WriteLine($"STABIL: {ID} metodu normal çalışıyor. Stabilite: {Stabilite}%");
        }

        public override void DurumBilgisi()
        {
            base.DurumBilgisi();
            Console.WriteLine($"Analiz Tipi: {AnalizTipi}, Durum Bilgisi Aktif: {DurumBilgisiAktif}");
        }
    }

    // Main Program
    class Program
    {
        static double GetValidStability(string prompt)
        {
            while (true)
            {
                Console.Write(prompt);
                if (double.TryParse(Console.ReadLine(), out double value))
                {
                    if (value >= 0 && value <= 100)
                        return value;
                    Console.WriteLine("Hatalı giriş! 0-100 arasında bir sayı giriniz.");
                }
                else
                {
                    Console.WriteLine("Hatalı giriş! Lütfen sayısal bir değer giriniz.");
                }
            }
        }

        static int GetValidMenuChoice(string prompt, int max)
        {
            while (true)
            {
                Console.Write(prompt);
                if (int.TryParse(Console.ReadLine(), out int value))
                {
                    if (value >= 1 && value <= max)
                        return value;
                    Console.WriteLine($"Hatalı giriş! 1-{max} arasında bir sayı giriniz.");
                }
                else
                {
                    Console.WriteLine("Hatalı giriş! Lütfen sayısal bir değer giriniz.");
                }
            }
        }

        static void YeniNesneEkle(List<KuantumNesnesi> kuantumNesneleri)
        {
            Console.WriteLine("\n=== YENİ NESNE EKLE ===");
            Console.WriteLine("1. Ambar");
            Console.WriteLine("2. Metot");
            int tip = GetValidMenuChoice("Nesne tipi seçiniz (1-2): ", 2);

            Console.Write("ID giriniz: ");
            string nesneId = Console.ReadLine() ?? "UNKNOWN";
            double stabilite = GetValidStability("Stabilite giriniz (0-100): ");

            if (tip == 1)
            {
                Console.Write("Vardiya Amiri giriniz: ");
                string amir = Console.ReadLine() ?? "Bilinmiyor";
                Ambar nesne = new Ambar(nesneId, amir);
                nesne.Stabilite = stabilite;
                kuantumNesneleri.Add(nesne);
                Console.WriteLine($"✓ Ambar {nesneId} başarıyla eklendi!");
            }
            else
            {
                Console.Write("Analiz Tipi giriniz: ");
                string analizTipi = Console.ReadLine() ?? "Bilinmiyor";
                Metot nesne = new Metot(nesneId, analizTipi);
                nesne.Stabilite = stabilite;
                kuantumNesneleri.Add(nesne);
                Console.WriteLine($"✓ Metot {nesneId} başarıyla eklendi!");
            }
        }

        static void NesneleriListele(List<KuantumNesnesi> kuantumNesneleri)
        {
            Console.WriteLine("\n=== NESNE LİSTESİ (DURUM RAPORU) ===");
            if (kuantumNesneleri.Count == 0)
            {
                Console.WriteLine("Henüz hiç nesne eklenmemiş.");
                return;
            }

            for (int i = 0; i < kuantumNesneleri.Count; i++)
            {
                Console.WriteLine($"\n{i + 1}. Nesne:");
                kuantumNesneleri[i].DurumBilgisi();
            }
        }

        static void TehlikeyiAnalizEt(List<KuantumNesnesi> kuantumNesneleri)
        {
            Console.WriteLine("\n=== TEHLİKE ANALİZİ ===");
            if (kuantumNesneleri.Count == 0)
            {
                Console.WriteLine("Henüz hiç nesne eklenmemiş.");
                return;
            }

            foreach (KuantumNesnesi nesne in kuantumNesneleri)
            {
                nesne.TehlikeSeviyesi();
                Console.WriteLine("---");
            }
        }

        static void AcilDurumSogutmasiYap(List<KuantumNesnesi> kuantumNesneleri)
        {
            Console.WriteLine("\n=== ACİL DURUM SOĞUTMASI ===");
            if (kuantumNesneleri.Count == 0)
            {
                Console.WriteLine("Henüz hiç nesne eklenmemiş.");
                return;
            }

            bool bulundu = false;
            foreach (KuantumNesnesi nesne in kuantumNesneleri)
            {
                if (nesne is IKritik kritikNesne)
                {
                    kritikNesne.AcilDurumSogutmasi();
                    Console.WriteLine("---");
                    bulundu = true;
                }
            }

            if (!bulundu)
            {
                Console.WriteLine("Soğutma yapılabilecek nesne bulunamadı.");
            }
        }

        static void Main(string[] args)
        {
            Console.WriteLine("=== KUANTUM KAOS YÖNETİMİ SİSTEMİ ===");
            Console.WriteLine("C# Implementation\n");

            // Polymorphism - Farklı türdeki nesneleri aynı listede saklama
            List<KuantumNesnesi> kuantumNesneleri = new List<KuantumNesnesi>();

            // Ana döngü (Main Loop)
            while (true)
            {
                Console.WriteLine("\n" + new string('=', 50));
                Console.WriteLine("KUANTUM AMBARI KONTROL PANELİ");
                Console.WriteLine(new string('=', 50));
                Console.WriteLine("1. Yeni Nesne Ekle (Rastgele Veri/Kararlık Madde/Anti Madde üretir)");
                Console.WriteLine("2. Nesneleri Listele (Durum Raporu)");
                Console.WriteLine("3. Tehlikeyi Analiz Et (ID integersı)");
                Console.WriteLine("4. Acil Durum Soğutması Yap (Sadece İKritik olanlar için)");
                Console.WriteLine("5. Çıkış");

                int secim = GetValidMenuChoice("Seçiminiz (1-5): ", 5);

                if (secim == 1)
                {
                    YeniNesneEkle(kuantumNesneleri);
                }
                else if (secim == 2)
                {
                    NesneleriListele(kuantumNesneleri);
                }
                else if (secim == 3)
                {
                    TehlikeyiAnalizEt(kuantumNesneleri);
                }
                else if (secim == 4)
                {
                    AcilDurumSogutmasiYap(kuantumNesneleri);
                }
                else if (secim == 5)
                {
                    Console.WriteLine("\n=== SİSTEM RAPORU ===");
                    int kritikSayisi = 0;
                    int guvenliSayisi = 0;

                    foreach (KuantumNesnesi nesne in kuantumNesneleri)
                    {
                        if (nesne.Stabilite < 30)
                            kritikSayisi++;
                        else if (nesne.Stabilite >= 60)
                            guvenliSayisi++;
                    }

                    Console.WriteLine($"Toplam Nesne: {kuantumNesneleri.Count}");
                    Console.WriteLine($"Kritik Seviye: {kritikSayisi}");
                    Console.WriteLine($"Güvenli Seviye: {guvenliSayisi}");
                    Console.WriteLine($"Orta Risk Seviye: {kuantumNesneleri.Count - kritikSayisi - guvenliSayisi}");
                    Console.WriteLine("\nProgram sonlandırılıyor...");
                    break;
                }
            }

            Console.WriteLine("\nÇıkmak için bir tuşa basın...");
            Console.ReadKey();
        }
    }
}
