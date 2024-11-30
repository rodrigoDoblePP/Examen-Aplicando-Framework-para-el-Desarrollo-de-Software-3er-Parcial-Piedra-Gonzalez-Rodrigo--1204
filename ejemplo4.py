print (" ")
print ("Piedra Gonzalez Rodrigo #1204")
print (" ")

# Definimos la clase Calculadora para realizar operaciones matemáticas
class Calculadora:
    # Método constructor __init__ que inicializa los números num1 y num2
    def __init__(self, num1, num2):
        self._num1 = num1  # Atributo para el primer número
        self._num2 = num2  # Atributo para el segundo número

    # Método para realizar la suma de los dos números
    def suma(self):
        resultado = self._num1 + self._num2  # Realiza la suma
        print(f"El resultado de la suma es: {self._num1} + {self._num2} = {resultado}")

    # Método para realizar la resta de los dos números
    def resta(self):
        resultado = self._num1 - self._num2  # Realiza la resta
        print(f"El resultado de la resta es: {self._num1} - {self._num2} = {resultado}")

    # Método para realizar la división de los dos números
    def division(self):
        if self._num2 != 0:  # Verifica si el divisor no es cero
            resultado = self._num1 / self._num2  # Realiza la división
            print(f"El resultado de la división es: {self._num1} / {self._num2} = {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")  # Mensaje de error si el divisor es cero

    # Método para realizar la multiplicación de los dos números
    def multiplicacion(self):
        resultado = self._num1 * self._num2  # Realiza la multiplicación
        print(f"El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}")

# Función para obtener la operación del usuario
def ejecutar_calculadora():
    try:
        # Pedir al usuario que ingrese los números
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        # Crear una instancia de la clase Calculadora
        operacion = Calculadora(num1, num2)

        # Menú para seleccionar la operación a realizar
        print("\nSelecciona la operación que deseas realizar:")
        print("1. Suma")
        print("2. Resta")
        print("3. División")
        print("4. Multiplicación")

        # Pedir al usuario que seleccione la operación
        opcion = int(input("Opción: "))

        if opcion == 1:
            operacion.suma()  # Llamar al método suma
        elif opcion == 2:
            operacion.resta()  # Llamar al método resta
        elif opcion == 3:
            operacion.division()  # Llamar al método division
        elif opcion == 4:
            operacion.multiplicacion()  # Llamar al método multiplicacion
        else:
            print("Opción no válida.")

    except ValueError:
        print("Por favor ingresa números válidos.")

# Ejecutar la calculadora
ejecutar_calculadora()
