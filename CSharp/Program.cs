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
        static void Main(string[] args)
        {
            Console.WriteLine("=== KUANTUM KAOS YÖNETİMİ SİSTEMİ ===");
            Console.WriteLine("C# Implementation\n");

            // Polymorphism - Farklı türdeki nesneleri aynı listede saklama
            List<KuantumNesnesi> kuantumNesneleri = new List<KuantumNesnesi>();

            // Nesneler oluşturma
            Ambar ambar1 = new Ambar("AMB-001", "Ahmet Yılmaz");
            ambar1.Stabilite = 25; // Kritik seviye

            Ambar ambar2 = new Ambar("AMB-002", "Ayşe Demir");
            ambar2.Stabilite = 75; // Güvenli seviye

            Metot metot1 = new Metot("MET-001", "Soğutma Analizi");
            metot1.Stabilite = 15; // Kritik seviye

            Metot metot2 = new Metot("MET-002", "Stabilite Kontrolü");
            metot2.Stabilite = 80; // Güvenli seviye

            // Listeye ekleme
            kuantumNesneleri.Add(ambar1);
            kuantumNesneleri.Add(ambar2);
            kuantumNesneleri.Add(metot1);
            kuantumNesneleri.Add(metot2);

            // Polymorphism - Aynı interface üzerinden farklı davranışlar
            foreach (KuantumNesnesi nesne in kuantumNesneleri)
            {
                nesne.DurumBilgisi();
                nesne.TehlikeSeviyesi();
                
                // Interface kontrolü ve kullanımı
                if (nesne is IKritik kritikNesne)
                {
                    kritikNesne.AcilDurumSogutmasi();
                }
                
                Console.WriteLine("---");
            }

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

            Console.WriteLine("\nProgram tamamlandı. Çıkmak için bir tuşa basın...");
            Console.ReadKey();
        }
    }
}
