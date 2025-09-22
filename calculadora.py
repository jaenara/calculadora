# Funciones matemáticas
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

# Calculadora con manejo de errores
def calculadora():
    try:
        a = float(input("Primer número: "))
        operacion = input("Elige operación: Suma: +, Resta: - , Multiplicacion: * , Division: / ): ")
        b = float(input("Segundo número: "))
       

        if operacion == '+':
            resultado = sumar(a, b)
        elif operacion == '-':
            resultado = restar(a, b)
        elif operacion == '*':
            resultado = multiplicar(a, b)
        elif operacion == '/':
            resultado = dividir(a, b)
        else:
            print("Operación inválida")
            return

        print(f"Resultado: {resultado}")

    except ValueError as e:
        print(f"Error: {e}")

# Llamamos a la función principal
calculadora()
