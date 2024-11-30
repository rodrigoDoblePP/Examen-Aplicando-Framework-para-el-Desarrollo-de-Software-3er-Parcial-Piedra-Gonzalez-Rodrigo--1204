print (" ")
print ("Piedra Gonzalez Rodrigo #1204")
print (" ")

class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre} \nNota: {self.nota}")

    def resultados(self):
        if self.nota >= 7:
            print("Has APROBADO felicidades ahora puedes descansar y pasar las festividades tranquilo")
        else:
            print("Has REPROBADO Diablo tendras que pasar el resto de diciembre recursando!")


estudiante1 = Estudiante("Jose Alejandro Gutierritoz ", 4)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2 = Estudiante("Rodrigo Piedra Alias Rorrin Pedorrin ", 10)
estudiante2.imprimir()
estudiante2.resultados()