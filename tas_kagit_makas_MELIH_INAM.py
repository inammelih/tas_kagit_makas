import random
def tas_kagit_makas():
    print("TAS KAGIT MAKAS OYUNUNA HOSGELDIN !!!")
    print("\n")       
    print("Oyunun Kurallari:")
    print("---Tas: Makasi yener (cunku tas makasi kirar), ancak kagida yenilir (cunku kagit tasi sarar).")
    print("---Kagit: Tasi yener (cunku kagit tasi sarar), ancak makasa yenilir (cunku makas kagidi keser).")
    print("---Makas: Kagidi yener (cunku makas kagidi keser), ancak tasa yenilir (cunku tas makasi kirar).")
    print("\n")
    print("Oyunun Oynanisi:")
    print("---Oyuncu 'tas', 'kagit' , 'makas' ve 'cikis' seceneklerinden birini secer.('cikis' secegini secerse oyunun bitirilip bitirilmeyecegi sorulur.)")
    print("---Oyuncu 'tas', 'kagit' ve 'makas' seceneklerinin birini sectikten sonra bilgisayar da bu secenekler arasindan bir secenek secer ve round sonuclanir.")
    print("\n")
    print("Oyunun Sonu:")
    print("---Ilk 2 round galibiyetine ulasan takim oyunu kazanir ve oyuna devam edip etmeyecegi hakkinda soru sorulur. Eger bilgisayar da oynamayi kabul ederse yeni oyuna baslanir.")
    print("\n")
    print("Hadi Deneyelim!!! :)")
    print("\n")


    list=["tas","kagit","makas"]
    list2=["evet","hayir"]
    round = 1
    oyuncu_count=0
    bilgisayar_count=0




    while True:        
        oyuncunun_secimi=input("Degerlerden birini seciniz: tas, kagit, makas veya cikis? ")
        print("\n")
        bilgisayarin_secimi=list[random.randrange(0,3)]

        if oyuncunun_secimi=="tas":

            if bilgisayarin_secimi=="kagit":
                print("Bilgisayar kazandi")
                bilgisayar_count = bilgisayar_count + 1 
                print(f"{round}.round sonucu: Oyuncu - Bilgisayar: {oyuncu_count} - {bilgisayar_count}")
                print("\n")       
                round = round + 1 

            elif bilgisayarin_secimi=="makas":
                print("Oyuncu kazandi")
                oyuncu_count = oyuncu_count + 1
                print(f"{round}.round sonucu: Oyuncu - Bilgisayar: {oyuncu_count} - {bilgisayar_count}")
                print("\n")       
                round = round + 1      
  

            elif bilgisayarin_secimi=="tas":
                print("Berabere")              
                print(f"{round}.round sonucu: Oyuncu - Bilgisayar: {oyuncu_count} - {bilgisayar_count}")
                print("\n")            
                round = round + 1 


        elif oyuncunun_secimi=="kagit":

            if bilgisayarin_secimi=="tas":
                print("Oyuncu kazandi")
                oyuncu_count = oyuncu_count + 1
                print(f"{round}.round sonucu: Oyuncu - Bilgisayar: {oyuncu_count} - {bilgisayar_count}")
                print("\n")            
                round = round + 1   

            elif bilgisayarin_secimi=="kagit":
                print("Berabere")
                print(f"{round}.round sonucu: Oyuncu - Bilgisayar: {oyuncu_count} - {bilgisayar_count}")
                print("\n")            
                round = round + 1 

            elif bilgisayarin_secimi=="makas":
                print("Bilgisayar kazandi")
                bilgisayar_count = bilgisayar_count + 1 
                print(f"{round}.round sonucu: Oyuncu - Bilgisayar: {oyuncu_count} - {bilgisayar_count}")
                print("\n")            
                round = round + 1 

        elif oyuncunun_secimi == "makas":

            if bilgisayarin_secimi=="tas":
                print("Bilgisayar kazandi")
                bilgisayar_count = bilgisayar_count + 1 
                print(f"{round}.round sonucu: Oyuncu - Bilgisayar: {oyuncu_count} - {bilgisayar_count}")
                print("\n")            
                round = round + 1             

            elif bilgisayarin_secimi=="kagit":
                print("Oyuncu kazandi")
                oyuncu_count = oyuncu_count + 1
                print(f"{round}.round sonucu: Oyuncu - Bilgisayar: {oyuncu_count} - {bilgisayar_count}")
                print("\n")            
                round = round + 1
          

            elif bilgisayarin_secimi=="makas":
                print("Berabere")
                print(f"{round}.round sonucu: Oyuncu - Bilgisayar: {oyuncu_count} - {bilgisayar_count}")
                print("\n")             
                round = round + 1 

                
        elif oyuncunun_secimi=="cikis":

            if round==1:
                print("Daha oynamadik bile hemen kacacak misin? (evet/hayir)")
                cevap2=input()

                if cevap2=="evet":
                    print("gorusmek uzere :))")
                    break

                elif cevap2=="hayir":
                    print("hadi baslayalim")


            elif round !=1:
                print("Cikmak mi istiyorsun? (evet/hayir)")
                cevap2=input()

                if cevap2=="evet":
                    print("Gorusmek uzere :))")
                    break

                elif cevap2=="hayir":
                    print("Hadi devam edelim")
        
        else:
            print("Hatali deger girdiniz! Lutfen seceneklerden birini sectiginize emin olunuz!(buyuk, kucuk harf ve yazim hatalarina dikkat ediniz! :)")
            print("\n")
            
        if oyuncu_count == 2:
            print("Oyunu oyuncu kazandi!")
            print("\n")
            cevap = input("Oynamaya devam etmek istiyor musunuz? (evet/hayir) ")
            bilgisayarin_cevabi = list2[random.randrange(0,2)]

            while cevap not in list2:
                print("Hatali deger girdiniz! Lutfen 'evet' veya 'hayir' olarak yanit verin.")
                print("\n")
                cevap = input("Oynamaya devam etmek istiyor musunuz? (evet/hayir) ")
                
            print(f"Bilgisayar, sen devam etmek istiyor musun? {bilgisayarin_cevabi} ")
            print("\n")

            if cevap == "evet":

                if bilgisayarin_cevabi == "evet":
                    print("Hadi yeni oyun oynayalim!")
                    print("\n")
                    round = 1
                    oyuncu_count = 0
                    bilgisayar_count = 0

                elif bilgisayarin_cevabi == "hayir":
                    print("Bilgisayar oynamak istemiyor :'/")
                    print("Gorusmek uzere! :)")
                    break


            elif cevap == "hayir":
                print("Gorusmek uzere! :)")
                break


        elif bilgisayar_count == 2:
            print("Oyunu bilgisayar kazandi!")
            print("\n")
            cevap = input("Oynamaya devam etmek istiyor musunuz? (evet/hayir) ")
            bilgisayarin_cevabi = list2[random.randrange(0,2)]

            while cevap not in list2:
                print("Hatali deger girdiniz! Lutfen 'evet' veya 'hayir' olarak yanit verin.")
                cevap = input("Oynamaya devam etmek istiyor musunuz? (evet/hayir) ")

            print(f"Bilgisayar, sen devam etmek istiyor musun? {bilgisayarin_cevabi} ")
            print("\n")

            if cevap == "evet":

                if bilgisayarin_cevabi == "evet":
                    print("Hadi yeni oyun oynayalim!")
                    print("\n")
                    round = 1
                    oyuncu_count = 0
                    bilgisayar_count = 0

                elif bilgisayarin_cevabi == "hayir":
                    print("Bilgisayar oynamak istemiyor :'/")
                    print("Gorusmek uzere! :)")
                    break


            elif cevap == "hayir":
                print("Gorusmek uzere! :)")
                break

            
tas_kagit_makas()