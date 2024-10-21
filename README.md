# Documentación del Sistema Penitenciario

Este documento detalla los pasos para levantar el entorno de ejecución del proyecto **Sistema Penitenciario**, implementado en Python 3.9.6, con conexión a una base de datos MySQL mediante la librería `pyodbc`. El código del proyecto está alojado en el siguiente repositorio público: [Carcel-Repositorio](https://github.com/osvaldoGC4/Carcel-Repositorio.git).

## Tabla de Contenidos
- [Requisitos del Proyecto](#requisitos-del-proyecto)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Guía de Instalación](#guía-de-instalación)
- [Configuración de la Base de Datos](#configuración-de-la-base-de-datos)
- [Cadena de Conexión a la Base de Datos](#cadena-de-conexión-a-la-base-de-datos)
- [Configuración del Entorno de Desarrollo](#configuración-del-entorno-de-desarrollo)
- [Ejecución del Proyecto](#ejecución-del-proyecto)
- [Contribución al Proyecto](#contribución-al-proyecto)

## Requisitos del Proyecto

1. **Lenguaje de Programación**: Python 3.9.6.
2. **Sistema de Gestión de Base de Datos**: MySQL.
3. **Conexión a la base de datos**: Librería `pyodbc`.
4. **Servidor Web**: Utilizado mediante XAMPP (con MySQL y Apache).
5. **Control de Versiones**: Git.

### Dependencias del Proyecto
- `pyodbc`: Librería para conectar Python con MySQL.
  
Instalación:
```bash
pip install pyodbc

XAMPP: Servidor web local para ejecutar MySQL y Apache.
Descargar XAMPP: https://www.apachefriends.org/index.html

#### Estructura del Proyecto

Carcel-Repositorio/
│
├── main.py                 # Archivo principal del proyecto
├── Models/
│   └── entidad.py          # Definiciones de las entidades del sistema
├── Controller/
│   └── entidad.py          # Controladores para manejar las entidades
├── Common/
│   ├── conexion.py         # Gestión de la conexión a la base de datos
│   └── crud.py             # Métodos comunes de creación, lectura, actualización y eliminación
├── Scripts/
│   └── EsquemaBD.sql       # Script SQL para crear el esquema de la base de datos
└── README.md               # Documentación del proyecto

##### Guía de Instalación

Paso 1: Clonar el Repositorio
Para empezar, clona el repositorio del proyecto en tu máquina local:

git clone https://github.com/osvaldoGC4/Carcel-Repositorio.git
cd Carcel-Repositorio

Paso 2: Instalación de Python 3.9.6
Asegúrate de tener instalada la versión de Python 3.9.6 en tu sistema. Puedes descargarla desde el sitio oficial de Python:
Descargar https://www.python.org/downloads/release/python-396/

Verifica la instalación de Python:
python --version

Paso 3: Instalar Dependencias
Instala las dependencias necesarias, en este caso, la librería pyodbc para la conexión a MySQL:
pip install pyodbc

Paso 4: Instalar XAMPP
Descarga e instala XAMPP para gestionar el servidor MySQL y Apache:

Una vez instalado, inicia el servidor MySQL desde el panel de control de XAMPP.

Configuración de la Base de Datos

Paso 1: Crear la Base de Datos
Accede al panel de phpMyAdmin de XAMPP en http://localhost/phpmyadmin y crea una base de datos llamada carcel.

Paso 2: Ejecutar el Script SQL
En el directorio Scripts/ del proyecto, se encuentra el archivo EsquemaBD.sql, que contiene la estructura de la base de datos. Ejecuta este script en tu base de datos carcel para crear las tablas necesarias.

Para ejecutar el script:

Abre phpMyAdmin.
Selecciona la base de datos carcel.
Haz clic en la pestaña SQL y carga el archivo EsquemaBD.sql o copia y pega su contenido.
Ejecuta el script.
Cadena de Conexión a la Base de Datos
La cadena de conexión utilizada en el proyecto es la siguiente:

string_conexion: str = """
    Driver={MySQL ODBC 9.0 Unicode Driver};
    Server=localhost;
    Database=carcel;
    PORT=3306;
    user=user_carcel;
    password=carcel1234"""

Asegúrate de que el controlador ODBC de MySQL esté instalado en tu sistema. Si no lo tienes, puedes descargarlo desde el siguiente enlace:
https://dev.mysql.com/downloads/connector/odbc/

Configurar la Conexión en el Proyecto
El archivo conexion.py en la carpeta Common/ gestiona la conexión a la base de datos. No es necesario modificar la conexión si tu configuración local coincide con la cadena proporcionada.

Configuración del Entorno de Desarrollo
Para configurar el entorno de desarrollo:

Asegúrate de tener pyodbc instalado.
Inicia el servidor MySQL en XAMPP.
Ejecuta el script SQL para crear el esquema de la base de datos.

Ejecución del Proyecto
Una vez que tengas todo el entorno configurado:

Verifica que el servidor MySQL esté ejecutándose en XAMPP.
Desde la terminal, navega al directorio del proyecto.
Ejecuta el archivo main.py: python main.py


Contribución al Proyecto
Si deseas contribuir a este proyecto, sigue estos pasos:

1. Clona el repositorio en tu máquina local.

2. Crea una nueva rama para tus cambios: 
git checkout -b nombre-de-tu-rama

3. Realiza tus cambios y guarda el progreso: git add .
git commit -m "Descripción de los cambios"

4. Sube tus cambios al repositorio:
git push origin nombre-de-tu-rama

5. Abre un Pull Request en GitHub describiendo tus cambios detalladamente.



