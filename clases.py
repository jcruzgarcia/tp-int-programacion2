from generadores import generar_contrasenia
from abc import ABC
import datetime

class Usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia
        
    def __str__(self) -> str:
       return f"Nombre: {self._nombre}, Apellido: {self._apellido}, Email: {self._email}"
    
    def get_nombre(self): #metodo protegido que retornará el atributo protegido _nombre
        return self._nombre
    
    def get_apellido(self): 
        return self._apellido
    
    def get_email(self): 
        return self._email
    
    def get_contrasenia(self):
        return self._contrasenia
    
    def validar_credenciales(self, email, contrasenia)-> bool:
        if self._email == email and self._contrasenia == contrasenia:
            return True
        else:
            return False


class Estudiante(Usuario):
    estudiantes = []
    def __init__(self, _legajo: int, _anio_inscripcion_carrera: int, nombre, apellido, email, contrasenia):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = _legajo
        self.__anio_inscripcion_carrera = _anio_inscripcion_carrera
        self._mis_cursos = []
    def __str__(self) -> str:
       return f"Legajo: {self.__legajo}, Año: {self.__anio_inscripcion_carrera}"
   
    def matricular_en_curso(self):
        lista_cursos = Curso.cursos
        for indice, curso in enumerate(lista_cursos):
            print(f"{indice + 1}. {curso.get_nombre()}")
        indice_curso = int(input("Ingrese el índice de un curso para matricularse: "))
        for indice, curso in enumerate(lista_cursos):
            if (indice + 1) == indice_curso:
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
        lista_cursos = Curso.cursos
        for indice, curso in enumerate(lista_cursos):
            print(f"{indice + 1}. {curso.get_nombre()}")
        indice_curso = int(input("Ingrese el índice de un curso para desmatricularse: "))
        for indice, curso in enumerate(lista_cursos):
            if (indice + 1) == indice_curso:
                if curso in self._mis_cursos:
                    self._mis_cursos.remove(curso)
                    print("Se ha desmatriculado con éxito del curso.")
                else:
                   print("El índice ingresado no pertenece a ningún curso.")
                            
    def get_legajo(self):
        return self.__legajo
    def get_anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera
    def get_mis_cursos(self):
        return self._mis_cursos
    
    
class Profesor(Usuario):
    profesores = []
    def __init__(self, _titulo: str, _anio_egreso: int, nombre, apellido, email, contrasenia):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = _titulo
        self.__anio_egreso = _anio_egreso
        self._mis_cursos = []
    def __str__(self) -> str:
        return f"Titulo: {self.__titulo}, Año Egreso: {self.__anio_egreso}"
    
    def dictar_curso(self):
        nuevo_curso = str(input("Ingrese el nombre del curso: "))
        nueva_contrasenia = generar_contrasenia(6)
        curso_creado = Curso(nuevo_curso, nueva_contrasenia) 
        Curso.cursos.append(curso_creado) 
        self._mis_cursos.append(curso_creado)
        print(f"Se ha creado el siguiente curso exitosamente.")
        print("Nombre: ", nuevo_curso)
        print("Contraseña: ", nueva_contrasenia)
        print("Código del curso:", curso_creado.get_codigo())
        
    def get_titulo(self):
        return self.__titulo
    def get_anio_egreso(self):
        return self.__anio_egreso
    def get_mis_cursos(self):
        return self._mis_cursos
    
    
class Curso():
    cursos = []
    __prox_cod = 1
    
    def __init__(self, __nombre: str, __contrasenia_matriculacion: str):
        self.__nombre = __nombre
        __codigo =Curso.__prox_cod
        self.__codigo = __codigo
        self.__contrasenia_matriculacion = __contrasenia_matriculacion
        Curso.__prox_cod += 1
        
    def __str__(self) -> str:
        return f"Codigo:{self.__codigo}, Nombre del curso: {self.__nombre}, Contraseña de matriculación: {self.__contrasenia_matriculacion}"

    @classmethod
    def __generar_contrasenia(cls):
        return cls.__generar_contrasenia(6)
    
    def nuevo_archivo(self):
        nombre = str(input("Ingresa el nombre del archivo:"))
        fecha = datetime.now()
        formato = str("pdf")
        nuevo_archivo = Archivo(nombre, fecha, formato)
        archivos = []               #REVISAR ----------------------------
        archivos.append(nuevo_archivo)
        
    def get_nombre(self):
        return self.__nombre
    def get_contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    def get_codigo(self):
        return self.__codigo
    
class Carrera():
    def __init__(self, __nombre: str, __cant_anios: int):
        self.__nombre = __nombre
        self.__cant_anios = __cant_anios
    def __str__(self) -> str:
        return f"Nombre del curso: {self.__nombre}, Duración: {self.__cant_anios} años"
    
    def get_cantidad_materias() -> int:
        pass                          #completar------------------------------------------------------
    def get_nombre(self):
        return self.__nombre
    def get_cant_anios(self):
        return self.__cant_anios
    
class Archivo():
    def __init__(self, __nombre: str, __fecha: datetime, __formato: str):
        self.__nombre = __nombre
        self.__fecha= __fecha
        self.__formato= __formato
    def __srt__(self):
        return f"Nombre del archivo: {self.__nombre}, Fecha: {self.__fecha}, Formato: {self.__formato}"    
    
    def get_nombre(self):
        return self.__nombre
    def get_fecha(self):
        return self.__fecha
    def get_formato(self):
        return self.__formato