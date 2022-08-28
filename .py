#Kazanç ve Geçen Arabaların Tanımlanması
gunluk_gecen_arac_listesi = []
gunluk_kazanc = 0

#Otomobil Sınıfı
class otomobil:
    def __init__(self, HGS = "Belirtilmedi", Markamodel = "Belirtilmedi", Ad = "Belirtilmedi", Soyad = "Belirtilmedi", Sinif = "Belirtilmedi",Tarihsaat = "Belirtilmedi", Bakiye = "Belirtilmedi"):
        self.HGS = input("HGS Numarası: ")
        self.Markamodel = input("Arabanın Markası, modeli ve rengi: ")
        self.Ad = input("Ad: ")
        self.Soyad = input("Soyad: ")
        self.Sinif = input("Aracın Sınıfı (Sayı ile belirtiniz, Otomobil = 1, Minibüs = 2, Otobüs = 3): ")
        self.Tarihsaat = input("Tarih ve Saat ('27.08.2022-14.01' gibi belirtiniz): ")
        self.Bakiye = input("Bakiye (Bakiyesi yoksa 0 yazmanız yeterli): ")
        print("Otomobil başarıyla eklenmiştir.")
        global gunluk_gecen_arac_listesi
        gunluk_gecen_arac_listesi += {"[               HGS: {},Marka/Model/Renk {}, Ad: {}, Soyad: {}, Sınıf: {}, Tarih ve Saat {}, Bakiye: {}          ]"
        .format(self.HGS,self.Markamodel,self.Ad,self.Soyad,self.Sinif,self.Tarihsaat,self.Bakiye)
                    }
                    


#Minibüs Sınıfı
class minibus:
    def __init__(self, HGS = "Belirtilmedi", Markamodel = "Belirtilmedi", Ad = "Belirtilmedi", Soyad = "Belirtilmedi", Sinif = "Belirtilmedi", Tarihsaat = "Belirtilmedi", Bakiye = "Belirtilmedi"):
        self.HGS =  input("HGS Numarası: ")
        self.Markamodel = input("Arabanın Markası, modeli ve rengi: ")
        self.Ad = input("Ad: ")
        self.Soyad = input("Soyad: ")
        self.Sinif = input("Aracın Sınıfı (Sayı ile belirtiniz, Otomobil = 1, Minibüs = 2, Otobüs = 3): ")
        self.Tarihsaat = input("Tarih ve Saat ('27.08.2022-14.01' gibi belirtiniz): ")
        self.Bakiye = input("Bakiye (Bakiyesi yoksa 0 yazmanız yeterli): ")
        global gunluk_gecen_arac_listesi
        gunluk_gecen_arac_listesi += {"HGS: {},Marka/Model/Renk {}, Ad: {}, Soyad: {}, Sınıf: {}, Tarih ve Saat {}, Bakiye: {}                                                                                                        "
                    .format(self.HGS,self.Markamodel,self.Ad,self.Soyad,self.Sinif,self.Tarihsaat,self.Bakiye)
                    }
        print("Minibüs başarıyla eklenmiştir")

#Otobüs Sınıfı
class otobus:
    def __init__(self, HGS = "Belirtilmedi", Markamodel = "Belirtirlmedi", Ad = "Belirtilmedi", Soyad = "Belirtilmedi", Sinif = "Belirtilmedi",Tarihsaat = "Belirtilmedi", Bakiye = "Belirtilmedi"):
        self.HGS = input("HGS Numarası: ")
        self.Markamodel = input("Arabanın Markası, modeli ve rengi: ")
        self.Ad = input("Ad: ")
        self.Soyad = input("Soyad: ")
        self.Sinif = input("Aracın Sınıfı (Sayı ile belirtiniz, Otomobil = 1, Minibüs = 2, Otobüs = 3): ") 
        self.Tarihsaat = input("Tarih ve Saat ('27.08.2022-14.01' gibi belirtiniz): ")
        self.Bakiye = input("Bakiye (Bakiyesi yoksa 0 yazmanız yeterli): ")
        global gunluk_gecen_arac_listesi
        gunluk_gecen_arac_listesi += {"HGS: {},Marka/Model/Renk {}, Ad: {}, Soyad: {}, Sınıf: {}, Tarih ve Saat {}, Bakiye: {}"
                    .format(self.HGS,self.Markamodel,self.Ad,self.Soyad,self.Sinif,self.Tarihsaat,self.Bakiye)
                    }
        print("Otobüs başarıyla eklenmiştir.")

#Gişe Sınıfı
class gise:
    def __init__(self):
        global gunluk_kazanc 
        gise_islem = int(input("Araç sınıfı giriniz: "))
        if (gise_islem == 1):
            gunluk_kazanc += 100
        elif(gise_islem == 2):
            gunluk_kazanc += 200
        elif(gise_islem == 3):
            gunluk_kazanc += 300
        else:
            print("Hatalı veri girdiniz tekrar deneyin...")
            return

#Yönetim Sınıfı   
class yönetim:
    def __init__(self):
        print(gunluk_gecen_arac_listesi)



#Giriş Ekranı
print("""
---------------------------------------------------------------------

Boğaz köprüsü HGS sistemine hoşgeldiniz!

İşlemler:
 
1. Otomobil Ekleme
 
2. Minibüs Ekleme
 
3. Otobüs Ekleme
 
4. Yönetim İşlemleri(Geçen araçları görüntüleme ve toplam bakiyeyi görüntüleme)

5. Gişe İşlemleri 

İşlemlerden birini seçmek için önündeki sayıyı yazmanız yeterlidir.

Programı kapatmak için 'q' tuşuna basınız.

 ---------------------------------------------------------------------
""")

#Yapılmak İstenen İşlemler İçin:
while True:
    islem = input("İşlem Seçiniz: ")
    if (islem == "q"):
        print("Program kapanıyor...")
        break
    elif (islem == "1"):
        otomobil()
    elif (islem == "2"):
        minibus()
    elif (islem == "3"):
        otobus()
    elif (islem == "4"):
        yönetim()
    elif (islem == "5"):
        print(gunluk_kazanc)
    elif (islem == "5"):
        gise() 
    else:
        print("Farklı bir sayı girdiniz, lütfen tekrar deneyin.")


