import Yeni1 as satis
import Admin
import datetime
dir(datetime.datetime)
an = datetime.datetime.now()

import locale
locale.setlocale(locale.LC_ALL, '')
while True:
    print("""
    *************************************
    Teknoloji Marketine Hoş Geldiniz.
    Üye Olmak İçin "1" 
    Üye Girişi İçin "2"
    Çıkmak İçin "q"
    Basınız.
    **********************************
    """)
    islem = input("Yapacağınız İşlem:")

    if islem == "1":
        while True:
            kullanici_adi = input("Kullanıcı Adınız:")
            kullanici_varmi = satis.ATM().uye_goster(kullanici_adi)
            if kullanici_varmi:
                print("Böyle bir kullanıcı var.")
            else:
                break

        sifre = int(input("Şifreniz:"))
        bakiye = int(input("Yatırdığınız Miktar:"))

        yeni_kullanici = satis.Kullanıcı(kullanici_adi, sifre, bakiye)

        print("Kullanıcı Ekleniyor..")
        satis.time.sleep(2)

        satis.ATM().uye_ekle(yeni_kullanici)
        print("Ayrıcalık alışverişe hoş geldin {} :)".format(yeni_kullanici.kullanici_adi))
    elif islem == "2":
        kullanici = satis.ATM().uye_cek()
        while True:
            if kullanici.kullanici_adi == "admin":
                print("""
    ************
    Güncel Stok bilgisi için "1"
    Fiyat Güncellemek için "2"
    Güncel satış rakamları "3" 
    Önceki Sayfaya dönmek için "q"  
    Basınız.....
    *************   
                """)

                Giris = input("Lütfen değer giriniz :")

                if Giris == "1":
                    satis.PC().pc_stok()

                elif Giris == "2":
                    satis.PC().pc_fiyat()
                    id= input("Bilgisayarın numarası:")
                    ucret= int(input("Ücretini giriniz:"))
                    satis.PC().pc_fiyat_guncelleme(ucret,id)
                    print("Lütfen bekleyiniz Fiyat Güncelleniyor...")
                    satis.time.sleep(2)
                    print("Fiyat güncellenmiştir.")
                elif Giris == "3":

                    Admin.ADMIN().bilgi_alma()

                    break

                elif Giris == "q":
                    print("Hoşçakalın...")
                    break
                else:
                    print("Geçersiz işlem")

            else:
                while True:
                    print("""
                   Bilgisayar fiyatlarına bakmak için "1"
                   Satın almak için "2"
                   Bir önceki menü için "q"
                   Basınız :) 
                    """)

                    islem = input("Yapacağınız işlemi seçiniz:")


                    if islem == "1":
                        satis.PC().pc_fiyat()

                    elif islem == "2":
                        satis.PC().pc_fiyat()
                        Satis = int(input("Almak istediğiniz bilgisayar ="))
                        bilgisayar = satis.PC().pc_sorgulama(Satis)
                        b = bilgisayar.fiyat
                        d = kullanici.bakiye
                        if d < b:
                            print("Bakiyeniz Yetersiz. :/")
                        else:
                            print("Lütfen bekleyiniz..")
                            satis.time.sleep(2)

                            print("Canavar gibi {} iyi günlerde kullan {} :)".format(bilgisayar.model, kullanici.kullanici_adi))
                            Admin.ADMIN().alici_bilgisi(kullanici.kullanici_adi,bilgisayar.model,datetime.datetime.strftime(an, '%d %B %Y'))
                            a = satis.PC().pc_sorgulama(Satis)
                            e = a.adet - 1
                            satis.PC().pc_satis(e,Satis)
                            c = kullanici.bakiye-bilgisayar.fiyat
                            satis.ATM().uye_satis(c,kullanici.kullanici_adi)
                            print("Kalan bakiyeniz {}".format(c))
                            break
                    elif islem == "q":
                        print("Hoşçakalın")
                        break

                break

    elif islem == "q":
        print("Hoşçakalın..")
        break
    else:
        print("Geçersiz İşlem...")


