package com.kuantum;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Ana program sınıfı - Kuantum Kaos Yönetimi Sistemi
 * Java Implementation
 */
public class KuantumKaosYonetimi {
    
    static Scanner scanner = new Scanner(System.in);
    
    static double getValidStability(String prompt) {
        while (true) {
            System.out.print(prompt);
            try {
                double value = Double.parseDouble(scanner.nextLine());
                if (value >= 0 && value <= 100) {
                    return value;
                }
                System.out.println("Hatalı giriş! 0-100 arasında bir sayı giriniz.");
            } catch (NumberFormatException e) {
                System.out.println("Hatalı giriş! Lütfen sayısal bir değer giriniz.");
            }
        }
    }
    
    static int getValidMenuChoice(String prompt, int max) {
        while (true) {
            System.out.print(prompt);
            try {
                int value = Integer.parseInt(scanner.nextLine());
                if (value >= 1 && value <= max) {
                    return value;
                }
                System.out.println("Hatalı giriş! 1-" + max + " arasında bir sayı giriniz.");
            } catch (NumberFormatException e) {
                System.out.println("Hatalı giriş! Lütfen sayısal bir değer giriniz.");
            }
        }
    }
    
    static void yeniNesneEkle(List<KuantumNesnesi> kuantumNesneleri) {
        System.out.println("\n=== YENİ NESNE EKLE ===");
        System.out.println("1. Ambar");
        System.out.println("2. Metot");
        int tip = getValidMenuChoice("Nesne tipi seçiniz (1-2): ", 2);
        
        System.out.print("ID giriniz: ");
        String nesneId = scanner.nextLine();
        double stabilite = getValidStability("Stabilite giriniz (0-100): ");
        
        if (tip == 1) {
            System.out.print("Vardiya Amiri giriniz: ");
            String amir = scanner.nextLine();
            Ambar nesne = new Ambar(nesneId, amir);
            nesne.setStabilite(stabilite);
            kuantumNesneleri.add(nesne);
            System.out.println("✓ Ambar " + nesneId + " başarıyla eklendi!");
        } else {
            System.out.print("Analiz Tipi giriniz: ");
            String analizTipi = scanner.nextLine();
            Metot nesne = new Metot(nesneId, analizTipi);
            nesne.setStabilite(stabilite);
            kuantumNesneleri.add(nesne);
            System.out.println("✓ Metot " + nesneId + " başarıyla eklendi!");
        }
    }
    
    static void nesneleriListele(List<KuantumNesnesi> kuantumNesneleri) {
        System.out.println("\n=== NESNE LİSTESİ (DURUM RAPORU) ===");
        if (kuantumNesneleri.isEmpty()) {
            System.out.println("Henüz hiç nesne eklenmemiş.");
            return;
        }
        
        for (int i = 0; i < kuantumNesneleri.size(); i++) {
            System.out.println("\n" + (i + 1) + ". Nesne:");
            kuantumNesneleri.get(i).durumBilgisi();
        }
    }
    
    static void tehlikeyiAnalizEt(List<KuantumNesnesi> kuantumNesneleri) {
        System.out.println("\n=== TEHLİKE ANALİZİ ===");
        if (kuantumNesneleri.isEmpty()) {
            System.out.println("Henüz hiç nesne eklenmemiş.");
            return;
        }
        
        for (KuantumNesnesi nesne : kuantumNesneleri) {
            nesne.tehlikeSeviyesi();
            System.out.println("---");
        }
    }
    
    static void acilDurumSogutmasiYap(List<KuantumNesnesi> kuantumNesneleri) {
        System.out.println("\n=== ACİL DURUM SOĞUTMASI ===");
        if (kuantumNesneleri.isEmpty()) {
            System.out.println("Henüz hiç nesne eklenmemiş.");
            return;
        }
        
        boolean bulundu = false;
        for (KuantumNesnesi nesne : kuantumNesneleri) {
            if (nesne instanceof IKritik) {
                IKritik kritikNesne = (IKritik) nesne;
                kritikNesne.acilDurumSogutmasi();
                System.out.println("---");
                bulundu = true;
            }
        }
        
        if (!bulundu) {
            System.out.println("Soğutma yapılabilecek nesne bulunamadı.");
        }
    }
    
    public static void main(String[] args) {
        System.out.println("=== KUANTUM KAOS YÖNETİMİ SİSTEMİ ===");
        System.out.println("Java Implementation\n");

        // Polymorphism - Farklı türdeki nesneleri aynı listede saklama
        List<KuantumNesnesi> kuantumNesneleri = new ArrayList<>();

        // Ana döngü (Main Loop)
        while (true) {
            System.out.println("\n" + "=".repeat(50));
            System.out.println("KUANTUM AMBARI KONTROL PANELİ");
            System.out.println("=".repeat(50));
            System.out.println("1. Yeni Nesne Ekle (Rastgele Veri/Kararlık Madde/Anti Madde üretir)");
            System.out.println("2. Nesneleri Listele (Durum Raporu)");
            System.out.println("3. Tehlikeyi Analiz Et (ID integersı)");
            System.out.println("4. Acil Durum Soğutması Yap (Sadece İKritik olanlar için)");
            System.out.println("5. Çıkış");

            int secim = getValidMenuChoice("Seçiminiz (1-5): ", 5);

            if (secim == 1) {
                yeniNesneEkle(kuantumNesneleri);
            } else if (secim == 2) {
                nesneleriListele(kuantumNesneleri);
            } else if (secim == 3) {
                tehlikeyiAnalizEt(kuantumNesneleri);
            } else if (secim == 4) {
                acilDurumSogutmasiYap(kuantumNesneleri);
            } else if (secim == 5) {
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
                System.out.println("\nProgram sonlandırılıyor...");
                break;
            }
        }

        scanner.close();
    }
}
