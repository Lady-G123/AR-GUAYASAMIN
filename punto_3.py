print("***************")
print("número mayor")
print("***************")

numero_1 = int(input("ingrese el primer numero:"))
numero_2 = int(input("ingrese el segundo numero:"))
numero_3 = int(input("ingrese el tercer numero:"))

if numero_1 > numero_2 and numero_1 > numero_3:
    print("el numero ", numero_1," es el numero mayor de los tres.")
else:
   if numero_2 > numero_1 and numero_2 > numero_3:
       print("el numero ", numero_2," es el numero mayor de los tres.")
       
   if numero_3 > numero_1 and numero_3 > numero_2:
       print("el numero ", numero_3," es el numero mayor de los tres.")
               
