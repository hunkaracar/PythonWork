print("*****" + "stok_market" + "*****")



def menu():
    print("""
    1.stoklara olmayan ürünü ekle
    2.stoklara olan ürünü ekle
    3.stoktan ürün çıkar
    4.stokta ürün bilgi güncelle
    5.stok görüntüle\n\n""")
    
    stok_sec = int(input("lütfen işlem yapmak istediğiniz numarayı giriniz>>>"))
    stok_s = {101001:{'Telefon': {'Adet':5,'Alış fiyatı':1950,'Renk':'Siyah','Satış Fiyatı':1250,'İsim':'Samsung'}},
    101002:{'Telefon': {'Adet':2,'Alış fiyatı':2050,'Renk':'Mavi','Satış Fiyatı':1650,'İsim':'Redmi'}},
    201005:{'Bilgisayar': {'Adet':10,'Alış fiyatı':11000,'Renk':'Siyah','Satış Fiyatı':10050,'İsim':'Asus'}},
    301003:{'Televizyon': {'Adet':8,'Alış fiyatı':9000,'Renk':'Beyaz','Satış Fiyatı':5750,'İsim':'AIG'}},
    401004:{'Mikrodalga': {'Adet':4,'Alış fiyatı':3300,'Renk':'Siyah','Satış Fiyatı':1980,'İsim':'Bosch'}}}
    print("""
    1.Fırın=4000tl
    2.Çamaşır makinesi=7000tl
    3.Klima=5500tl
    4.Kahve Makinesi=1700tl\n\n\n""")

    if stok_sec == 1:
        def urun_ekle():
            new_urun = input("almak istediğiniz ürünün ismini giriniz:")

            if new_urun == "fırın":
                stok_s[301003] = {}
                stok_s[301003]["fırın"] = {}
                stok_s[301003]['Adet'] = 4
                stok_s[301003]['Alış fiyatı'] = 4000
                stok_s[301003]['Renk'] = "Beyaz"
                stok_s[301003]['Satış Fiyatı'] = 2200
                stok_s[301003]['İsim'] = "Vestel"

            if new_urun == "çamaşır makinesi":
                stok_s[301003] = {}
                stok_s[301003]["çamaşır makinesi"] = {}
                stok_s[301003]['Adet'] = 7
                stok_s[301003]['Alış fiyatı'] = 7000
                stok_s[301003]['Renk'] = "Açık beyaz"
                stok_s[301003]['Satış Fiyatı'] = 2000
                stok_s[301003]['İsim'] = "Beko"
            
            if new_urun == "klima":
                stok_s[301003] = {}
                stok_s[301003]["klima"] = {}
                stok_s[401004]['Adet'] = 8
                stok_s[401004]['Alış fiyatı'] = 5500
                stok_s[401004]['Renk'] = "Gri"
                stok_s[401004]['Satış fiyatı'] = 1800
                stok_s[401004]['İsim'] = "Baymak"

            if new_urun == "kahve makinesi":
                stok_s[301003] = {}
                stok_s[301003]["kahve makinesi"] = {}
                stok_s[301003]['Adet'] = 10
                stok_s[301003]['Alış fiyatı'] = 1700
                stok_s[301003]['Renk'] = "Siyah"
                stok_s[301003]['Satış fiyatı'] = 500
                stok_s[301003]['İsim'] = "Bosch"    

            else:
                print("Bilinmeyen işlem.")        

            print(stok_s)

        
        urun_ekle()
            
    if stok_sec == 2:
        def stok_urun_ekle():
            print("""
            1.Televizyon
            2.Bilgisayar
            3.Telefon
            4.Mikrodalga\n""")
            urun_cık = input("Çıkarmak istediğiniz ürünün ismini giriniz:")

            if urun_cık == "Televizyon":
                adet_s = int(input("Adet sayısını giriniz:"))
                alıs_f = int(input("Alış fiyatı Sayısını giriniz:"))
                satıs_f = int(input("Satış fiyatı giriniz:"))
                renk_g = input("Yeni rengi giriniz:")
                marka_g = input("Yeni marka giriniz:")
                guncel_stok = {'Adet':adet_s,'Alış fiyatı':alıs_f,'Renk':renk_g,'Satış Fiyatı':satıs_f,'İsim':marka_g}
                stok_s[301003].update(guncel_stok)     

                print(stok_s)
            
            if urun_cık == "Bilgisayar":
                 adet_s = int(input("Adet sayısını giriniz:"))
                 alıs_f = int(input("Alış fiyatı Sayısını giriniz:"))
                 satıs_f = int(input("Satış fiyatı giriniz:"))
                 renk_g = input("Yeni rengi giriniz:")
                 marka_g = input("Yeni marka giriniz:")
                 guncel_stok = {'Adet':adet_s,'Alış fiyatı':alıs_f,'Renk':renk_g,'Satış Fiyatı':satıs_f,'İsim':marka_g}
                 stok_s[201005].update(guncel_stok)     
            
                 print(stok_s)   

            if urun_cık == "Telefon":
                 adet_s = int(input("Adet sayısını giriniz:"))
                 alıs_f = int(input("Alış fiyatı Sayısını giriniz:"))
                 satıs_f = int(input("Satış fiyatı giriniz:"))
                 renk_g = input("Yeni rengi giriniz:")
                 marka_g = input("Yeni marka giriniz:")
                 guncel_stok = {'Adet':adet_s,'Alış fiyatı':alıs_f,'Renk':renk_g,'Satış Fiyatı':satıs_f,'İsim':marka_g}
                 stok_s[101001].update(guncel_stok)     

                 print(stok_s)    
               
            if urun_cık == "Mikrodalga":
                 adet_s = int(input("Adet sayısını giriniz:"))
                 alıs_f = int(input("Alış fiyatı Sayısını giriniz:"))
                 satıs_f = int(input("Satış fiyatı giriniz:"))
                 renk_g = input("Yeni rengi giriniz:")
                 marka_g = input("Yeni marka giriniz:")
                 guncel_stok = {'Adet':adet_s,'Alış fiyatı':alıs_f,'Renk':renk_g,'Satış Fiyatı':satıs_f,'İsim':marka_g}
                 stok_s[401004].update(guncel_stok)     

            
            print(stok_s)    

        stok_urun_ekle()

    if stok_sec == 3:
        def stok_urun_cıkar():
            print("""
            1.Televizyon
            2.Bilgisayar
            3.Telefon
            4.Mikrodalga\n""")
            urun_cık = input("Çıkarmak istediğiniz ürünün ismini giriniz:")

            if urun_cık == "Televizyon":
                new_val = stok_s[301003]['Televizyon']['Adet'] - 1
                guncel_stok = {'Adet':new_val}     
                stok_s[301003].update(guncel_stok)

                print(stok_s)
            
            if urun_cık == "Bilgisayar":
                 new_val = stok_s[201005]['Bilgisayar']['Adet'] - 1
                 guncel_stok = {'Adet':new_val}     
                 stok_s[201005].update(guncel_stok)
                
            
                 print(stok_s)

            if urun_cık == "Telefon":
                 new_val = stok_s[101001]['Telefon']['Adet'] - 1
                 guncel_stok = {'Adet':new_val}     
                 stok_s[101001].update(guncel_stok)

                 print(stok_s)
                
               
            if urun_cık == "Mikrodalga":
                 new_val = stok_s[401004]['Mikrodalga']['Adet'] - 1
                 guncel_stok = {'Adet':new_val}     
                 stok_s[401004].update(guncel_stok)
            
                 print(stok_s)    

        stok_urun_cıkar()

    
    if stok_sec == 4:
        print("Güncel stok durumu...")
        for i in stok_s.items():
            print(i)

    if stok_sec == 5:
        print("Stok görüntüleniyor...")
        for i in stok_s.items():
            print(i)



menu()