def area(x, y):
    ar=x*y
    peri=2*(x+y)
    return ar, peri

x=int(input("Escriba la base: "))
y=int(input("Escriba la altura: "))

a, p = area(x, y)

print ("Area ", a)
print("perimetro ", p)
