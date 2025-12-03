package com.kuantum;

/**
 * Inheritance & Polymorphism - Ambar sınıfı
 * KuantumNesnesi'nden türetilmiş ve IKritik interface'ini implement eder
 */
public class Ambar extends KuantumNesnesi implements IKritik {
    private String yerVardiyaAmirsiniz;

    public Ambar(String id, String amir) {
        super(id);
        this.yerVardiyaAmirsiniz = amir;
    }

    // Getter ve Setter
    public String getYerVardiyaAmirsiniz() {
        return yerVardiyaAmirsiniz;
    }

    public void setYerVardiyaAmirsiniz(String yerVardiyaAmirsiniz) {
        this.yerVardiyaAmirsiniz = yerVardiyaAmirsiniz;
    }

    @Override
    public void tehlikeSeviyesi() {
        if (getStabilite() < 30) {
            System.out.println("UYARI: " + getId() + " ambarı kritik seviyede! Stabilite: " + getStabilite() + "%");
        } else if (getStabilite() < 60) {
            System.out.println("DİKKAT: " + getId() + " ambarı orta risk seviyesinde. Stabilite: " + getStabilite() + "%");
        } else {
            System.out.println("GÜVENLİ: " + getId() + " ambarı güvenli seviyede. Stabilite: " + getStabilite() + "%");
        }
    }

    @Override
    public void acilDurumSogutmasi() {
        System.out.println(getId() + " ambarı için acil durum soğutması başlatıldı!");
        setStabilite(Math.min(100, getStabilite() + 20));
    }

    @Override
    public void durumBilgisi() {
        super.durumBilgisi();
        System.out.println("Vardiya Amiri: " + yerVardiyaAmirsiniz);
    }
}
