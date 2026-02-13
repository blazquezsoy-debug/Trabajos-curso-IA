🧮 Calculadora Básica en Python
Este proyecto implementa una calculadora básica en Python que permite realizar operaciones matemáticas simples: sumar, restar, multiplicar y dividir.
Además, incluye un conjunto de tests unitarios utilizando el módulo estándar unittest para validar el correcto funcionamiento de cada operación.

📁 Estructura del proyecto
Código
calculadora/
│
├── src/
│   ├── operaciones.py
│   └── main.py
│
├── tests/
│   └── test_operaciones.py
│
└── README.md
📌 Funcionalidades
La calculadora permite realizar:

Suma

Resta

Multiplicación

División (con manejo de error al dividir entre cero)

📄 Contenido de los archivos
operaciones.py
Contiene las funciones matemáticas:

python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
main.py
Interfaz simple por consola:

python
from operaciones import sumar, restar, multiplicar, dividir

print("Calculadora básica")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Elige una opción: ")

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if opcion == "1":
    print("Resultado:", sumar(num1, num2))
elif opcion == "2":
    print("Resultado:", restar(num1, num2))
elif opcion == "3":
    print("Resultado:", multiplicar(num1, num2))
elif opcion == "4":
    try:
        print("Resultado:", dividir(num1, num2))
    except ValueError as e:
        print("Error:", e)
else:
    print("Opción no válida")
test_operaciones.py
Tests unitarios con unittest:

python
import unittest
from src.operaciones import sumar, restar, multiplicar, dividir

class TestOperaciones(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_restar(self):
        self.assertEqual(restar(5, 2), 3)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(4, 3), 12)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

if __name__ == "__main__":
    unittest.main()
▶️ Cómo ejecutar el programa
Desde la carpeta src:

Código
python main.py
🧪 Cómo ejecutar los tests
Desde la raíz del proyecto:

Código
python -m unittest discover