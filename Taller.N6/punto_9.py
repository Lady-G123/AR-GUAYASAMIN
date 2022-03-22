print("script interactivo de temperatura")

gc = float(input("¿cual es la temperatura de grados celcius?"))

gf = (gc * 9/5) + 32

gk = gc + 273.15

print("{} grados celcius son {} grados fahrenheit".format(gc,gf))
           
print("{} grados celcius son {} grados kelvin".format(gc,gk))
