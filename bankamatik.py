YusufHesap = {
    "ad": "Yusuf Büyükdağ",
    "hesapNo": "123434567",
    "bakiye": 3000,
    "ekHesap": 2000
    }

AliHesap = {
    "ad": "Ali Turan",
    "hesapNo": "234234234",
    "bakiye": 2000,
    "ekHesap": 1000
}

def paraCek(hesap, miktar):
    print("Merhaba", hesap["ad"])

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz.")
        
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if toplam >= miktar:
            ekHesapKullanimi = input("Ek hesap kullanılsın mı (E/H)?")

            if ekHesapKullanimi == "E":
                ekHesapKullanilicakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekHesapKullanilicakMiktar
                print("Paranızı alabilirsiniz.")
               

            else:
                print(hesap["hesapNo"]," nolu hesabınızda ",hesap["bakiye"]," TL bulunmaktadır." )    

        else:
            print("Bakiyeniz yetersizdir.")

def bakiyeSorgula(hesap):
    print(hesap["hesapNo"]," nolu hesabınızda ",hesap["bakiye"]," TL bulunmaktadır. Ek hesap limitiniz ise ",hesap["ekHesap"]," TL'dir.")

paraCek(YusufHesap, 3000)
bakiyeSorgula(YusufHesap)

print("******************")
paraCek(YusufHesap, 2000)
bakiyeSorgula(YusufHesap)
