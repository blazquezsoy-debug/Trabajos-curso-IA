def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

print("Calculadora básica")
print("1. Sumar")
print("2. Restar")

opcion = input("Elige una opción: ")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if opcion == "1":
    print("Resultado:", sumar(num1, num2))
elif opcion == "2":
    print("Resultado:", restar(num1, num2))
else:
    print("Opción no válida")


# -----------------------------
# Segunda parte: eval de operaciones
# -----------------------------

def calcular(operacion):
    try:
        resultado = eval(operacion)
        return resultado
    except Exception as e:
        return f"Error: {e}"

operaciones = [
    "2 + 2",
    "10 / 5",
    "3 * 7",
    "(8 - 3) * 2",
    "5 ** 3",
    "100 / (2 + 3)",
]

print("\nPruebas de la calculadora:\n")

for op in operaciones:
    print(f"{op} = {calcular(op)}")



