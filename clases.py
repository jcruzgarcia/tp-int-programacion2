from generador_contra import generar_contrasenia

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
    def __init__(self, _legajo, _anio_inscripcion_carrera, nombre, apellido, email, contrasenia):
        super().__init__(nombre, apellido, email, contrasenia)
        self._legajo = _legajo
        self._anio_inscripcion_carrera = _anio_inscripcion_carrera
        self._mis_cursos = []
    def __str__(self) -> str:
       return f"Legajo: {self.legajo}, Año: {self.anio_inscripcion_carrera}"
    def matricular_en_curso(self):
        lista_cursos = Curso.cursos
        for indice, curso in enumerate(lista_cursos):
            print(f"{indice + 1}. {curso._nombre}")
        indice_matriculacion_curso = int(input("Ingrese el índice de un curso para matricularse:"))
        for indice, curso in enumerate(lista_cursos):
            if (indice + 1) == indice_matriculacion_curso:
                if curso in self._mis_cursos:
                    print("Usted ya se encuentra matriculado en esta materia.")
                else:
                    while True:
                        contrasenia_ingresada = str(input("Ingrese la clave de matriculación: "))
                        if contrasenia_ingresada == curso.get_contrasenia_matriculacion():
                            self._mis_cursos.append(curso)
                            print("Se ha matriculado exitosamente.")
                            break
                        else:
                            print("Clave incorrecta.")
                        
    def desmatricular_curso(self):
        pass # Agregar codigo para la 2da entrega.
    def get_legajo(self):
        return self._legajo
    def get_anio_inscripcion_carrera(self):
        return self._anio_inscripcion_carrera
    def get_mis_cursos(self):
        return self._mis_cursos
    
    
class Profesor(Usuario):
    profesores = []
    def __init__(self, _titulo, _anio_egreso, nombre, apellido, email, contrasenia):
        super().__init__(nombre, apellido, email, contrasenia)
        self._titulo = _titulo
        self._anio_egreso = _anio_egreso
        self._mis_cursos = []
    def __str__(self) -> str:
        return f"Titulo: {self.titulo}, Año Egreso: {self.anio_egreso}"
    def dictar_curso(self):
        nuevo_curso = str(input("Ingrese el nombre del curso: "))
        nueva_contrasenia = generar_contrasenia(6)
        print(f"Se ha creado el siguiente curso exitosamente.")
        print("Nombre: ", nuevo_curso)
        print("Contraseña: ", nueva_contrasenia)
        curso_creado = Curso(nuevo_curso, nueva_contrasenia) # Creamos el objeto a partir de la clase Curso.
        Curso.cursos.append(curso_creado) # Guardamos el objeto en la lista cursos[] (no requerido por la consigna pero realizado con un fin de mayor prolijidad para tener todos los cursos dictados por todos los profesores en una misma lista.)
        self._mis_cursos.append(curso_creado) #Guardamos el objeto en la lista mis_cursos, propia de la clase Profesor (es decir, cada objeto de la clase profesor tendra su propia lista de cursos dictados).
    def get_titulo(self):
        return self._titulo
    def get_anio_egreso(self):
        return self._anio_egreso
    def get_mis_cursos(self):
        return self._mis_cursos
    
    
class Curso():
    cursos = []
    def __init__(self, _nombre, _contrasenia_matriculacion):
        self._nombre = _nombre
        self._contrasenia_matriculacion = _contrasenia_matriculacion
    def __str__(self) -> str:
        return f"Nombre del curso: {self._nombre}, Contraseña de matriculación: {self._contrasenia_matriculacion}"
    def generar_contrasenia():
        return generar_contrasenia(6)
    def get_nombre(self):
        return self._nombre
    def get_contrasenia_matriculacion(self):
        return self._contrasenia_matriculacion