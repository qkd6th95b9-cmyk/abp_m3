from validaciones import validar_correo,validar_edad,validar_nombre,validar_rut

pacientes = []

def buscar_indice_por_rut(rut):
    for indice, paciente in enumerate(pacientes):
        if rut in paciente:
            return indice
    return -1

def obtener_paciente_por_rut(rut):
    # busco el indice del paciente que tenga el rut ingresado
    # retorno el diccionario con los datos del paciente 
    indice = buscar_indice_por_rut(rut)
    if indice == -1:
        return None
    return pacientes[indice][rut]

# CRUD (create-read-update-delete)
# Create
def crear_paciente():
    try:
        print("\n ==> Registrar datos del nuevo paciente\n")
        rut = pedir_dato("Ingrese el rut del paciente (con guión): ", validar_rut)
        nombre = pedir_dato("Ingrese el nombre: ",validar_nombre).strip()
        apellido = pedir_dato("Ingrese el apellido: ",validar_nombre).strip()        
        edad = pedir_dato("Ingrese la edad: ",validar_edad)
        email = pedir_dato("Ingrese el email: ",validar_correo).strip()
        nuevo_paciente = {
            rut:{
                "nombre":(nombre,apellido),
                "edad": edad,
                "email": email, 
            }
        }
        pacientes.append(nuevo_paciente)
    except ValueError as e:
        print(f"Error:{e}")
 # Mensaje de confirmación
    print(f'\nDatos de {nombre} {apellido} agregados exitosamente.')

# Read (by_id, all)
def listar_todos():
    print("\n== Listado de todos los pacientes registrados ==\n")
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    for _, paciente in enumerate(pacientes):
        rut = next(iter(paciente.keys()))
        datos = paciente[rut]
        print(f"Paciente con el rut: {rut}")
        print(f"Nombre completo: {datos['nombre'][0]} {datos['nombre'][1]}")
        print(f"Correo: {datos['email']}")
        print(f"Edad: {datos['edad']}")
        print("-" * 30)

def buscar_paciente():
    try:
        rut=validar_rut(input("==> Ingrese el rut del paciente a buscar: "))
        datos=obtener_paciente_por_rut(rut)
        
        if datos is None:
            print("El paciente no existe")
        else:
            print(f"\nPaciente con el rut: {rut}\n")
            print(f"Nombre: {datos["nombre"][0]}")
            print(f"Apellido: {datos["nombre"][1]}")
            print(f"Edad: {datos["edad"]}")
            print(f"Correo: {datos["email"]}")
    except ValueError as e:
        print(f"Error:{e}")

# Update
def editar_paciente():
    try:
        rut = validar_rut(input("\n==> Ingrese el rut del paciente a buscar: "))
        indice = buscar_indice_por_rut(rut)
        if indice == -1:
            print("No existe paciente con ese rut")
            return
        datos = pacientes[indice][rut]
        print("Deje en blanco para mantener el valor actual.")
        print(f"Nombre: {datos['nombre'][0]}")
        print(f"Apellido: {datos['nombre'][1]}")
        print(f"Edad: {datos['edad']}")
        print(f"Email: {datos['email']}\n")
        nuevo_nombre = input("Nuevo nombre: ")
        nuevo_apellido = input("Nuevo apellido: ")
        nueva_edad = input("Nueva edad: ")
        nuevo_correo = input("Nuevo email: ")

        if nuevo_nombre:
            nombre = validar_nombre(nuevo_nombre)
        else:
            nombre = datos["nombre"][0]

        if nuevo_apellido:
            apellido = validar_nombre(nuevo_apellido)
        else:
            apellido = datos["nombre"][1]
        
        datos["nombre"] = (nombre,apellido)

        if nuevo_correo:
            datos["email"] = validar_correo(nuevo_correo)
        if nueva_edad:
            datos["edad"] = validar_edad(nueva_edad)
    except ValueError as e:
        print(f"Error:{e}")


# Delete
def borrar_paciente():
    try:
        rut = validar_rut(input("Ingrese el rut del paciente a buscar: "))
        indice = buscar_indice_por_rut(rut)
        if indice == -1:
            print("No existe un paciente con ese rut")
            return
        confirm = input(f"Está seguro que quiere borrar al paciente con rut {rut}? (s/n): ").strip().lower()
        
        if confirm == "s":
            pacientes.pop(indice)
            print("Paciente eliminado")
        elif confirm == "n":
            print("Borrado cancelado")
        else:
            print("Opción no válida")

    except ValueError as e:
        print(f"Error:{e}")

def obtener_todos_pacientes():
    return pacientes

def cargar_todos_pacientes(nuevos_pacientes):
    global pacientes
    pacientes = list(nuevos_pacientes)

# Función genérica para pedir y validar datos
def pedir_dato(mensaje, funcion_validacion):
    # Solicita un dato al usuario y lo valida repetidamente hasta que sea correcto
    while True:
        try:
            valor = input(mensaje)
            # Intentamos validar el valor ingresado
            valor_validado = funcion_validacion(valor)
            return valor_validado  # Si es válido, lo devuelve y sale del bucle
        except ValueError as e:
            # Si la validación falla (raise ValueError), muestra el mensaje y repite
            print(f"Error: {e}. Intente de nuevo.")
