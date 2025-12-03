package com.kuantum;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Ana program sınıfı - Kuantum Kaos Yönetimi Sistemi
 * Java Implementation
 */
public class KuantumKaosYonetimi {
    public static void main(String[] args) {
        System.out.println("=== KUANTUM KAOS YÖNETİMİ SİSTEMİ ===");
        System.out.println("Java Implementation\n");

        // Polymorphism - Farklı türdeki nesneleri aynı listede saklama
        List<KuantumNesnesi> kuantumNesneleri = new ArrayList<>();

        // Nesneler oluşturma
        Ambar ambar1 = new Ambar("AMB-001", "Ahmet Yılmaz");
        ambar1.setStabilite(25); // Kritik seviye

        Ambar ambar2 = new Ambar("AMB-002", "Ayşe Demir");
        ambar2.setStabilite(75); // Güvenli seviye

        Metot metot1 = new Metot("MET-001", "Soğutma Analizi");
        metot1.setStabilite(15); // Kritik seviye

        Metot metot2 = new Metot("MET-002", "Stabilite Kontrolü");
        metot2.setStabilite(80); // Güvenli seviye

        // Listeye ekleme
        kuantumNesneleri.add(ambar1);
        kuantumNesneleri.add(ambar2);
        kuantumNesneleri.add(metot1);
        kuantumNesneleri.add(metot2);

        // Polymorphism - Aynı interface üzerinden farklı davranışlar
        for (KuantumNesnesi nesne : kuantumNesneleri) {
            nesne.durumBilgisi();
            nesne.tehlikeSeviyesi();
            
            // Interface kontrolü ve kullanımı
            if (nesne instanceof IKritik) {
                IKritik kritikNesne = (IKritik) nesne;
                kritikNesne.acilDurumSogutmasi();
            }
            
            System.out.println("---");
        }

        System.out.println("\n=== SİSTEM RAPORU ===");
        int kritikSayisi = 0;
        int guvenliSayisi = 0;

        for (KuantumNesnesi nesne : kuantumNesneleri) {
            if (nesne.getStabilite() < 30) {
                kritikSayisi++;
            } else if (nesne.getStabilite() >= 60) {
                guvenliSayisi++;
            }
        }

        System.out.println("Toplam Nesne: " + kuantumNesneleri.size());
        System.out.println("Kritik Seviye: " + kritikSayisi);
        System.out.println("Güvenli Seviye: " + guvenliSayisi);
        System.out.println("Orta Risk Seviye: " + (kuantumNesneleri.size() - kritikSayisi - guvenliSayisi));

        System.out.println("\nProgram tamamlandı. Çıkmak için Enter tuşuna basın...");
        Scanner scanner = new Scanner(System.in);
        scanner.nextLine();
        scanner.close();
    }
}
