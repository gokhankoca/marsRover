#!/usr/bin/env python
# -*-coding: iso-8859-9 -*-


class konum:
    def __init__(self, x=0,y=0, yon='N'):
        self.x=x
        self.y=y
        self.yon=yon
        
        
class gezegen:
    def __init__(self, genislik=0, yukseklik=0):
        self.genislik=genislik
        self.yukseklik=yukseklik      
        
        
class komut:
    def __init__(self,emir='L'):
        self.emir=emir
        
def kontrol(konum):                 #bulunulan konumun gezegenin sınırları içindeyse işlemi devam ettirir, değilse sonlandırır
        if 0<= konum.x <=gezegen.genislik and 0<= konum.y <=gezegen.yukseklik:
            pass
        else:
            print "Mars tan aşağıya düştünüz"
    
    
def hareket(konum, komut):
    if komut.emir=='L' and konum.yon=='N':
        konum.yon='W'
    elif komut.emir=='L' and konum.yon=='W':
        konum.yon='S'
    elif komut.emir=='L' and konum.yon=='S':
        konum.yon='E'
    elif komut.emir=='L' and konum.yon=='E':
        konum.yon='N'
    elif komut.emir=='R' and konum.yon=='N':
        konum.yon='E'
    elif komut.emir=='R' and konum.yon=='E':
        konum.yon='S'
    elif komut.emir=='R' and konum.yon=='S':
        konum.yon='W'
    elif komut.emir=='R' and konum.yon=='W':
        konum.yon='N'
    elif komut.emir=='M' and konum.yon=='N':
        konum.y += 1
    elif komut.emir=='M' and konum.yon=='W':
        konum.x -= 1
    elif komut.emir=='M' and konum.yon=='S':
        konum.y -= 1
    elif komut.emir=='M' and konum.yon=='E':
        konum.x += 1
        
        
def okuma(dosya):               
    girdi=open(dosya)                #Belirtilen girdi dosyasının açılması sağlanır
    satirlar=girdi.readlines()       #Dosyanın satırları dizi halinde kaydedilir
    
    gboyut=satirlar[0]                   #Dosyanın ilk satırı dizi halinde kaydedilir    
    gezegen.genislik= int(gboyut[0])     #ilk satırın 0 ve 2 nolu karakterleri gezegenin genişlik
    gezegen.yukseklik= int(gboyut[2])    # ve yüksekliği olacağı için class gezegendeki genişlik ve yükseklikle eşleştirilir.
    
    arac=satirlar[1]                 
    konum.x=int(arac[0])            
    konum.y=int(arac[2])            #eşleştirmelerde int'e çevirme kullanılır çünkü text ten gelen her karakter string 
    konum.yon=arac[4]               # olarak gelir
    
    gorev=satirlar[2]                #gelen emir sayısında kısıtlama olmadığı için dizinin uzunluğu hesaplanır ve 
    for i in range(len(gorev)):     # for döngüsü ile çekilir
        komut.emir=gorev[i] 
        hareket(konum,komut)       # hareket fonksiyonunu for döngüsü içinde işleterek her komuttan sonra 
                                    # konumu güncelleyerek, for döngüsü bittiğinde en son duruma erişilir.
        kontrol(konum)
        
        
                      
        
okuma('girdi.txt')

print konum.x, konum.y, konum.yon







