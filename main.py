from clases import Estudiante,Profesor,Curso

# ----------------- BLOQUE PRINCIPAL -----------------

# ALUMNOS Y PROFESORES CARGADOS DE ARRANQUE:
estudiante1 = Estudiante("1000", 2023, "Lucas", "Ochoa", "lucasochoa@gmail.com", "1234")
Estudiante.estudiantes.append(estudiante1)
estudiante2 = Estudiante("1001", 2023, "Jorge", "Maslaton", "jorgemaslaton@gmail.com", "lolencio")
Estudiante.estudiantes.append(estudiante2)


profesor1 = Profesor("Ingeniero en Sistemas", 2017, "Abelardo", "Turbotomi", "turbotomi@gmail.com", "fuckencio")
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
            if email == e.email:
                if e.validar_credenciales(email, contrasenia) == True:
                    print("Verificado")
                    contrasenia_encontrada = True
                if contrasenia_encontrada == False:
                    "Error: contraseña incorrecta."
                email_encontrado = True
        if email_encontrado == False:
            print("El email ingresado no existe, debe darse de alta en Alumnado.")
            
            # -------------------SUB-MENU ALUMNOS ----------------#
        sub_opcion_alumno = 0
        while sub_opcion_alumno !=3:
            print("1. Matricularse a un curso")
            print("2. Ver curso")
            print("3. Volver al menú principal")
            sub_opcion_alumno = int(input("Selecciona una opción (1/2/3)"))
            if sub_opcion_alumno == 1:
                lista_cursos = Curso.cursos
                for curso in lista_cursos:
                    print(curso.nombre)
        
    elif opcion == 2:
        print("Usted está por ingresar como profesor")
        email = str(input("Ingrese el mail: "))
        contrasenia = str(input("Ingrese su contraseña: "))
        email_encontrado = False
        contrasenia_encontrada = False
        for p in Profesor.profesores:
            if email == p.email:
                if p.validar_credenciales(email, contrasenia) == True:
                    print("Verificado")
                    contrasenia_encontrada = True
                if contrasenia_encontrada == False:
                    "Error: contraseña incorrecta."
                email_encontrado = True
        if email_encontrado == False:
            print("El email ingresado no existe, debe darse de alta en Alumnado.")
        
         # -------------------SUB-MENU PROFESOR ----------------#
        sub_opcion_profesor = 0
        while sub_opcion_profesor != 3:
            print("1. Dictar curso")
            print("2. Ver curso")
            print("3. Volver al menú principal")
            sub_opcion_profesor = int(input("Selecciona una opción (1/2/3)"))
            if sub_opcion_profesor == 1:
                nuevo_curso = str(input("Ingrese el nombre del curso: "))
                nueva_contrasenia = Curso.generar_contrasenia()
                print(nueva_contrasenia)
                
                
                
                
                
                
                
    elif opcion == 3:
        print("Cursos disponibles:")
        lista_cursos_ordenada = sorted(Curso.cursos, key=lambda x: x.nombre)
        for curso in lista_cursos_ordenada:
            print("-"*10)
            print(f"Nombre: {curso.nombre}, Carrera: Tecnicatura Universitaria en Programación")
        
    else:
        print("Saliendo del sistema...")
        break