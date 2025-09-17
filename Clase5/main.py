"""
num=int(input("Introduce un numero (Del 1 al 11): "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
"""

""""
nombre=["ana", "juan", "pedro", "maria"]
for nombre in nombre:
    print(nombre.upper())
"""


"""carros = ["ford", "chevrolet", "fiat", "audi"]
print("Lista original:", carros)

nuevocarro = input("Introduce el nombre de un carro: ")
carros.append(nuevocarro)

print("Lista actualizada:")
for carro in carros:
    print(carro)
"""

"""
lista = ["Helado (0)", "Galletas (1)", "Chocolates (2)", "Dulces (3)"]
print("Lista original:")
print(lista)

for i in range(1):
    eliminar = input("Introduce el número del dulce que deseas eliminar (0, 1, 2 o 3): ")
    lista.pop(int(eliminar))
    print("Lista actualizada:")
    print(lista)
"""

"""
numeros=[1,2,3,4,5,6,7,8,9]
numeros.reverse()
for numero in range(1):
    print(f"La lista alrevez es: {numeros}")
"""
"""
contraseña=" "
contraseña=input("Pon la contraseña: ")
contador=1
while contraseña != "python" and contador <3:
    print("contraseña inccorecta, digite nuevamente:")
    contraseña=input("Introduce nuevamente la contraseña: ")
    contador += 1
if contraseña == "python":  
        print("Acceso concedido")
"""
"""
numeros =[1,2,3,4,5,7,8,9,10]
for numeros in numeros:
    print(f"Numero {numeros}")
"""
"""
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
i = 0
while i < len(numeros):
    print(numeros[i])
    i += 1
"""


