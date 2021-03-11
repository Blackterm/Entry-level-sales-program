import sqlite3
import datetime
dir(datetime.datetime)
an = datetime.datetime.now()

import locale
locale.setlocale(locale.LC_ALL, '')


class ADMIN:

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("uyeler.db")

        self.cursor = self.baglanti.cursor()

        self.cursor.execute("Create Table If not exists Satis (Alici TEXT, urun TEXT)")

        self.baglanti.commit()

    def alici_bilgisi(self,alici,urun,tarih):
        self.cursor.execute("Insert into Satis Values (?,?,?)",(alici,urun,tarih))
        self.baglanti.commit()

    def bilgi_alma(self):
        self.cursor.execute("Select * From Satis")
        alan = self.cursor.fetchall()
        for i in alan:
            print("Alıcının adı:{}   Ürünün Adı:{}   Aldığı Tarih:{}".format(i[0], i[1], i[2]))



