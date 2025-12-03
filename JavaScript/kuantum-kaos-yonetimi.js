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
 * Ana program fonksiyonu - Menü döngüsü
 */
async function main() {
    console.log("=== KUANTUM KAOS YÖNETİMİ SİSTEMİ ===");
    console.log("JavaScript Implementation\n");

    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const question = (query) => new Promise((resolve) => readline.question(query, resolve));

    const getValidStability = async (prompt) => {
        while (true) {
            const value = parseFloat(await question(prompt));
            if (!isNaN(value) && value >= 0 && value <= 100) {
                return value;
            }
            console.log("Hatalı giriş! 0-100 arasında bir sayı giriniz.");
        }
    };

    const getValidMenuChoice = async (prompt, max) => {
        while (true) {
            const value = parseInt(await question(prompt));
            if (!isNaN(value) && value >= 1 && value <= max) {
                return value;
            }
            console.log(`Hatalı giriş! 1-${max} arasında bir sayı giriniz.`);
        }
    };

    try {
        const kuantumNesneleri = [];

        // Ana döngü (Main Loop)
        while (true) {
            console.log("\n" + "=".repeat(50));
            console.log("KUANTUM AMBARI KONTROL PANELİ");
            console.log("=".repeat(50));
            console.log("1. Yeni Nesne Ekle (Rastgele Veri/Kararlık Madde/Anti Madde üretir)");
            console.log("2. Nesneleri Listele (Durum Raporu)");
            console.log("3. Tehlikeyi Analiz Et (ID integersı)");
            console.log("4. Acil Durum Soğutması Yap (Sadece İKritik olanlar için)");
            console.log("5. Çıkış");

            const secim = await getValidMenuChoice("Seçiminiz (1-5): ", 5);

            if (secim === 1) {
                console.log("\n=== YENİ NESNE EKLE ===");
                console.log("1. Ambar");
                console.log("2. Metot");
                const tip = await getValidMenuChoice("Nesne tipi seçiniz (1-2): ", 2);

                const nesneId = await question("ID giriniz: ");
                const stabilite = await getValidStability("Stabilite giriniz (0-100): ");

                if (tip === 1) {
                    const amir = await question("Vardiya Amiri giriniz: ");
                    const nesne = new Ambar(nesneId, amir);
                    nesne.stabilite = stabilite;
                    kuantumNesneleri.push(nesne);
                    console.log(`✓ Ambar ${nesneId} başarıyla eklendi!`);
                } else {
                    const analizTipi = await question("Analiz Tipi giriniz: ");
                    const nesne = new Metot(nesneId, analizTipi);
                    nesne.stabilite = stabilite;
                    kuantumNesneleri.push(nesne);
                    console.log(`✓ Metot ${nesneId} başarıyla eklendi!`);
                }
            } else if (secim === 2) {
                console.log("\n=== NESNE LİSTESİ (DURUM RAPORU) ===");
                if (kuantumNesneleri.length === 0) {
                    console.log("Henüz hiç nesne eklenmemiş.");
                } else {
                    kuantumNesneleri.forEach((nesne, i) => {
                        console.log(`\n${i + 1}. Nesne:`);
                        nesne.durumBilgisi();
                    });
                }
            } else if (secim === 3) {
                console.log("\n=== TEHLİKE ANALİZİ ===");
                if (kuantumNesneleri.length === 0) {
                    console.log("Henüz hiç nesne eklenmemiş.");
                } else {
                    kuantumNesneleri.forEach(nesne => {
                        nesne.tehlikeSeviyesi();
                        console.log("---");
                    });
                }
            } else if (secim === 4) {
                console.log("\n=== ACİL DURUM SOĞUTMASI ===");
                if (kuantumNesneleri.length === 0) {
                    console.log("Henüz hiç nesne eklenmemiş.");
                } else {
                    const kritikNesneler = kuantumNesneleri.filter(n => typeof n.acilDurumSogutmasi === 'function');
                    if (kritikNesneler.length === 0) {
                        console.log("Soğutma yapılabilecek nesne bulunamadı.");
                    } else {
                        kritikNesneler.forEach(nesne => {
                            nesne.acilDurumSogutmasi();
                            console.log("---");
                        });
                    }
                }
            } else if (secim === 5) {
                console.log("\n=== SİSTEM RAPORU ===");
                const kritikSayisi = kuantumNesneleri.filter(nesne => nesne.stabilite < 30).length;
                const guvenliSayisi = kuantumNesneleri.filter(nesne => nesne.stabilite >= 60).length;

                console.log(`Toplam Nesne: ${kuantumNesneleri.length}`);
                console.log(`Kritik Seviye: ${kritikSayisi}`);
                console.log(`Güvenli Seviye: ${guvenliSayisi}`);
                console.log(`Orta Risk Seviye: ${kuantumNesneleri.length - kritikSayisi - guvenliSayisi}`);
                console.log("\nProgram sonlandırılıyor...");
                break;
            }
        }
    } catch (error) {
        console.error("Bir hata oluştu:", error);
    } finally {
        readline.close();
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
