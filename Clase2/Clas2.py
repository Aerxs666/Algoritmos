#La suma de dos numers
""""
a=2
b=3
suma = a + b
print("La suma es: ",suma)"""

#La resta de dos numerps
"""a=int(input("Pon un un numero : "))
b=int(input("Pon otro numero: "))
q=input("Que quieres hacer? dividir o restar o multiplicar?: ")
if q == "restar":
    resta = a-b
    print("La resta es: ",resta)
if q == "dividir":
    dividir = a/b
    print("La division es: ",dividir)
if q == "multiplicar":
    mult= a*b
    print("La multiplicacion es: ",mult)"""
#Algoritmo suma con entrada

"""a=int(input("Pon un numero: "))
b=int(input("Pon otro numero: "))
suma = a+b
print("La suma es: ",suma)"""

#Hacer 5 ejercicios medios de resta, division, suma y promedio de notas 

"""
numeros = input("Ingresa números separados por coma: ")
lista = [int(n) for n in numeros.split(",")]
suma = sum(lista)
print(f"La suma de los números es: {suma}")
"""

"""numeros = input("Ingresa números separados por coma: ")
lista = [int(n) for n in numeros.split(",")]
resta = lista[0]
for n in lista[1:]:
    resta -= n
print(f"El resultado de la resta progresiva es: {resta}")
"""
"""
a = float(input("Ingresa el dividendo: "))
b = float(input("Ingresa el divisor: "))

if b != 0:
    resultado = a / b
    print(f"{a} dividido por {b} es {resultado}")
else:
    print("Error: No se puede dividir por cero.")
"""


"""notas = input("Ingresa tus notas separadas por coma (0 a 5): ")
lista = [float(n) for n in notas.split(",") if 0 <= float(n) <= 5]
if lista:
    promedio = sum(lista) / len(lista)
    print(f"Tu promedio es: {round(promedio, 2)}")
else:
    print("No se ingresaron notas válidas.")
"""

""""
promedio = float(input("Ingresa tu promedio final: "))
if promedio >= 3.0:
    print("¡Aprobaste! ")
else:
    print("Reprobaste.  Sigue intentando.")"""