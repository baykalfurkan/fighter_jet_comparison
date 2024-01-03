# -*- coding: utf-8 -*-

import random

nesil5   = ['F-35','F-22','Su-57','J-20','MiG-35','J-31']
nesil4_5 = ['F-18E','F-18F','Su-30','Su-33','Su-35','JAS 39','Dassault Rafale','F-15K']
nesil4   = ['Mitsubishi F-2','Panavia Tornado','Yak-38','AV-8B Harrier II','F-16','F-15','F-18','Su-27','MiG-29','JAS 39','Eurofighter Typhoon','J-10','JF-17','F-14','Mirage 2000','MiG-31']
nesil3   = ['F-4','MiG-23','F-5','MiG-25','Su-15','Su-17','Su-20','Su-22','Tu-28','Yak-28','Dassault Mirage F1','J8',"Saab 35",'MiG-21']
nesil2   = ['F-100','F-101','F-102','F-104','F-105','F-106','F-8','F-11','MiG-19','Su-9','Su-11','Yak-25']
nesil1   = ['Me 262','He 162','Me 162','Gloster Meteor','F-86','F-89','F-94','FH-1','MiG-15','MiG-17','La-15','Yak-15','Yak-170','Yak-23','J21R','J29','Saab 32','CF-100']

liste = [nesil5 , nesil4_5 , nesil4 , nesil3 , nesil2 , nesil1 ]   

print("* Savas ucagi karsilastirma yazilimina hosgeldiniz. * \n* Listeden iki ucagi secerek karsilastirabilirsin. *\n* ( Karsilastirmalar ucak ozelliklerine gore yapilmistir! ) *\n \nUcaklar;")

# Listeleleri karistirma
tum_elemanlar = []
for listeq in liste:
    tum_elemanlar.extend(listeq)

random.shuffle(tum_elemanlar)

eleman_sayisi = 0
for eleman in tum_elemanlar:
    print(eleman, end='  /  ')
    eleman_sayisi += 1
    if eleman_sayisi == 7:
        print()  
        eleman_sayisi = 0

if eleman_sayisi > 0:
    print()


def karsilastirma (ucak1,ucak2):
        ucak1n = next((nesiller[nesil] for nesil in nesiller if ucak1 in nesil), None)
        ucak2n = next((nesiller[nesil] for nesil in nesiller if ucak2 in nesil), None)
         
        if ucak1n == None or ucak2n == None:
            print("\nHatali deger girdiniz! \n--------------------------------------------------")        
        elif ucak1n == ucak2n:
           print("\n>> Sonuc: Ucaklarin ozellikleri benzer , pilota bagli << \n---------------------------------------------------------------------------------------------")
        elif ucak1n > ucak2n:
           if secim == "2":
               print("\n>> Kazandiniz! ")
           print("\n>> Sonuc: {} kazanir <<\n---------------------------------------------------------------------------------------------".format(ucak1))
        elif ucak1n < ucak2n:
           if secim == "2":
               print("\n>> Kaybettiniz! ")
           print("\n>> Sonuc: {} kazanir << \n---------------------------------------------------------------------------------------------".format(ucak2))
        else:
            print("\nHatali deger girdiniz! \n--------------------------------------------------")    


