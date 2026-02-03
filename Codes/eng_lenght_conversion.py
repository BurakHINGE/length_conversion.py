print("Welcome to the Program!")
print("In this program, you can convert length units such as km, hm, dam, m, dm, cm or mm into each other!")

while True: 

    first_choice = input("Enter the current unit: ")
    second_choice = input("Enter the unit you want to convert to: ")
    first_amount = int(input("Enter the amount you want to convert: "))

    def conversion():
        km == 1
        km == hm*10 == dam*100 == m*1000 == dm*10000 == cm*100000 == mm*1000000

    if first_choice == "km":
        if second_choice == "hm":
            print(f"{first_amount}km = {first_amount*10}hm")

        elif second_choice == "dam":
            print(f"{first_amount}km = {first_amount*100}dam") 

        elif second_choice == "m":
            print(f"{first_amount}km = {first_amount*1000}m")

        elif second_choice == "dm":
            print(f"{first_amount}km = {first_amount*10000}dm")   

        elif second_choice == "cm":
            print(f"{first_amount}km = {first_amount*100000}cm")

        elif second_choice == "mm":
            print(f"{first_amount}km = {first_amount*1000000}mm")    

    elif first_choice == "hm":
        if second_choice == "km":
            print(f"{first_amount}hm = {first_amount/10}km")

        elif second_choice == "dam":
            print(f"{first_amount}hm = {first_amount*10}dam") 

        elif second_choice == "m":
            print(f"{first_amount}hm = {first_amount*100}m")

        elif second_choice == "dm":
            print(f"{first_amount}hm = {first_amount*1000}dm")   

        elif second_choice == "cm":
            print(f"{first_amount}hm = {first_amount*10000}cm")

        elif second_choice == "mm":
            print(f"{first_amount}hm = {first_amount*100000}mm")

    elif first_choice == "dam":
        if second_choice == "km":
            print(f"{first_amount}dam = {first_amount/100}km")

        elif second_choice == "hm":
            print(f"{first_amount}dam = {first_amount/10}hm") 

        elif second_choice == "m":
            print(f"{first_amount}dam = {first_amount*10}m")

        elif second_choice == "dm":
            print(f"{first_amount}dam = {first_amount*100}dm")   

        elif second_choice == "cm":
            print(f"{first_amount}dam = {first_amount*1000}cm")

        elif second_choice == "mm":
            print(f"{first_amount}dam = {first_amount*10000}mm")    

    elif first_choice == "m":
        if second_choice == "km":
            print(f"{first_amount}m = {first_amount/1000}km")

        elif second_choice == "hm":
            print(f"{first_amount}m = {first_amount/100}hm") 

        elif second_choice == "dam":
            print(f"{first_amount}m = {first_amount/10}dam")

        elif second_choice == "dm":
            print(f"{first_amount}m = {first_amount*10}dm")   

        elif second_choice == "cm":
            print(f"{first_amount}m = {first_amount*100}cm")

        elif second_choice == "mm":
            print(f"{first_amount}m = {first_amount*1000}mm")   

    elif first_choice == "dm":
        if second_choice == "km":
            print(f"{first_amount}dm = {first_amount/10000}km")

        elif second_choice == "hm":
            print(f"{first_amount}dm = {first_amount/1000}hm") 

        elif second_choice == "dam":
            print(f"{first_amount}dm = {first_amount/100}dam")

        elif second_choice == "m":
            print(f"{first_amount}dm = {first_amount/10}m")   

        elif second_choice == "cm":
            print(f"{first_amount}dm = {first_amount*10}cm")

        elif second_choice == "mm":
            print(f"{first_amount}dm = {first_amount*100}mm") 

    elif first_choice == "cm":
        if second_choice == "km":
            print(f"{first_amount}cm = {first_amount/100000}km")

        elif second_choice == "hm":
            print(f"{first_amount}cm = {first_amount/10000}hm") 

        elif second_choice == "dam":
            print(f"{first_amount}cm = {first_amount/1000}dam")

        elif second_choice == "m":
            print(f"{first_amount}cm = {first_amount/100}m")   

        elif second_choice == "dm":
            print(f"{first_amount}cm = {first_amount/10}dm")

        elif second_choice == "mm":
            print(f"{first_amount}cm = {first_amount*10}mm")

    elif first_choice == "mm":
        if second_choice == "km":
            print(f"{first_amount}mm = {first_amount/1000000}km")

        elif second_choice == "hm":
            print(f"{first_amount}mm = {first_amount/100000}hm") 

        elif second_choice == "dam":
            print(f"{first_amount}mm = {first_amount/10000}dam")

        elif second_choice == "m":
            print(f"{first_amount}mm = {first_amount/1000}m")   

        elif second_choice == "dm":
            print(f"{first_amount}mm = {first_amount/100}dm")

        elif second_choice == "cm":
            print(f"{first_amount}mm = {first_amount/10}cm")
