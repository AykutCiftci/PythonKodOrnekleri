def sifrele(metin):
    şifreli_metin = ""
    for harf in metin:
        asciikod=ord(harf)
        asciikod+=key
        karakterkod=chr(asciikod)
        şifreli_metin += karakterkod

    print("Şifresiz : {clear}\n Şifreli : {code}".format(clear=metin,code=şifreli_metin))

def sifre_çöz(sifreli_metin):
    metin = ""
    for harf in sifreli_metin:
        asciikod=ord(harf)
        asciikod=asciikod-key
        karakterkod=chr(asciikod)
        metin += karakterkod

    print("Şifreli : {code}\n Şifresiz : {clear}".format(code=sifreli_metin,clear=metin))


print("""
Python Sezar Şifreleme Uygulaması
[1] Şifre Oluştur
[2] Şifre Çöz
""")
try:
    op = int(input("İşlem Numarası : "))
    key = int(input("Anahtar gir : "))
except ValueError:
    print('Sayısal değer gir')
    exit()
if op == 1:
    yazı = input("Şifrelemek istediğiniz metni giriniz : ")
    sifrele(yazı)

elif op == 2:
    yazı2 = input("Şifresiniz çözmek istediğiniz metni giriniz : ")
    sifre_çöz(yazı2)

else:
    print("Yanlış tuşa bastınız")