import sys

# 1. Mayor de dos números ingresados por teclado (operador ternario)
def ejercicio_1():
    a = float(input("Ingresá el primer número: "))
    b = float(input("Ingresá el segundo número: "))
    mayor = a if a > b else b
    print(f"El mayor es: {mayor}")


# 2. Buscar una palabra en una lista ingresada por teclado (args + ternario)
# Uso: python programa.py palabra_a_buscar
def ejercicio_2():
    if len(sys.argv) < 2:
        print("Error: falta la palabra a buscar")
        return
    palabra = sys.argv[1]
    lista = input("Ingresá una lista de palabras separadas por espacios: ").split()
    resultado = "encontrada" if palabra in lista else "no encontrada"
    print(f"La palabra '{palabra}' fue {resultado}")


# 3. Determinar si un número es par o impar
def ejercicio_3():
    n = int(input("Ingresá un número entero: "))
    if n % 2 == 0:
        print(f"{n} es par")
    else:
        print(f"{n} es impar")


# 4. Promedio de una lista de números (args + ternario)
# Uso: python programa.py 4 8 15 16
def ejercicio_4():
    numeros = [float(x) for x in sys.argv[1:]]
    promedio = sum(numeros) / len(numeros) if numeros else 0
    print(f"El promedio es: {promedio}")


# 5. Mensaje de error si no se pasan suficientes argumentos
# Uso: python programa.py arg1 arg2
def ejercicio_5():
    if len(sys.argv) < 3:
        print("Error: no se pasaron suficientes argumentos (se requieren al menos 2)")
        sys.exit(1)
    print("Argumentos recibidos:", sys.argv[1:])


if __name__ == "__main__":
    ejercicio_1()
    # ejercicio_2()
    # ejercicio_3()
    # ejercicio_4()
    # ejercicio_5()