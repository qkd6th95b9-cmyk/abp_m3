# Módulo validaciones.py

# validar nombre del paciente
def validar_nombre(nombre_input):
    nombre = nombre_input.strip().capitalize() # Quitar espacios de la entrada y asignar nuevo argumento a variable
    if len(nombre) < 2:             # Condicional if para evaluar la cantidad de letras mínimas
        raise ValueError("El nombre debe tener al menos 2 caracteres")
    if not nombre.isalpha():        # Condicional if para evaluar si la entrada son letras
        raise ValueError("El nombre debe contener solo letras")
    return nombre
    
# validar email del paciente
def validar_correo(email_input):
    email = email_input.strip()          
    if "@" not in email or "." not in email:
        raise ValueError("El correo debe contener '@'")
    return email

# validar edad del paciente
def validar_edad(edad_input):
    try:
        edad = int(edad_input) # int() elimina espacios automáticamente. No necesita strip()
    except ValueError:
        # Este error salta si ingresan letras, símbolos o puntos decimales
        raise ValueError("La edad debe ser un número entero (sin letras ni decimales)")
    # Una vez que sabemos que es un número, validamos el rango lógico
    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120")
    return edad

# validar rut del paciente
def validar_rut(rut_input):
    rut = rut_input.strip()

    # Dividimos el RUT por el guión, guardamos en la lista() partes_rut
    partes_rut = rut.split("-") 
    # Validar formato básico (presencia de guion y partes: el número y el dv)
    if len(partes_rut) != 2:
        raise ValueError("Formato de RUT inválido. Use el formato: 12345678-K")

    # Ahora que sabemos que hay 2 partes, las asignamos a variables (desempaquetado de secuencias o unpacking)
    numero, dv = partes_rut
    dv = dv.upper()

    # Validar que la primera parte sean solo números
    if not numero.isdigit():
        raise ValueError("La parte numérica del RUT debe contener sólo números")
    
    # Validar largo mínimo del RUT completo
    if len(numero) < 7:
        raise ValueError("El RUT debe contener al menos 8 caracteres")

    # Validar que el DV sea un número o la letra K
    if not (dv.isdigit() or dv == "K"):
        raise ValueError("El dígito verificador debe ser un número o la letra K")

    # Validar que el DV tenga largo 1 (evita casos como 12345678-KK)
    if len(dv) != 1:
        raise ValueError("El dígito verificador debe tener solo un carácter")
    
    return f"{numero}-{dv}"