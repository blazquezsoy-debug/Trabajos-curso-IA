def calcular(operacion):
    try:
        resultado = eval(operacion)
        return resultado
    except Exception as e:
        return f"Error: {e}"

# Lista de operaciones a probar
operaciones = [
    "2 + 2",
    "10 / 5",
    "3 * 7",
    "(8 - 3) * 2",
    "5 ** 3",
    "100 / (2 + 3)",
]

print("Pruebas de la calculadora:\n")

for op in operaciones:
    print(f"{op} = {calcular(op)}")



