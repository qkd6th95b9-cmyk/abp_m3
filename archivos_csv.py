import crud

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
archivo_csv = BASE_DIR / "documentos/pacientes.csv"

def guardar_csv(archivo = archivo_csv):
    pacientes = crud.obtener_todos_pacientes()
    if not pacientes:
        print("No hay pacientes para guardar.")
        return
    try:
        with open(archivo,"w",encoding = 'utf-8') as f:
            f.write("RUT;nombre;apellido;edad;email\n") # Escribir encabezado
            for paciente in pacientes:
                rut = next(iter(paciente.keys()))
                datos = paciente[rut]
                f.write(f"{rut};{datos['nombre'][0]};{datos['nombre'][1]};{datos['edad']};{datos['email']};\n")
        print("Guardado el archivo con éxito")
    except OSError as e:
        print(f"Error al escribir el archivo: {e}")
    
# Escritura del Archivo
def cargar_csv(archivo = archivo_csv):
    nuevas = []
    try:
        with open(archivo, "r", encoding = 'utf-8') as f:
            lineas = f.readlines()
            if not lineas:
                print("Archivo vacío!")
                return
            # Omitir el encabezado (primera línea)
            for linea in lineas[1:]:
                linea = linea.strip()
                if not linea:
                    continue # Omitir líneas vacías
                
                try:
                    rut, nombre, apellido, edad_str, email = linea.split(";")
                    edad = int(edad_str) # Convertir edad a entero
                    
                    # podrían existir validaciones de todos los campos antes de crear un registro
                    nuevas.append({rut:{"nombre": (nombre, apellido),
                                        "edad": edad,
                                        "email": email}})
                except ValueError:
                    print(f"Omitiendo línea con formato incorrecto: {linea}")
                    continue

        crud.cargar_todos_pacientes(nuevas)
        print("El archivo fue cargado exitosamente!")
    except FileNotFoundError:
        print("El archivo no existe!")

    except OSError as e:
        print(f"Error al leer el archivo: {e}")
