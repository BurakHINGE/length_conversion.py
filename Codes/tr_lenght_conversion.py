print("Programa Hoş Geldiniz!")
print("Bu programda km, hm, dam, m, dm, cm veya mm uzunluk birimlerini birbirine çevirebilirsiniz!")

while True: 

    ilk_secim = input("Mevcut birimizini yazınız:  ")
    ikinci_secim = input("Çevirmek istediğiniz birimi yazınız: ")
    ilk_miktar = int(input("Çevirmek istediğiniz miktarı yazınız: "))

    def conversion():
        km == 1
        km == hm*10 == dam*100 == m*1000 == dm*10000 == cm*100000 == mm*1000000

    if ilk_secim == "km":
        if ikinci_secim == "hm":
            print(f"{ilk_miktar}km = {ilk_miktar*10}hm")

        elif ikinci_secim == "dam":
            print(f"{ilk_miktar}km = {ilk_miktar*100}dam") 

        elif ikinci_secim == "m":
            print(f"{ilk_miktar}km = {ilk_miktar*1000}m")

        elif ikinci_secim == "dm":
            print(f"{ilk_miktar}km = {ilk_miktar*10000}dm")   

        elif ikinci_secim == "cm":
            print(f"{ilk_miktar}km = {ilk_miktar*100000}cm")

        elif ikinci_secim == "mm":
            print(f"{ilk_miktar}km = {ilk_miktar*1000000}mm")    

    elif ilk_secim == "hm":
        if ikinci_secim == "km":
            print(f"{ilk_miktar}hm = {ilk_miktar/10}hm")

        elif ikinci_secim == "dam":
            print(f"{ilk_miktar}hm = {ilk_miktar*10}dam") 

        elif ikinci_secim == "m":
            print(f"{ilk_miktar}hm = {ilk_miktar*100}m")

        elif ikinci_secim == "dm":
            print(f"{ilk_miktar}hm = {ilk_miktar*1000}dm")   

        elif ikinci_secim == "cm":
            print(f"{ilk_miktar}hm = {ilk_miktar*10000}cm")

        elif ikinci_secim == "mm":
            print(f"{ilk_miktar}hm = {ilk_miktar*100000}mm")

    elif ilk_secim == "dam":
        if ikinci_secim == "km":
            print(f"{ilk_miktar}dam = {ilk_miktar/100}hm")

        elif ikinci_secim == "hm":
            print(f"{ilk_miktar}dam = {ilk_miktar/10}dam") 

        elif ikinci_secim == "m":
            print(f"{ilk_miktar}dam = {ilk_miktar*10}m")

        elif ikinci_secim == "dm":
            print(f"{ilk_miktar}dam = {ilk_miktar*100}dm")   

        elif ikinci_secim == "cm":
            print(f"{ilk_miktar}dam = {ilk_miktar*1000}cm")

        elif ikinci_secim == "mm":
            print(f"{ilk_miktar}dam = {ilk_miktar*10000}mm")    

    elif ilk_secim == "m":
        if ikinci_secim == "km":
            print(f"{ilk_miktar}m = {ilk_miktar/1000}hm")

        elif ikinci_secim == "hm":
            print(f"{ilk_miktar}m = {ilk_miktar/100}dam") 

        elif ikinci_secim == "dam":
            print(f"{ilk_miktar}m = {ilk_miktar/10}m")

        elif ikinci_secim == "dm":
            print(f"{ilk_miktar}m = {ilk_miktar*10}dm")   

        elif ikinci_secim == "cm":
            print(f"{ilk_miktar}m = {ilk_miktar*100}cm")

        elif ikinci_secim == "mm":
            print(f"{ilk_miktar}m = {ilk_miktar*1000}mm")   

    elif ilk_secim == "dm":
        if ikinci_secim == "km":
            print(f"{ilk_miktar}dm = {ilk_miktar/10000}hm")

        elif ikinci_secim == "hm":
            print(f"{ilk_miktar}dm = {ilk_miktar/1000}dam") 

        elif ikinci_secim == "dam":
            print(f"{ilk_miktar}dm = {ilk_miktar/100}m")

        elif ikinci_secim == "m":
            print(f"{ilk_miktar}dm = {ilk_miktar/10}dm")   

        elif ikinci_secim == "cm":
            print(f"{ilk_miktar}dm = {ilk_miktar*10}cm")

        elif ikinci_secim == "mm":
            print(f"{ilk_miktar}dm = {ilk_miktar*100}mm") 

    elif ilk_secim == "cm":
        if ikinci_secim == "km":
            print(f"{ilk_miktar}cm = {ilk_miktar/100000}hm")

        elif ikinci_secim == "hm":
            print(f"{ilk_miktar}cm = {ilk_miktar/10000}dam") 

        elif ikinci_secim == "dam":
            print(f"{ilk_miktar}cm = {ilk_miktar/1000}m")

        elif ikinci_secim == "m":
            print(f"{ilk_miktar}cm = {ilk_miktar/100}dm")   

        elif ikinci_secim == "dm":
            print(f"{ilk_miktar}cm = {ilk_miktar/10}cm")

        elif ikinci_secim == "mm":
            print(f"{ilk_miktar}cm = {ilk_miktar*10}mm")

    elif ilk_secim == "mm":
        if ikinci_secim == "km":
            print(f"{ilk_miktar}mm = {ilk_miktar/1000000}hm")

        elif ikinci_secim == "hm":
            print(f"{ilk_miktar}mm = {ilk_miktar/100000}dam") 

        elif ikinci_secim == "dam":
            print(f"{ilk_miktar}mm = {ilk_miktar/10000}m")

        elif ikinci_secim == "m":
            print(f"{ilk_miktar}mm = {ilk_miktar/1000}dm")   

        elif ikinci_secim == "dm":
            print(f"{ilk_miktar}mm = {ilk_miktar/100}cm")

        elif ikinci_secim == "cm":
            print(f"{ilk_miktar}mm = {ilk_miktar/10}mm")
