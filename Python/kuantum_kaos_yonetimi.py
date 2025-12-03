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
import random


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


def get_valid_stability(prompt: str) -> float:
    """Kullanıcıdan geçerli bir stabilite değeri alır"""
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            print("Hatalı giriş! 0-100 arasında bir sayı giriniz.")
        except ValueError:
            print("Hatalı giriş! Lütfen sayısal bir değer giriniz.")

def get_valid_menu_choice(prompt: str, max_choice: int) -> int:
    """Kullanıcıdan geçerli bir menü seçimi alır"""
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= max_choice:
                return value
            print(f"Hatalı giriş! 1-{max_choice} arasında bir sayı giriniz.")
        except ValueError:
            print("Hatalı giriş! Lütfen sayısal bir değer giriniz.")

def yeni_nesne_ekle(kuantum_nesneleri: List[KuantumNesnesi]) -> None:
    """Yeni nesne ekleme fonksiyonu"""
    print("\n=== YENİ NESNE EKLE ===")
    print("1. Ambar")
    print("2. Metot")
    tip = get_valid_menu_choice("Nesne tipi seçiniz (1-2): ", 2)
    
    nesne_id = input("ID giriniz: ")
    stabilite = get_valid_stability("Stabilite giriniz (0-100): ")
    
    if tip == 1:
        amir = input("Vardiya Amiri giriniz: ")
        nesne = Ambar(nesne_id, amir)
        nesne.stabilite = stabilite
        kuantum_nesneleri.append(nesne)
        print(f"✓ Ambar {nesne_id} başarıyla eklendi!")
    else:
        analiz_tipi = input("Analiz Tipi giriniz: ")
        nesne = Metot(nesne_id, analiz_tipi)
        nesne.stabilite = stabilite
        kuantum_nesneleri.append(nesne)
        print(f"✓ Metot {nesne_id} başarıyla eklendi!")

def nesneleri_listele(kuantum_nesneleri: List[KuantumNesnesi]) -> None:
    """Nesneleri listeleme fonksiyonu"""
    print("\n=== NESNE LİSTESİ (DURUM RAPORU) ===")
    if not kuantum_nesneleri:
        print("Henüz hiç nesne eklenmemiş.")
        return
    
    for i, nesne in enumerate(kuantum_nesneleri, 1):
        print(f"\n{i}. Nesne:")
        nesne.durum_bilgisi()

def tehlikeyi_analiz_et(kuantum_nesneleri: List[KuantumNesnesi]) -> None:
    """Tehlike analizi fonksiyonu"""
    print("\n=== TEHLİKE ANALİZİ ===")
    if not kuantum_nesneleri:
        print("Henüz hiç nesne eklenmemiş.")
        return
    
    for nesne in kuantum_nesneleri:
        nesne.tehlike_seviyesi()
        print("---")

def acil_durum_sogutmasi_yap(kuantum_nesneleri: List[KuantumNesnesi]) -> None:
    """Acil durum soğutması fonksiyonu"""
    print("\n=== ACİL DURUM SOĞUTMASI ===")
    if not kuantum_nesneleri:
        print("Henüz hiç nesne eklenmemiş.")
        return
    
    kritik_nesneler = [n for n in kuantum_nesneleri if hasattr(n, 'acil_durum_sogutmasi')]
    if not kritik_nesneler:
        print("Soğutma yapılabilecek nesne bulunamadı.")
        return
    
    for nesne in kritik_nesneler:
        nesne.acil_durum_sogutmasi()
        print("---")

def main():
    """Ana program fonksiyonu - Menü döngüsü"""
    print("=== KUANTUM KAOS YÖNETİMİ SİSTEMİ ===")
    print("Python Implementation\n")
    
    # Polymorphism - Farklı türdeki nesneleri aynı listede saklama
    kuantum_nesneleri: List[KuantumNesnesi] = []
    
    # Ana döngü (Main Loop)
    while True:
        print("\n" + "="*50)
        print("KUANTUM AMBARI KONTROL PANELİ")
        print("="*50)
        print("1. Yeni Nesne Ekle (Rastgele Veri/Kararlık Madde/Anti Madde üretir)")
        print("2. Nesneleri Listele (Durum Raporu)")
        print("3. Tehlikeyi Analiz Et (ID integersı)")
        print("4. Acil Durum Soğutması Yap (Sadece İKritik olanlar için)")
        print("5. Çıkış")
        
        secim = get_valid_menu_choice("Seçiminiz (1-5): ", 5)
        
        if secim == 1:
            yeni_nesne_ekle(kuantum_nesneleri)
        elif secim == 2:
            nesneleri_listele(kuantum_nesneleri)
        elif secim == 3:
            tehlikeyi_analiz_et(kuantum_nesneleri)
        elif secim == 4:
            acil_durum_sogutmasi_yap(kuantum_nesneleri)
        elif secim == 5:
            print("\n=== SİSTEM RAPORU ===")
            kritik_sayisi = sum(1 for nesne in kuantum_nesneleri if nesne.stabilite < 30)
            guvenli_sayisi = sum(1 for nesne in kuantum_nesneleri if nesne.stabilite >= 60)
            
            print(f"Toplam Nesne: {len(kuantum_nesneleri)}")
            print(f"Kritik Seviye: {kritik_sayisi}")
            print(f"Güvenli Seviye: {guvenli_sayisi}")
            print(f"Orta Risk Seviye: {len(kuantum_nesneleri) - kritik_sayisi - guvenli_sayisi}")
            print("\nProgram sonlandırılıyor...")
            break


if __name__ == "__main__":
    main()
