from clases import *
from funciones import registrar_profesor
# ----------------- BLOQUE PRINCIPAL -----------------

# ALUMNOS, PROFESORES Y ARCHIVOS CARGADOS DE ARRANQUE:
estudiante1 = Estudiante("1000", 2023, "Lucas", "Ochoa", "lucasochoa@gmail.com", "1234")
Estudiante.estudiantes.append(estudiante1)
estudiante2 = Estudiante("1001", 2023, "Jorge", "Maslaton", "jorgemaslaton@gmail.com", "asd")
Estudiante.estudiantes.append(estudiante2)


profesor1 = Profesor("Ingeniero en Sistemas", 2017, "Abelardo", "Varela", "turbotomi@gmail.com", "hola123")
Profesor.profesores.append(profesor1)
profesor2 = Profesor("Profesorado en Computacion", 2010, "Bryan", "Shelby", "lsrp@gmail.com", "piyicones")
Profesor.profesores.append(profesor2)

# -------------------MENU PRINCIPAL ----------------#

opcion = 0

while opcion != 4:
    print("Menú:")
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")

    opcion = int(input("Selecciona una opción (1/2/3/4): "))
    if opcion == 1:
        print("Usted está por ingresar como alumno")
        email = str(input("Ingrese el mail: "))
        contrasenia = str(input("Ingrese su contraseña: "))
        email_encontrado = False
        contrasenia_encontrada = False
        for e in Estudiante.estudiantes:
            if email == e._email:
                if e.validar_credenciales(email, contrasenia) == True:
                    print("Verificado")
                    contrasenia_encontrada = True
            # -------------------SUB-MENU ALUMNOS ----------------#
                    sub_opcion_alumno = 0
                    while sub_opcion_alumno !=4:
                        print("1. Matricularse a un curso")
                        print("2. Desmatricularse a un curso")
                        print("3. Ver curso")
                        print("4. Volver al menú principal")
                        sub_opcion_alumno = int(input("Selecciona una opción (1/2/3) \n"))
                        if sub_opcion_alumno == 1:
                            e.matricular_en_curso()
                        elif sub_opcion_alumno == 2:
                            e.desmatricular_curso()
                        elif sub_opcion_alumno == 3:    
                            for indice, curso in enumerate(e.get_mis_cursos()):
                                print(f"{indice + 1}. {curso.get_nombre()}") 
                            indice_curso = int(input("Ingrese el índice de un curso para ver sus archivos: "))
                            for indice, curso in enumerate(e.get_mis_cursos()):
                                if (indice + 1) == indice_curso:
                                    print(f"Nombre del curso:{curso.get_nombre()} \n Listado de archivos del curso: ")# aca faltaría llamar a la lista de archivos (de ese curso en especifico)
                                else:
                                    print("El índice ingresado no coincide con ningun curso.")
                        elif sub_opcion_alumno == 4:         
                            print("Volviendo al menú principal...")
                            break
                        else:
                            print("Ingrese una opción válida")
                if contrasenia_encontrada == False:
                    "Error: contraseña incorrecta."
                    email_encontrado = True
        if email_encontrado == False:
            print("El email ingresado no existe, debe darse de alta en Alumnado.")
            
        
    elif opcion == 2:
        print("Usted está por ingresar como profesor")
        _email = str(input("Ingrese el mail: "))
        _contrasenia = str(input("Ingrese su contraseña: "))
        email_encontrado = False
        contrasenia_encontrada = False
        for p in Profesor.profesores:
            if _email == p._email:
                if p.validar_credenciales(_email, _contrasenia) == True:
                    print("Verificado")
                    contrasenia_encontrada = True
                    # -------------------SUB-MENU PROFESOR ----------------#
                    sub_opcion_profesor = 0
                    while sub_opcion_profesor != 3:
                        print("1. Dictar curso")
                        print("2. Ver curso")
                        print("3. Volver al menú principal")
                        sub_opcion_profesor = int(input("Selecciona una opción (1/2/3) \n"))
                        if sub_opcion_profesor == 1:
                            p.dictar_curso()
                        elif sub_opcion_profesor == 2:
                            print(f"Listado de cursos dictados por {p._nombre}:")
                            for indice, c in enumerate(p.get_mis_cursos()):
                                print(f"{indice + 1}. {c.get_nombre()}")
                            indice_curso = int(input("Ingrese el índice de un curso para ver sus datos: "))
                            for indice, c in enumerate(p.get_mis_cursos()):
                                if (indice + 1) == indice_curso:
                                    if c in p.get_mis_cursos():
                                        print(f"Nombre del curso: {c.get_nombre()} \n Contraseña: {c.get_contrasenia_matriculacion()} \n Código: {c.get_codigo()} \n Cantidad de archivos:") #faltaria agregar llamada a cant de archivos
                                    #REVISAR ----------------------------
                                    while True:
                                        agregar_adjunto = int (input("¿Desea agregar un archivo adjunto? \n 1. Si \n 2.No"))
                                        if agregar_adjunto == 1:
                                            c.nuevo_archivo()
                                        elif agregar_adjunto == 2:
                                            break
                                        else:
                                            print("Seleccione una opción válida")
                        elif sub_opcion_profesor == 3:
                            print("Volviendo al menú principal...")
                            break
                        else:
                            print("Ingrese una opción válida")
                if contrasenia_encontrada == False:
                    "Error: contraseña incorrecta."
                email_encontrado = True
        if email_encontrado == False:
            print("El email ingresado no existe.")
            dar_alta = str(input("Ingrese la contraseña para darse de alta como profesor: "))   
            if dar_alta == "admin":
                registrar_profesor()
                print("Profesor registrado exitosamente.")
                
    elif opcion == 3:
        print("Cursos disponibles:")
        lista_cursos_ordenada = sorted(Curso.cursos, key=lambda x: x.get_nombre)
        for curso in lista_cursos_ordenada:
            print("-"*10)
            print(f"Nombre: {curso.get_nombre()}, Carrera: Tecnicatura Universitaria en Programación")
        
    else:
        print("Saliendo del sistema...")
        break