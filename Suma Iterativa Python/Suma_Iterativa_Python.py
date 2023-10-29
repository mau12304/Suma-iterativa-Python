

def suma_iterativa(n):
    suma = 0
    while n > 9:
        suma += n % 10
        n //= 10
    return suma + n

try:
    n = int(input("Ingresa un número entero: "))
    resultado = suma_iterativa(n)
    print(f"La suma de los dígitos de {n} es: {resultado}")
except ValueError:
    print("Entrada no