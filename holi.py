import formulas

'''
def main():
    x=int(input("Escriba la base: "))
    y=int(input("Escriba la altura: "))

    a, p = formulas.area(x, y)

    print ("Area ", a)
    print("perimetro ", p)


def main():
    cad = formulas.leer_cadena()
    print ("El texto que ingresaste es: ", cad)
    
main()

x=int(input("ingresa la base"))
y=int(input("ingresa el exponente"))
def calcula_potencia(x, y):

   return formulas.potencia(x, y)

print (calcula_potencia(x, y))

x= int(input("Escribe un número: "))

if (x>10):
    print("El número ", x, " es mayor a 10!")
else:
    print("El número ", x, " es MENOR a 10!")
    print("Saludos")
    
a=int(input("Escriba un número del 1 al 7: "))
while (a>7):
    
    print("Error, vuelva a ejecutar e ingrese un valor del 1 al 7")
    a=int(input("Escriba un número del 1 al 7: "))
if(a==1):
    print("Domingo")
elif(a==2):
    print("Lunes")
elif(a==3):
    print("Martes")
elif(a==4):
    print("Miércoles")
elif(a==5):
    print("Jueves")
elif(a==6):
    print("Viernes")
else:
    print("Sábado")

x=int(input("ingrese la nota 1: "))
y=int(input("ingrese la nota 2: "))

if(x>=8 and y >=8):
    situacion="promovido"
elif(x>=4 and y>=4):
    situacion="Regular, debe rendir final"
else:
    situacion="Alumno libre"
print("Su calificación es: "+ situacion)'''

usuario=input("ingrese su usuario: ")
if (usuario.isdigit()):
    print("Su usuario consta solo de numeros")
elif(usuario.isalpha()):
    print("Su usuario consta solo de letras")
elif(usuario.isalnum()):
    print("Su usuario es alfanumerico")
else:
    print("Su usuario contiene caracteres incorrectos")