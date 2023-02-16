

def invertir():
    a=input("Ingrse el primer numero: ")
    b=input("Ingrse el segundo numero: ")

    lista = {a, b}
    lista =list(lista)
    lista[0], lista[1] = lista[1], lista[0]
    
    print("Los elementos ahora son ", lista[0]," y ",  lista[1])
    

invertir()