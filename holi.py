print ("hola")
print ('esto es una prueba')
nombre = "Ruth Isabel"
apellido= "Espinoza Herrera"
edad = 35
print ("Hola soy " + nombre + " " + apellido + " y tengo " + str(edad) + " años")
fav = 9
print ("numero favorito: " + str(fav))
num1 = 10
num2 = 6
result= num1*num2
print ("el resultado de " , num1,  " por ", num2,  " es " , result)


def invertir():
    a=input("Ingrse el primer numero: ")
    b=input("Ingrse el segundo numero: ")

    lista = {a, b}
    lista =list(lista)
    lista[0], lista[1] = lista[1], lista[0]
    
    print("Los elementos ahora son ", lista[0]," y ",  lista[1])
    

invertir()