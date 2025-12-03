package com.kuantum;

/**
 * Abstract Class & Encapsulation - KuantumNesnesi
 * Tüm kuantum nesnelerinin temel sınıfı
 */
public abstract class KuantumNesnesi {
    // Encapsulation - Private fields
    private String id;
    private double stabilite;

    // Constructor
    protected KuantumNesnesi(String id) {
        this.id = id;
        this.stabilite = 50.0; // Varsayılan stabilite
    }

    // Getter ve Setter metodları (Encapsulation)
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public double getStabilite() {
        return stabilite;
    }

    public void setStabilite(double stabilite) {
        if (stabilite >= 0 && stabilite <= 100) {
            this.stabilite = stabilite;
        } else {
            throw new IllegalArgumentException("Stabilite 0-100 arasında olmalıdır!");
        }
    }

    // Abstract method - Alt sınıflar tarafından implement edilmeli
    public abstract void tehlikeSeviyesi();

    // Virtual method - Override edilebilir
    public void durumBilgisi() {
        System.out.println("Nesne ID: " + id + ", Stabilite: " + stabilite + "%");
    }
}
