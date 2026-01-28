from typing import Protocol

class SolicitanteProtocol(Protocol):
    def solicitar_libro(self, titulo: str) -> str:
        '''Metodo que debe implementar cualquier solicitante'''
        ...

class Usuario:
    def __init__(self, name, cedula):
        self.name = name
        self.cedula = cedula
        self.libros_prestados = []
    
    def solicitar_libro(self, titulo):
        return f'La solicitud del libro {titulo} realizada'

class Estudiante(Usuario):
    def __init__(self, name, cedula, carrera):
        super().__init__(name, cedula)
        self.carrera = carrera
        self.limite_libros = 3


    def solicitar_libro(self, titulo):
        if len(self.libros_prestados) < self.limite_libros:
            self.libros_prestados.append(titulo)
            return f'Prestamo del libro {titulo} autorizado'
        else:
            return f'No puedes prestar mas libros, limite alcanzado: {self.limite_libros}'
        
    def devolver_libro(self, titulo):
        if titulo in self.libros_prestados:
            self.libros_prestados.remove(titulo)
            self.limite_libros -= 1
            return f'El libro {titulo} has sido devuelto'
        else:
            return f'este libro {titulo} no esta en su lista de libros prestados, devolucion rechazada'

class Profesor(Usuario):
    def __init__(self, name, cedula):
        super().__init__(name, cedula)
        self.limite_libros = None

    def solicitar_libro(self, titulo):
        self.libros_prestados.append(titulo)
        return f'Prestamo del libro {titulo} autorizado'
    

estudiante = Estudiante('Daniel', 1007328002, 'Software')
profesor = Profesor('Luis', 123445678)
estudiante1 = Estudiante('Omar', 1007328002, 'Sistemas')

usuarios = [estudiante, estudiante1, profesor]

for usuario in usuarios:
    print(usuario.solicitar_libro('Titulo de ejemplo'))

