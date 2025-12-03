#!/usr/bin/env node
/**
 * Kuantum Kaos Yönetimi Sistemi - JavaScript Implementation
 * Nesne Yönelimli Programlama Prensipleri:
 * - Abstract Class & Encapsulation (ES6 Classes ile)
 * - Interface Segregation (Duck Typing ile)
 * - Inheritance & Polymorphism
 */

/**
 * Interface Segregation - IKritik
 * JavaScript'te interface yoktur, ancak duck typing kullanılır
 * Kritik durumlarda acil müdahale gerektiren nesneler için
 */
class IKritik {
    acilDurumSogutmasi() {
        throw new Error("acilDurumSogutmasi() metodu implement edilmelidir!");
    }
}

/**
 * Abstract Class & Encapsulation - KuantumNesnesi
 * Tüm kuantum nesnelerinin temel sınıfı
 */
class KuantumNesnesi {
    /**
     * Constructor
     * @param {string} id - Nesne kimliği
     */
    constructor(id) {
        if (this.constructor === KuantumNesnesi) {
            throw new Error("Abstract class KuantumNesnesi doğrudan instantiate edilemez!");
        }
        
        // Encapsulation - Private fields (ES2022 syntax)
        this._id = id;
        this._stabilite = 50.0; // Varsayılan stabilite
    }

    // Getter ve Setter metodları (Encapsulation)
    get id() {
        return this._id;
    }

    set id(value) {
        this._id = value;
    }

    get stabilite() {
        return this._stabilite;
    }

    set stabilite(value) {
        if (value >= 0 && value <= 100) {
            this._stabilite = value;
        } else {
            throw new Error("Stabilite 0-100 arasında olmalıdır!");
        }
    }

    /**
     * Abstract method - Alt sınıflar tarafından implement edilmeli
     */
    tehlikeSeviyesi() {
        throw new Error("tehlikeSeviyesi() metodu alt sınıflarda implement edilmelidir!");
    }

    /**
     * Virtual method - Override edilebilir
     */
    durumBilgisi() {
        console.log(`Nesne ID: ${this._id}, Stabilite: ${this._stabilite}%`);
    }
}

/**
 * Inheritance & Polymorphism - Ambar sınıfı
 * KuantumNesnesi'nden türetilmiş ve IKritik interface'ini implement eder
 */
class Ambar extends KuantumNesnesi {
    /**
     * Constructor
     * @param {string} id - Ambar kimliği
     * @param {string} amir - Vardiya amiri adı
     */
    constructor(id, amir) {
        super(id);
        this._yerVardiyaAmirsiniz = amir;
    }

    // Getter ve Setter
    get yerVardiyaAmirsiniz() {
        return this._yerVardiyaAmirsiniz;
    }

    set yerVardiyaAmirsiniz(value) {
        this._yerVardiyaAmirsiniz = value;
    }

    /**
     * Override - Tehlike seviyesini değerlendirir ve rapor eder
     */
    tehlikeSeviyesi() {
        if (this.stabilite < 30) {
            console.log(`UYARI: ${this.id} ambarı kritik seviyede! Stabilite: ${this.stabilite}%`);
        } else if (this.stabilite < 60) {
            console.log(`DİKKAT: ${this.id} ambarı orta risk seviyesinde. Stabilite: ${this.stabilite}%`);
        } else {
            console.log(`GÜVENLİ: ${this.id} ambarı güvenli seviyede. Stabilite: ${this.stabilite}%`);
        }
    }

    /**
     * IKritik interface implementation - Acil durum soğutması
     */
    acilDurumSogutmasi() {
        console.log(`${this.id} ambarı için acil durum soğutması başlatıldı!`);
        this.stabilite = Math.min(100, this.stabilite + 20);
    }

    /**
     * Override - Genişletilmiş durum bilgisi
     */
    durumBilgisi() {
        super.durumBilgisi();
        console.log(`Vardiya Amiri: ${this._yerVardiyaAmirsiniz}`);
    }
}

/**
 * Inheritance & Polymorphism - Metot sınıfı
 * KuantumNesnesi'nden türetilmiş sınıf
 */
