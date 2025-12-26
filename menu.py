import crud
import archivos_csv

# Menú principal
def mostrar_menu():
    print("\n==== SISTEMA DE GESTION DE PACIENTES ====\n")
    print("1. Ingresar Paciente")
    print("2. Buscar Paciente")
    print("3. Editar Paciente")
    print("4. Borrar Paciente")
    print("5. Listar todos los pacientes")
    print("6. Guardar en CSV")
    print("7. Cargar en CSV")
    print("8. Agendar cita")
    print("9. Consultar cita")
    print("0. Salir\n")


# Programa Principal
def ejecutar_menu():
    # Flag para salir
    salir_programa = False
    while True:
        if salir_programa:
            print("\nHa salido del programa. ¡Hasta pronto!\n")
            break

        mostrar_menu()
        opcion = input("Ingrese una opción del menú: ")
        if opcion == '1':
            crud.crear_paciente()
            salir_programa = opcion_salir()
        elif opcion == '2':
            crud.buscar_paciente()
            salir_programa = opcion_salir()
        elif opcion == '3':
            crud.editar_paciente()
            salir_programa = opcion_salir()
        elif opcion == '4':
            crud.borrar_paciente()
            salir_programa = opcion_salir()
        elif opcion == '5':
            crud.listar_todos()
            salir_programa = opcion_salir()
        elif opcion == '6':
            archivos_csv.guardar_csv()
            salir_programa = opcion_salir()
        elif opcion == '7':
            archivos_csv.cargar_csv()
            salir_programa = opcion_salir()
        elif opcion == '8':
            crud.agendar_cita()
        elif opcion == '9':
            crud.consultar_cita()
        elif opcion == '0':
            print("\nHa salido exitosamente. ¡Hasta pronto!\n")
        else:
            print("\n !!! Opción inválida.\nPor favor, selecciona una opción válida (1-9 o 0 para salir).")


# Método 'opcion_salir'. Gestiona la opción de salir o volver al menú principal antes de mostrarlo.
def opcion_salir():
    # Inicio del ciclo while
    while True:
        # Declaración de variable 'respuesta'
        respuesta = input("\n ==> Volver al menú principal (m) - Salir (e): ").strip().lower()
        # Condicional if. Si la respuesta es 'm', sale del ciclo
        if respuesta == 'm':
            break
        # Condicional elif. Si la respuesta es 'e', devuelve True
        elif respuesta == 'e':
            return True
        # Condicional else. Valida si la opción ingresada no es correcta
        else:
            print(" !!! Opción inválida. Por favor, elija una opción válida.")