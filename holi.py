import formulas


def main():
    x=int(input("Escriba la base: "))
    y=int(input("Escriba la altura: "))

    a, p = formulas.area(x, y)

    print ("Area ", a)
    print("perimetro ", p)

def llamadoacadena():
    cad = leer_cadena()
    print ("El texto ingresado es: ", cad)
    
main()
llamadoacadena()



