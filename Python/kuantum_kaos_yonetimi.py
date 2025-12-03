#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kuantum Kaos Yönetimi Sistemi - Python Implementation
Nesne Yönelimli Programlama Prensipleri:
- Abstract Class & Encapsulation
- Interface Segregation  
- Inheritance & Polymorphism
"""

from abc import ABC, abstractmethod
from typing import List, Protocol


class IKritik(Protocol):
    """
    Interface Segregation - IKritik protokolü
    Kritik durumlarda acil müdahale gerektiren nesneler için
    """
    def acil_durum_sogutmasi(self) -> None:
        """Acil durum soğutması başlatır"""
        pass


class KuantumNesnesi(ABC):
    """
    Abstract Class & Encapsulation - KuantumNesnesi
    Tüm kuantum nesnelerinin temel sınıfı
    """
    
    def __init__(self, id_: str):
        """
        Constructor
        Args:
            id_: Nesne kimliği
        """
        self._id = id_  # Encapsulation - private attribute
        self._stabilite = 50.0  # Varsayılan stabilite
    
    @property
    def id(self) -> str:
        """ID getter (Encapsulation)"""
        return self._id
    
    @id.setter
    def id(self, value: str) -> None:
        """ID setter (Encapsulation)"""
        self._id = value
    
    @property
    def stabilite(self) -> float:
        """Stabilite getter (Encapsulation)"""
        return self._stabilite
    
    @stabilite.setter
    def stabilite(self, value: float) -> None:
        """
        Stabilite setter (Encapsulation)
        Args:
            value: 0-100 arasında stabilite değeri
        Raises:
            ValueError: Stabilite değeri geçersizse
        """
        if 0 <= value <= 100:
            self._stabilite = value
        else:
            raise ValueError("Stabilite 0-100 arasında olmalıdır!")
    
    @abstractmethod
    def tehlike_seviyesi(self) -> None:
        """Abstract method - Alt sınıflar tarafından implement edilmeli"""
        pass
    
    def durum_bilgisi(self) -> None:
        """Virtual method - Override edilebilir"""
        print(f"Nesne ID: {self._id}, Stabilite: {self._stabilite}%")


class Ambar(KuantumNesnesi):
    """
    Inheritance & Polymorphism - Ambar sınıfı
    KuantumNesnesi'nden türetilmiş ve IKritik interface'ini implement eder
    """
    
    def __init__(self, id_: str, amir: str):
        """
        Constructor
        Args:
            id_: Ambar kimliği
            amir: Vardiya amiri adı
        """
        super().__init__(id_)
        self._yer_vardiya_amirsiniz = amir
    
    @property
    def yer_vardiya_amirsiniz(self) -> str:
        """Vardiya amiri getter"""
        return self._yer_vardiya_amirsiniz
    
    @yer_vardiya_amirsiniz.setter
    def yer_vardiya_amirsiniz(self, value: str) -> None:
        """Vardiya amiri setter"""
        self._yer_vardiya_amirsiniz = value
    
    def tehlike_seviyesi(self) -> None:
        """Tehlike seviyesini değerlendirir ve rapor eder"""
        if self.stabilite < 30:
            print(f"UYARI: {self.id} ambarı kritik seviyede! Stabilite: {self.stabilite}%")
        elif self.stabilite < 60:
            print(f"DİKKAT: {self.id} ambarı orta risk seviyesinde. Stabilite: {self.stabilite}%")
        else:
            print(f"GÜVENLİ: {self.id} ambarı güvenli seviyede. Stabilite: {self.stabilite}%")
    
    def acil_durum_sogutmasi(self) -> None:
        """IKritik interface implementation - Acil durum soğutması"""
        print(f"{self.id} ambarı için acil durum soğutması başlatıldı!")
        self.stabilite = min(100, self.stabilite + 20)
    
    def durum_bilgisi(self) -> None:
        """Override - Genişletilmiş durum bilgisi"""
        super().durum_bilgisi()
        print(f"Vardiya Amiri: {self._yer_vardiya_amirsiniz}")


class Metot(KuantumNesnesi):
    """
    Inheritance & Polymorphism - Metot sınıfı
    KuantumNesnesi'nden türetilmiş sınıf
    """
    
    def __init__(self, id_: str, analiz_tipi: str):
        """
        Constructor
        Args:
            id_: Metot kimliği
            analiz_tipi: Analiz türü
        """
        super().__init__(id_)
        self._analiz_tipi = analiz_tipi
        self._durum_bilgisi_aktif = True
    
    @property
    def analiz_tipi(self) -> str:
        """Analiz tipi getter"""
        return self._analiz_tipi
    
    @analiz_tipi.setter
    def analiz_tipi(self, value: str) -> None:
        """Analiz tipi setter"""
        self._analiz_tipi = value
    
    @property
    def durum_bilgisi_aktif(self) -> bool:
        """Durum bilgisi aktiflik durumu getter"""
        return self._durum_bilgisi_aktif
    
    @durum_bilgisi_aktif.setter
    def durum_bilgisi_aktif(self, value: bool) -> None:
        """Durum bilgisi aktiflik durumu setter"""
        self._durum_bilgisi_aktif = value
    
    def tehlike_seviyesi(self) -> None:
        """Tehlike seviyesini değerlendirir ve rapor eder"""
        if self.stabilite < 20:
            print(f"KRİTİK: {self.id} metodu çökme riski altında! Stabilite: {self.stabilite}%")
        elif self.stabilite < 50:
            print(f"UYARI: {self.id} metodu kararsız. Stabilite: {self.stabilite}%")
        else:
            print(f"STABIL: {self.id} metodu normal çalışıyor. Stabilite: {self.stabilite}%")
    
    def durum_bilgisi(self) -> None:
        """Override - Genişletilmiş durum bilgisi"""
        super().durum_bilgisi()
        print(f"Analiz Tipi: {self._analiz_tipi}, Durum Bilgisi Aktif: {self._durum_bilgisi_aktif}")


def main():
    """Ana program fonksiyonu"""
    print("=== KUANTUM KAOS YÖNETİMİ SİSTEMİ ===")
    print("Python Implementation\n")
    
    # Polymorphism - Farklı türdeki nesneleri aynı listede saklama
    kuantum_nesneleri: List[KuantumNesnesi] = []
    
    # Nesneler oluşturma
    ambar1 = Ambar("AMB-001", "Ahmet Yılmaz")
    ambar1.stabilite = 25  # Kritik seviye
    
    ambar2 = Ambar("AMB-002", "Ayşe Demir")
    ambar2.stabilite = 75  # Güvenli seviye
    
    metot1 = Metot("MET-001", "Soğutma Analizi")
    metot1.stabilite = 15  # Kritik seviye
    
    metot2 = Metot("MET-002", "Stabilite Kontrolü")
    metot2.stabilite = 80  # Güvenli seviye
    
    # Listeye ekleme
    kuantum_nesneleri.extend([ambar1, ambar2, metot1, metot2])
    
    # Polymorphism - Aynı interface üzerinden farklı davranışlar
    for nesne in kuantum_nesneleri:
        nesne.durum_bilgisi()
        nesne.tehlike_seviyesi()
        
        # Interface kontrolü ve kullanımı (Duck Typing)
        if hasattr(nesne, 'acil_durum_sogutmasi'):
            nesne.acil_durum_sogutmasi()
        
        print("---")
    
    print("\n=== SİSTEM RAPORU ===")
    kritik_sayisi = sum(1 for nesne in kuantum_nesneleri if nesne.stabilite < 30)
    guvenli_sayisi = sum(1 for nesne in kuantum_nesneleri if nesne.stabilite >= 60)
    
    print(f"Toplam Nesne: {len(kuantum_nesneleri)}")
    print(f"Kritik Seviye: {kritik_sayisi}")
    print(f"Güvenli Seviye: {guvenli_sayisi}")
    print(f"Orta Risk Seviye: {len(kuantum_nesneleri) - kritik_sayisi - guvenli_sayisi}")
    
    print("\nProgram tamamlandı. Çıkmak için Enter tuşuna basın...")
    input()


if __name__ == "__main__":
    main()
