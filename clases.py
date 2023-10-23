from generador_contra import contrasenia_aleatoria

class Usuario:
    def __init__(self, nombre, apellido, email, contrasenia):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasenia = contrasenia
    def __str__(self) -> str:
       return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}"
    def validar_credenciales(self, email, contrasenia)-> bool:
        if self.email == email and self.contrasenia == contrasenia:
            return True
        else:
            return False


class Estudiante(Usuario):
    estudiantes = []
    def __init__(self, legajo, anio_inscripcion_carrera, nombre, apellido, email, contrasenia):
        super().__init__(nombre, apellido, email, contrasenia)
        self.legajo = legajo
        self.anio_inscripcion_carrera = anio_inscripcion_carrera
    def __str__(self) -> str:
       return f"Legajo: {self.legajo}, Año: {self.anio_inscripcion_carrera}"
        
class Profesor(Usuario):
    profesores = []
    def __init__(self, titulo, anio_egreso, nombre, apellido, email, contrasenia):
        super().__init__(nombre, apellido, email, contrasenia)
        self.titulo = titulo
        self.anio_egreso = anio_egreso
    def __str__(self) -> str:
        return f"Titulo: {self.titulo}, Año Egreso: {self.anio_egreso}"
    
class Curso():
    cursos = []
    def __init__(self, nombre, contrasenia_matriculacion):
        self.nombre = nombre
        self.contrasenia_matriculacion = contrasenia_matriculacion
    def __str__(self) -> str:
        return f"Nombre del curso: {self.nombre}, Contraseña de matriculación: {self.contrasenia_matriculacion}"
    def generar_contrasenia():
        return contrasenia_aleatoria