#Dongu
secim = 0
while True:
    
    nesiller = {
    tuple(nesil5): 5,
    tuple(nesil4_5): 4.5,
    tuple(nesil4): 4,
    tuple(nesil3): 3,
    tuple(nesil2): 2,
    tuple(nesil1): 1
    }
    

    #Kullanicinin sectigi ucagýn neslini atama islemi
    if secim == 0 or secim =="":
        print("\n")
        ucak1 = str(input("Birinci ucak: "))
        ucak2 = str(input("Ikinci ucak: "))
        karsilastirma(ucak1,ucak2)
                 

    #Rastgele ucak secip neslini atama islemi
    if secim == "1":
        print("---------------------------------------------------------------------------------------------\nRastgele seciliyor..\n")
        b = random.randrange(0,6)      
        c = random.randrange(0,6) 
        d = random.randrange(0,17) 
        e = random.randrange(0,17) 

        r_ucak1n = liste[b]
        r_ucak2n = liste[c]
        while True:
            if not d >= len(r_ucak1n):
                break
            else:
                d = random.randrange(0,17) 
        while True:
            if not e >= len(r_ucak2n) and e != d:
                break     
            else:
                e = random.randrange(0,17) 
        print("Secilen birinci ucak: {} ".format(r_ucak1n[d]))
        print("Secilen ikinci ucak: {} ".format(r_ucak2n[e]))
        t = r_ucak1n[d]
        k = r_ucak2n[e]
        karsilastirma(t,k) 
        
    #Pc ile vs
    if secim == "2":
       k_ucaklari = [1,2,3]
       pc_ucaklari = [1,2,3]
       
       f = 0
       for a in range(0,3):
           x = tum_elemanlar[random.randrange(0,74)]
           k_ucaklari[f] = x     
           f += 1
         
       f = 0
       for a in range(0,3):
           x = tum_elemanlar[random.randrange(0,74)]
           pc_ucaklari[f] = x     
           f += 1
         
       print("---------------------------------------------------------------------------------------------\n")    
       print("Secim yapacaginiz liste : {}".format(k_ucaklari))
       print("\nBilgisayarin sececegi liste : {}".format(pc_ucaklari))
       k_secim = input("\nListeden bir ucak seciniz : ")
       pc_secim = pc_ucaklari[random.randrange(0,3)]
       print("Bilgisayarin secimi : {}".format(pc_secim))
       karsilastirma(k_secim,pc_secim) 
       
    #Guclu ucagi tahmin etme oyunu 
    if secim == "3":
        k_skor = 0
        c_soru = 0
        while True:

            if c_soru == 0:
                print("---------------------------------------------------------------------------------------------\nGuclu ucagi tahmin etme oyunu \n") 
            z_secim = input("Zorluk seviyesi seciniz. Kolay(K) ,Orta(O) ,Zor(Z). \n(Cikis yapmak icin farkli bir deger giriniz) : ")
            if z_secim != "K"  and z_secim != "O" and z_secim != "Z":
                print("Cikis yapiliyor...\n--------------------------------------------------------------------------------------------\n")
                break
            
            s_liste = []
            
            while True:
              s_secim = int(input("Liste uzunlugunu seciniz. (min 4 ,maks 12) : "))
              if s_secim > 3 and s_secim < 13:
                  break
              else:
                  print("\nYanlis deger girdiniz! Araligin icinden bir deger seciniz. \n")
              
            if z_secim == "K":
                listek = [nesil2 ,nesil4]
                tum_elemanlar1 = []
                for listeq in listek:
                   tum_elemanlar1.extend(listeq)


            elif z_secim == "O":  
                listeo = [nesil3 ,nesil4]
                tum_elemanlar1 = []
                for listeq in listeo:
                   tum_elemanlar1.extend(listeq)


            elif z_secim == "Z": 
                listez = [nesil1 ,nesil2]
                tum_elemanlar1 = []
                for listeq in listez:
                   tum_elemanlar1.extend(listeq)

            else:
                print("Hatali deger girdiniz!")
                
                
            random.shuffle(tum_elemanlar1)
            s_liste = tum_elemanlar1[:s_secim-1]
            if z_secim == "K":
                s_liste.append(nesil5[random.randrange(0,len(nesil5))])

            elif z_secim == "O":
                s_liste.append(nesil4_5[random.randrange(0,len(nesil4_5))])
        
            elif z_secim == "Z":
                s_liste.append(nesil3[random.randrange(0,len(nesil3))])
        

            random.shuffle(s_liste)
            print("\n")
            print(s_liste)    
            s_ucak = input("Secilen ucak :   ")
            if s_ucak not in s_liste:
                print("\nHatali deger girdiniz! \n \nSkorunuz: {} / Yanitladiginiz soru: {} <<\n---------------------------------------------------------------------------------------------".format(k_skor,c_soru))
                break
            
            s_ucakn = next((nesiller[nesil] for nesil in nesiller if s_ucak in nesil), None)

            c = 0
            cevap = 0
            for sayi in s_liste: 
                b = next((nesiller[nesil] for nesil in nesiller if s_liste[c] in nesil), None)

                if s_ucakn < b:
                    cevap = b
                c += 1
    
            if s_ucakn > cevap:
               print(">> Dogru secim. <<\n")
               if z_secim == "K":
                   k_skor += 1
                   c_soru += 1
                     
               if z_secim == "O":
                   k_skor += 2
                   c_soru += 1
                    
               if z_secim == "Z":
                   k_skor += 3
                   c_soru += 1
                   
               if s_secim > 3 and s_secim < 7:
                   k_skor += 1
                     
               if s_secim > 6 and s_secim < 9:
                   k_skor += 3
                    
               if s_secim > 8 and s_secim < 13:
                   k_skor += 5
                    
            else:
                print("\n>> Yanlis secim. << \n \nSkorunuz: {} / Yanitladiginiz soru: {} ".format(k_skor,c_soru))
                k_skor = 0
                c_soru = 0

    #dongude kalabilmesi icin secim yapilir
    secim = input("\n>> Farkli bir karsilastirma icin       'ENTER' ;\n>> Rastgele karsilastirma yapmak icin    '1' ;\n>> Pc ile vs icin                        '2' ;\n>> Guclu ucagi tahmin etme oyunu icin    '3' giriniz.\nSeciminiz : ")
    if secim == "":
            print("\n\n\n---------------------------------------------------------------------------------------------\nDevam ediliyor..\n\nUcaklar;")
            eleman_sayisi = 0
            for eleman in tum_elemanlar:
                print(eleman, end='  /  ')
                eleman_sayisi += 1
                if eleman_sayisi == 7:
                    print()  
                    eleman_sayisi = 0

            if eleman_sayisi > 0:
                print()  
            
