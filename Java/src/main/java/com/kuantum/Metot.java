package com.kuantum;

/**
 * Inheritance & Polymorphism - Metot sınıfı
 * KuantumNesnesi'nden türetilmiş sınıf
 */
public class Metot extends KuantumNesnesi {
    private String analizTipi;
    private boolean durumBilgisiAktif;

    public Metot(String id, String analizTipi) {
        super(id);
        this.analizTipi = analizTipi;
        this.durumBilgisiAktif = true;
    }

    // Getter ve Setter metodları
    public String getAnalizTipi() {
        return analizTipi;
    }

    public void setAnalizTipi(String analizTipi) {
        this.analizTipi = analizTipi;
    }

    public boolean isDurumBilgisiAktif() {
        return durumBilgisiAktif;
    }

    public void setDurumBilgisiAktif(boolean durumBilgisiAktif) {
        this.durumBilgisiAktif = durumBilgisiAktif;
    }

    @Override
    public void tehlikeSeviyesi() {
        if (getStabilite() < 20) {
            System.out.println("KRİTİK: " + getId() + " metodu çökme riski altında! Stabilite: " + getStabilite() + "%");
        } else if (getStabilite() < 50) {
            System.out.println("UYARI: " + getId() + " metodu kararsız. Stabilite: " + getStabilite() + "%");
        } else {
            System.out.println("STABIL: " + getId() + " metodu normal çalışıyor. Stabilite: " + getStabilite() + "%");
        }
    }

    @Override
    public void durumBilgisi() {
        super.durumBilgisi();
        System.out.println("Analiz Tipi: " + analizTipi + ", Durum Bilgisi Aktif: " + durumBilgisiAktif);
    }
}
