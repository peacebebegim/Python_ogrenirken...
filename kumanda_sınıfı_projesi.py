import random
import time

class Kumanda():
    def __init__(self,tv_durum = "kapalı",tv_ses = 0,kanal_listesi = ["Trt","Atv","Star","Show","Bloomberg"],kanal = "Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def tv_aç(self):
        if (self.tv_durum == "Açık"):
            print("Televizyon zaten açık...")
        else:
            print("Televizyon açılıyor...")
            self.tv_durum = "Açık"
    def tv_kapat(self):
        if(self.tv_durum == "Kapalı"):
            print("Televizyon zaten kapalı...")
        else:
            print("Televizyon kapatılıyor")
            self.tv_durum = "Kapalı"
    def ses_ayarları(self):
        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Artır: '>'\nÇıkış: çıkış")
            if (cevap == "<"):
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
            elif (cevap ==">"):
                if(self.tv_ses != 31):
                    self.tv_ses += 1
                    print("Ses:",self.tv_ses)
            else:
                print("Ses güncellendi:",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi.")
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal:",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv durumu: {}\nTv ses: {}\nKanal listesi: {}\nŞu anki kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

    def ses_kapat(self):
        self.tv_ses = 0
        print("Ses kapatıldı")
        print("Ses:",self.tv_ses)

    def kanal_çıkar(self):
        sil = input("Çıkarmak istediğiniz kanal ismini giriniz:")
        print("Kanal siliniyor...")
        time.sleep(1)
        self.kanal_listesi.remove(sil)
        print("Bu kanal silindi:",sil)






kumanda = Kumanda()

print("""
Televizyon Uygulaması

1. Tv Aç
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısını Öğrenme
6. Rastgele Kanala Geçme
7. Televizyon Bilgieri
8. Sesi Kapat
9. Kanal Çıkar

Çıkmak için 'q'ya basın.

""")


while True:

    işlem = input("İşlemi Seçiniz:")
    if (işlem == "q"):
        print("Program sonlandırılıyor...")
        break

    elif (işlem == "1"):
        kumanda.tv_aç()
    elif (işlem == "2"):
        kumanda.tv_kapat()

    elif (işlem == "3"):
        kumanda.ses_ayarları()

    elif (işlem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak giriniz:")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (işlem == "5"):
        print("Kanal Sayısı:",len(kumanda))

    elif (işlem == "6"):
        kumanda.rastgele_kanal()
    elif ( işlem == "7"):
        print(kumanda)
    elif (işlem == "8"):
        kumanda.ses_kapat()
    elif (işlem == "9"):
        kumanda.kanal_çıkar()
    else:
        print("Geçersiz işlem...")