class Metot extends KuantumNesnesi {
    /**
     * Constructor
     * @param {string} id - Metot kimliği
     * @param {string} analizTipi - Analiz türü
     */
    constructor(id, analizTipi) {
        super(id);
        this._analizTipi = analizTipi;
        this._durumBilgisiAktif = true;
    }

    // Getter ve Setter metodları
    get analizTipi() {
        return this._analizTipi;
    }

    set analizTipi(value) {
        this._analizTipi = value;
    }

    get durumBilgisiAktif() {
        return this._durumBilgisiAktif;
    }

    set durumBilgisiAktif(value) {
        this._durumBilgisiAktif = value;
    }

    /**
     * Override - Tehlike seviyesini değerlendirir ve rapor eder
     */
    tehlikeSeviyesi() {
        if (this.stabilite < 20) {
            console.log(`KRİTİK: ${this.id} metodu çökme riski altında! Stabilite: ${this.stabilite}%`);
        } else if (this.stabilite < 50) {
            console.log(`UYARI: ${this.id} metodu kararsız. Stabilite: ${this.stabilite}%`);
        } else {
            console.log(`STABIL: ${this.id} metodu normal çalışıyor. Stabilite: ${this.stabilite}%`);
        }
    }

    /**
     * Override - Genişletilmiş durum bilgisi
     */
    durumBilgisi() {
        super.durumBilgisi();
        console.log(`Analiz Tipi: ${this._analizTipi}, Durum Bilgisi Aktif: ${this._durumBilgisiAktif}`);
    }
}

/**
 * Ana program fonksiyonu
 */
function main() {
    console.log("=== KUANTUM KAOS YÖNETİMİ SİSTEMİ ===");
    console.log("JavaScript Implementation\n");

    // Polymorphism - Farklı türdeki nesneleri aynı dizide saklama
    const kuantumNesneleri = [];

    // Nesneler oluşturma
    const ambar1 = new Ambar("AMB-001", "Ahmet Yılmaz");
    ambar1.stabilite = 25; // Kritik seviye

    const ambar2 = new Ambar("AMB-002", "Ayşe Demir");
    ambar2.stabilite = 75; // Güvenli seviye

    const metot1 = new Metot("MET-001", "Soğutma Analizi");
    metot1.stabilite = 15; // Kritik seviye

    const metot2 = new Metot("MET-002", "Stabilite Kontrolü");
    metot2.stabilite = 80; // Güvenli seviye

    // Diziye ekleme
    kuantumNesneleri.push(ambar1, ambar2, metot1, metot2);

    // Polymorphism - Aynı interface üzerinden farklı davranışlar
    kuantumNesneleri.forEach(nesne => {
        nesne.durumBilgisi();
        nesne.tehlikeSeviyesi();
        
        // Interface kontrolü ve kullanımı (Duck Typing)
        if (typeof nesne.acilDurumSogutmasi === 'function') {
            nesne.acilDurumSogutmasi();
        }
        
        console.log("---");
    });

    console.log("\n=== SİSTEM RAPORU ===");
    const kritikSayisi = kuantumNesneleri.filter(nesne => nesne.stabilite < 30).length;
    const guvenliSayisi = kuantumNesneleri.filter(nesne => nesne.stabilite >= 60).length;

    console.log(`Toplam Nesne: ${kuantumNesneleri.length}`);
    console.log(`Kritik Seviye: ${kritikSayisi}`);
    console.log(`Güvenli Seviye: ${guvenliSayisi}`);
    console.log(`Orta Risk Seviye: ${kuantumNesneleri.length - kritikSayisi - guvenliSayisi}`);

    console.log("\nProgram tamamlandı. Çıkmak için Ctrl+C tuşuna basın...");
    
    // Node.js ortamında kullanıcı girişi için
    if (typeof process !== 'undefined' && process.stdin) {
        process.stdin.setRawMode(true);
        process.stdin.resume();
        process.stdin.on('data', () => {
            process.exit(0);
        });
    }
}

// Program başlatma
if (typeof require !== 'undefined' && require.main === module) {
    main();
}

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        KuantumNesnesi,
        Ambar,
        Metot,
        IKritik,
        main
    };
}
