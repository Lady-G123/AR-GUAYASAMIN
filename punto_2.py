print("*************************************")
print("convertidor de unidades de tiempo")
print("*************************************")

horas = int(input("ingrese la cantidad de horas: "))
minutos = int(input("ingrese la cantidad de minutos: "))
segundos = int(input("ingrese la cantidad de segundos: "))

segundos += horas * 60 * 60
segundos += minutos * 60

print("la cantidad de segundos es igual a: {}".format(segundos))
