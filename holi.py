import formulas

'''
def main():
    x=int(input("Escriba la base: "))
    y=int(input("Escriba la altura: "))

    a, p = formulas.area(x, y)

    print ("Area ", a)
    print("perimetro ", p)
'''

'''def main():
    cad = formulas.leer_cadena()
    print ("El texto que ingresaste es: ", cad)
    
main()'''

x=int(input("ingresa la base"))
y=int(input("ingresa el exponente"))
def calcula_potencia(x, y):
   return formulas.potencia(x, y)

print (calcula_potencia(x, y))
