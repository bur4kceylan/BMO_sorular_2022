sinav_sonuc = {'isim':['Ayşe K.','Ahmet M.','Nuri C.','Nawar T.','Suzan T.','Ala B.'], #sinav_sonuc isimli liste olusturdum icine tabloyu aktardim
'cinsiyet':['K','E','E','E','K','K'],     
'vize':[80, 60, 77, 25, 36, 75],
'final':[90, 50, 53, 100, 98, 66],
'gecme_notu':[]}
def gecme_notu():        

    i=0                                                                               #listedeki diger kisilerin gecme notunu hesaplayan fonksiyon
    for i in range(len(sinav_sonuc["cinsiyet"])):
        sonuc=(sinav_sonuc["vize"][i]*(3/10))+(sinav_sonuc["final"][i]*(7/10))
        sinav_sonuc["gecme_notu"].append(sonuc)
        i=1+i
def ogrenci_ekle():
#ilk ogrencinin notlarini ekliyoruz
    isim=input("bir isim giriniz:")
    cinsiyet=input("cinsiyetini giriniz:")
    vize=int(input("vize notunu giriniz:"))  
    final=int(input("final notunu giriniz:"))
    sinav_sonuc["isim"].append(isim)
    sinav_sonuc["cinsiyet"].append(cinsiyet)
    sinav_sonuc["vize"].append(vize)
    sinav_sonuc["final"].append(final)

def ogrenci_ekle1():
#ikinci ogrencinin notlarini ekliyoruz
    isim=input("bir isim giriniz:")
    cinsiyet=input("cinsiyetini giriniz:")
    vize=int(input("vize notunu giriniz:"))  
    final=int(input("final notunu giriniz:"))
    sinav_sonuc["isim"].append(isim)
    sinav_sonuc["cinsiyet"].append(cinsiyet)
    sinav_sonuc["vize"].append(vize)
    sinav_sonuc["final"].append(final)

ogrenci_ekle()
ogrenci_ekle1()
gecme_notu()
print(sinav_sonuc)

