from clases import Profesor

def registrar_profesor():
    nombre = str(input("Ingrese el nombre del nuevo profesor a registrar: "))
    apellido = str(input("Ingrese el apellido del nuevo profesor: "))
    email = str(input("Ingrese el email: "))
    contrasenia = str(input("Ingrese la contrasenia: "))
    titulo = str(input("Ingrese el título que posee: "))
    anio_egreso = str(input("Ingrese el año de egreso: "))
    nuevo_profesor = Profesor(titulo,anio_egreso,nombre,apellido,email,contrasenia)
    Profesor.profesores.append(nuevo_profesor)
    
    
        