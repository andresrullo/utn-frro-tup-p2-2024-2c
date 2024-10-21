#01) Crear la clase Persona con los métodos “set_nombre”, 
# “set_edad”, “get_nombre”, “get_edad” y “print_persona”. 
# Luego crear dos objetos del tipo Persona e imprimirlos por consola

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return "Nombre: {}. Edad: {}". format(self.nombre, self.edad)

    def set_nombre(self, nombre):
        self.nombre= nombre
    def set_edad(self, edad):
        self.edad= edad
    
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad

    def print_persona(self):
        print(self)

persona1 = Persona("Aylen", 37)
persona2 = Persona("Andres", 29)

print(persona1)
persona2.print_persona()