""" Realizar un programa que pida tus datos personales y mostrar en pantalla los datos solisitados """ 
# 1. Datos personales
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
DNI = input("Introduce tu número de dni: ")

print("\nDatos personales:")
print("Nombre:", nombre)
print("Apellido:", apellido)
print("DNI:", DNI)


# 2. Área y perímetro
opcion = input("¿Qué polígono desea calcular? (triángulo, cuadrado, círculo): ")

if opcion == "triángulo":
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    perimetro = base * 3
elif opcion == "cuadrado":
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = lado * lado
    perimetro = lado * 4
elif opcion == "círculo":
    radio = float(input("Ingrese el radio del círculo: "))
    area = 3.1416 * radio ** 2
    perimetro = 2 * 3.1416 * radio
else:
    print("Opción no válida.")
    area = 0
    perimetro = 0

print(f"El área del {opcion} es: {area}")
print(f"El perímetro del {opcion} es: {perimetro}")



# 3. Ingresos y gastos
ingreso_total = float(input("Ingrese el ingreso total del hogar: "))
gastos = []
while True:
    gasto = input("Ingrese un gasto (o 'fin' para terminar): ")
    if gasto.lower() == "fin":
        break
    gastos.append(float(gasto))

total_gastos = sum(gastos)
ahorro = ingreso_total - total_gastos

print(f"Total de gastos: {total_gastos}")
print(f"Ahorro: {ahorro}")



# 4. Registro de negocio
mayor_edad = input("¿Eres mayor de edad? (si/no): ")
tiene_ruc = input("¿Tienes RUC? (si/no): ")
tiene_nombre_comercial = input("¿Tienes un nombre comercial? (si/no): ")

if mayor_edad.lower() == "si" and tiene_ruc.lower() == "si" and tiene_nombre_comercial.lower() == "si":
    print("Estás apto para abrir un negocio.")
else:
    print("No estás apto para abrir un negocio.")
