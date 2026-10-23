## Ejercicio 1: ZeroDivisionError
try:
    a = float(input("Ingresá el primer número: "))
    b = float(input("Ingresá el segundo número: "))
    print(f"Resultado: {a / b}")
except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")

#  Ejercicio 2: TypeError
try:
    numero = 5
    cadena = "hola"
    resultado = numero + cadena
    print(resultado)
except TypeError:
    print("Error de tipo: no se puede sumar un número y una cadena.")

#Ejercicio 3: KeyError  
    persona = {"nombre": "Ana", "edad": 30}

try:
    print(persona["ciudad"])
except KeyError:
    print("Error: la clave 'ciudad' no existe en el diccionario.")

###Ejercicio 4: FileNotFoundError (y crear el archivo si no existe) 
nombre_archivo = "datos.txt"

try:
    with open(nombre_archivo, "r") as f:
        print(f.read())
except FileNotFoundError:
    print(f"Error: el archivo '{nombre_archivo}' no existe. Se creará uno nuevo.")
    with open(nombre_archivo, "w") as f:
        f.write("Archivo creado automáticamente.\n")
    print("Archivo creado correctamente.")

### Ejercicio 5: ZeroDivisionError y ValueError

try:
    a = float(input("Ingresá el primer número: "))
    b = float(input("Ingresá el segundo número: "))
    print(f"Resultado: {a / b}")
except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")
except ValueError:
    print("Error: ingresaste un valor que no es un número válido.")
finally:
    print("Fin del programa.")