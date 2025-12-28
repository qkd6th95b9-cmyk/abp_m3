# Documentación Técnica: Sistema de Gestión de Usuarios

## Descripción General. 
El objetivo principal de este proyecto es diseñar e implementar un sistema de gestión basado en Python aplicando los conocimientos adquiridos en el módulo de Introdcción a Python del Bootcamp Full Stack Python del programa Talento Digital de Sence.  
Este proyecto es una aplicación de consola desarrollada en Python, diseñada para gestionar registros de usuarios (pacientes).  
El sistema permite realizar operaciones __CRUD__ (Crear, Leer, Actualizar, Borrar) y garantiza la persistencia de datos mediante archivos CSV.


## 📋 Especificaciones del Proyecto.
| Especificación | Detalle        
|----------------|----------------
| Lenguaje       | Python 3.13.7  
| Persistencia   | CSV (Comma Separated Values)
| Arquitectura   | Modular (5 archivos independientes)
| Paradigma      | Programación Funcional y Procedural

## 🏗️ Arquitectura del Proyecto. 
El sistema está dividido en módulos independientes para facilitar su mantenimiento y escalabilidad:  
| Módulos | Descripción
|---------|------------
| `main.py`   | Punto de entrada del programa
| `menu.py`   | Gestiona la interfaz de usuario por consola y el flujo de navegación
| `crud.py`   | Contiene la lógica de negocio (operaciones sobre la lista de pacientes).
| `validaciones.py` | Módulo dedicado a asegurar la integridad de los datos (RUT, Nombre, Email, Edad).
| `archivos_csv.py` | Maneja la lectura y escritura en disco duro.  

## 🚀 Desafíos Enfrentados y Soluciones
#### 1. Validación de Datos Robusta

- __Desafío:__ Evitar que el ingreso de datos erróneos (como un RUT mal escrito o una edad no numérica) provocara el cierre inesperado del programa.

- __Solución:__ Se implementó una __estrategia basada en excepciones__. En el módulo validaciones.py, cada función lanza un `raise ValueError` con un mensaje específico. Estos errores son capturados por la función de orden superior `pedir_dato` en el módulo crud.py, la cual solicita el dato nuevamente hasta que sea válido sin interrumpir el flujo.

#### 2. Sincronización de Persistencia (CSV)
- __Desafío:__ Durante las pruebas de validación, se detectó una inconsistencia en el orden de los datos al guardar y cargar el archivo CSV (específicamente entre los campos edad e email).

- __Solución:__ Se estandarizó la estructura del archivo utilizando un encabezado fijo y se sincronizó el método `.split(";")` de `cargar_csv` con el formato de escritura en `guardar_csv`, asegurando que la información recupere su tipo de dato original (conversión de `str` a `int` para la edad).

#### 3. Modularización y Acoplamiento
- __Desafío:__ Mantener el código limpio y evitar que los módulos dependieran excesivamente unos de otros.

- __Solución:__ Se utilizó un diseño donde `main.py` solo conoce a `menu.py`, y `menu.py` delega las tareas a los módulos especializados, reduciendo el acoplamiento y facilitando la depuración individual de cada componente.

## 📋 Funcionalidades Principales
1. __Registro de Pacientes:__ Validación de RUT chileno (formato y dígito verificador), nombres y correos electrónicos.

2. __Búsqueda Indexada:__ Localización rápida de registros mediante el RUT.

3. __Edición Dinámica:__ Permite actualizar campos específicos manteniendo los valores anteriores si se dejan en blanco.

4. __Almacenamiento Persistente:__ Carga automática y guardado manual en la carpeta `/documentos`.

## 📈 Roadmap (Mejoras Futuras)
- __Refactorización a POO:__ Implementar la clase Paciente para manejar objetos en lugar de diccionarios.

- __Interfaz Gráfica:__ Migrar la consola a una ventana visual con Tkinter.

- __Seguridad:__ Añadir un sistema de login para usuarios autorizados.

- __Funcionalidad:__ Agregar agendamiento y visualizacion de citas médicas.

## 🔧 Instalación y Ejecución
Clona este repositorio o descarga los archivos.  
Asegúrate de tener instalada una versión de Python 3.8 o superior.
Ejecuta el archivo principal: `python main.py`

