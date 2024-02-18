import sys

def saludar():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    correo = input("Ingrese su correo: ")
    cursos = []
    while True:
        curso = input("Ingrese el nombre del curso o 'fin' para terminar: ")
        if curso.lower() == "fin":
            break
        notas = []
        while True:
            nota = input(f"Ingrese la nota del curso {curso} o 'fin' para terminar: ")
            if nota.lower() == "fin":
                break
            notas.append(float(nota))
        cursos.append({"nombre_curso": curso, "notas": notas})
    return {"nombre": nombre, "edad": edad, "correo": correo, "cursos": cursos}

def operacion_matematica():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación a realizar (+, -, *, /): ")
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        return num1 / num2
    else:
        print("Operación no válida")
        return None

def promedio_notas(lista_alumnos):
    notas_finales = []
    for alumno in lista_alumnos:
        promedio = sum(alumno["notas"]) / len(alumno["notas"])
        notas_finales.append(promedio)
    return notas_finales

def alumnos_aprobados(lista_alumnos):
    return [alumno for alumno in lista_alumnos if all(nota >= 4 for nota in alumno["notas"])]

def alumnos_desaprobados(lista_alumnos):
    return [alumno for alumno in lista_alumnos if any(nota < 4 for nota in alumno["notas"])]

def multiplos():
    n = 10**10
    step = int(input("Ingrese el step: "))
    lista_multiplos = [num for num in range(1, n, step) if num % 2 == 0 and num % 5 == 0 and num % 7 == 0]
    print(f"Tamaño de la lista de multiplos: {len(lista_multiplos)}")

def mayor_numero():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    return max(num1, num2)

def menu():
    lista_alumnos = []
    while True:
        print("\nMenu:")
        print("1. Saludar")
        print("2. Realizar una operación matemática")
        print("3. Agregar a lista un diccionario de alumno")
        print("4. Calcular promedio de notas")
        print("5. Mostrar listado de alumnos aprobados")
        print("6. Mostrar listado de alumnos desaprobados")
        print("7. Generar lista de multiplos")
        print("8. Calcular el mayor de 2 números")
        print("9. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            print(saludar())
        elif opcion == "2":
            print(operacion_matematica())
        elif opcion == "3":
            lista_alumnos.append(saludar())
        elif opcion == "4":
            print(promedio_notas(lista_alumnos))
        elif opcion == "5":
            print(alumnos_aprobados(lista_alumnos))
        elif opcion == "6":
            print(alumnos_desaprobados(lista_alumnos))
        elif opcion == "7":
            multiplos()
        elif opcion == "8":
            print(mayor_numero())
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")

menu()
