import sqlite3

import time


class Bilgisayar():
    def __init__(self, model, fiyat, adet):
        self.model = model
        self.fiyat = fiyat
        self.adet = adet


class Kullanıcı():

    def __init__(self, kullanici_adi, sifre, bakiye):
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre
        self.bakiye = bakiye

    def __str__(self):
        return "Kullanıcı Adı: {}\nSifre: {}\nBakiye: {}\n".format(self.kullanici_adi, self.sifre, self.bakiye)


class ATM():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("uyeler.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists Kullanicilar (kullanici_adi TEXT,sifre INT,bakiye INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def uye_goster(self, uye_isim):

        self.cursor.execute("Select * From Kullanicilar where kullanici_adi= ?", (uye_isim,))

        uye = self.cursor.fetchone()

        if uye:
            return uye

        else:
            return None

    def uye_ekle(self, kullanici):
        sorgu = "Insert into Kullanicilar Values(?,?,?)"

        self.cursor.execute(sorgu, (kullanici.kullanici_adi, kullanici.sifre, kullanici.bakiye))

        self.baglanti.commit()

    def uye_cek(self):
     while True:
        a = input("Kullanıcı adınız: ")
        b = input("Parolanız: ")

        self.cursor.execute("""SELECT * FROM Kullanicilar WHERE
                kullanici_adi = ? AND sifre = ?""", (a, b))

        uye = self.cursor.fetchone()
        if uye:
            if uye[0] == "admin":
                print("Sisteme hoşgeldin {} :)".format(uye[0]))
                kullanici2 = Kullanıcı(kullanici_adi=uye[0], sifre=uye[1], bakiye=uye[2])
                return kullanici2


            else:
                print("Ayrıcalıklı alışverişe HOŞGELDİN {} :)".format(uye[0]))
                kullanici1 = Kullanıcı(kullanici_adi=uye[0], sifre=uye[1], bakiye=uye[2])
                return kullanici1


        else:
            print("Parola veya kullanıcı adı yanlış!")

    def uye_satis(self,fiyat,isim):

        self.cursor.execute("UPDATE Kullanicilar SET bakiye =? where kullanici_adi = ?", (fiyat,isim))
        self.baglanti.commit()


class PC():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("uyeler.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists PC (adi TEXT,fiyat INT,stok INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def pc_stok(self):
        self.cursor.execute("Select * From PC")
        pc = self.cursor.fetchall()
        for i in pc:
            print("{} = Adı:{} Adeti:{} Tane".format(i[0], i[1],i[3]))

    def pc_fiyat(self):
        self.cursor.execute("Select * From PC")

        pc = self.cursor.fetchall()
        for i in pc:
            print("{} = Adı:{} Fiyatı:{} TL Adeti:{} Tane".format(i[0], i[1], i[2], i[3]))

    def pc_sorgulama(self, id):
        self.cursor.execute("Select * From PC where id= ?", (id,))
        pc = self.cursor.fetchone()
        bilgisayar = Bilgisayar(model=pc[1], fiyat=pc[2], adet=pc[3])
        return bilgisayar

    def pc_satis(self,adet,id):
        self.cursor.execute("UPDATE PC SET adet = ? where id = ?", (adet,id))
        self.baglanti.commit()

    def pc_fiyat_guncelleme(self,fiyat,id):
        self.cursor.execute("UPDATE PC SET fiyat = ? where id = ?", (fiyat,id))
        self.baglanti.commit()
