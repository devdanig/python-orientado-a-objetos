# Definir nuestra primera clase 
# Class primera mayuscula
# 2 clases mas y crear lista catalogo que permitea usar for para hacer print de todos los libros

class Libro:
    def __init__(self, name, author, sbn, disponible=True):
        self.name = name
        self.author = author
        self.sbn = sbn
        self.disponible = disponible
        self.__prestamos = 0

    def __str__(self):
        return f'Libro: {self.name} por {self.author} disponible: {self.disponible}'
    
    def prestar_libro(self):
        if self.disponible:
            self.disponible = False
            self.__prestamos += 1
            return f'Libro {self.name} prestado. Total prestamos {self.__prestamos}'
        return f'Libro {self.name} no disponible'

    def devolver_libro(self):
        self.disponible = True
        return f'Libro {self.name} devuelto bien ahi'
    
    def famoso(self):
        return self.__prestamos > 5
    
    def get_prestamos(self):
        return self.__prestamos
    
    def set_prestamos(self, veces):
        self.__prestamos = veces

mi_libro = Libro('Roba coomo un artista', 'Austin Kleon', 12345, True)
otro_libro = Libro('El principito', 'No se', 23456, False)

print(mi_libro.prestar_libro())
print(mi_libro.devolver_libro())
print(mi_libro.prestar_libro())
print(mi_libro.get_prestamos())

catalogo = [mi_libro, otro_libro]

for i in catalogo:
    print(i)