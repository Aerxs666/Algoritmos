#Voy hacer una funcion de una receta de cocina 
"""
def preparar_cocina(nombre,pasos):
    print(f"Preparando{nombre}...")
    for pasos in pasos:
        print(f"{pasos}")
    print(f"{nombre} Listo!")

nombre_receta = "Torta de arroz"
pasos_receta = ["Mezclar ingredientes", "Hornear por 30 minutos", "Dejar enfriar"]
preparar_cocina(nombre_receta, pasos_receta)
"""
"""
Componentes de una funcion
Def: es la palabra clave para definir una funcion
nombre_funcion: Identificador unico
Parametros: datos que recibe
cuerpo: bloque de codigo que se ejecuta
return: devuelve
"""

"""
Ejemplo.
Ejemplo 1 funcion sin parametros
"""
#Funcion que saluda
"""
def saludar():
    print("Hola")
    print("Bienvenido al programa")
saludar()
"""
#funcion con parametros
"""
def saludar_personal(nombre,edad):
    print(f"Hola {nombre}")
    print(f"tienes {edad} años")
#Usar con diferentes datos
saludar_personal("Ricardo",20)
saludar_personal("Juan",80)
"""
#Funcion que calcula y devuelve resultado
"""
def sumar(a,b):
    resultado=a+b
    return resultado
#usar y guardar resultados
total=sumar(5,3)
print("la suma es: ",total)
"""
#Funciones integradas
"""
def decirtunombre():
    nombre=input("Cual es tu nombre?: ")
    print(f"Hola {nombre}")
decirtunombre()
"""
"""def preguntas():
    trabajo=input("A que te dedicas? ")
    salario=input("Cuanto es tu salario en dolar?: ")
    print(f"Con que eres {trabajo} y ganas {salario} $")
preguntas()
"""
#Funciones de modulos
"""
def calcular_salario(horas_trabajadas, pago_hora):
    salario = horas_trabajadas*pago_hora
    print(f"Tu salario mensual es: ${salario}")
calcular_salario(160, 25)
"""
def crear_personaje(nombre, clase, raza, nivel):
    print(f"Nombre: {nombre}")
    print(f"Clase: {clase}")
    print(f"Raza: {raza}")
    print(f"Nivel: {nivel}")
crear_personaje("Astuard","Hechizero","Elfo",99)