año = int(input("ingrese el año: "))
if año % 4 == 0:
    if año % 100 != 0:
        print("el año es bisiesto")
    else:
        if año % 400 == 0:
            print("el año es bisiesto")
        else:
            print("es un año comun")

else:
    print("es un año comun")
