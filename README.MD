# Encriptación por metodo de Hills

## ¿Quién hizo esto?

Sebastián Tamayo Avendaño - Estudiante Ing Sistemas.
Interfaz web: Natalia Flórez - Estefany Jaimes

## ¿Qué es y para qué es?

Este es un método de encriptación a través de matrices que esta relacionado con él código cesar, este tiene alfabeto donde cada palabra tiene un número o peso asociado Este se utilizará a través de operaciones entre matrices para obtener la encriptación De un mensaje limitado por la cantidad de letras en el alfabeto.

## ¿Cómo lo hago funcionar?

### Prerrequisitos:
    - Descargar libreria numpy
    - Descargar libreria sympy
    - Descargar libreria src
    - Descargar libreria kivy
    - Descargar librería Flask
    - Descargar psycopg2


## ¿Cómo está hecho?

El cifrado Hill es un criptosistema que se basa en emplear una matriz como clave para cifrar un texto en claro y 
Su inversa para descifrar el criptograma correspondiente.

Se ha usado un alfabeto de 67 caracteres que incluyen letras  dígitos numéricos, del 0 al 9, 
así como los 4 caracteres siguientes: ".", ",", ":", "?" y el espacio en blanco, en ese orden.

Cada letra está representada por un número (diccionario).

## Estructura

- Carpeta src: Codigo fuente de la logica de la aplicación. Tiene subcarpetas por cada capa de la aplicacion
- Carpeta tests: Pruebas Unitarias (UnitTests-Encryption.py)

Recuerde que cada carpeta de código fuente debe contener un archivo __init.py que permite que python
reconozca la carpeta como un Módulo y pueda hacer import

- Modulos: Existen los siguientes modulos en el conjunto de subcarpetas **src**, que estan diseñados para la logica y la interfaz del Usuario.

├── src/
│   ├── Console/
│   │   ├── EncryptionGUI_Console.py
│   │   ├──__init__.py
│   ├── Database/
│   │   ├── Controllers/
│   │   │   ├── __init__.py
│   │   │   ├── UserController.py
│   │   │   ├── EncryptionKeyController.py
│   │   ├── Models/
│   │   │   ├── __init__.py
│   │   │   ├── User.py
│   │   │   ├── EncryptionKey.py
│   │   ├── tests/
│   │   │   ├── ControllerEncryptionKey.py
│   │   │   ├── ControllerUserTest.py
│   │   ├── SecretConfig.py
│   │   ├── __init__.py
│   ├── Encryption/
│   │   ├──__init__.py
│   │   ├──EncryptionLogic.py
│   ├── Gui/
│   │   ├──Console/
│   │   │   ├── EncryptionGUI_Console.py
│   │   │   ├── __init__.py
│   │   ├── GuiLogic/
│   │   │   ├── Kivy/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── EncryptionGUI_KivyLogic.py
│   │   │   ├── __init__.py
│   │   ├── Kivy/
│   │   │   ├── __init__.py
│   │   │   ├── EncryptionGUI_Kivy.py
│   │   │   ├── LoginGUI_Kivy.py
│   │   │   ├── MenuGUI_Kivy.py
│   │   ├── view_web/
│   │   │   ├── __init__.py
│   │   │   ├── vista_usuarios.py
│   │   ├── __init__.py
│   ├── __init__.py
├── static/
│   ├── encrypt.js
│   ├── images/
│   │   ├── encriptacion.png
├── templates/
│   ├── index.html
│   ├── login.html
├── tests/
│   ├── __init__.py
│   ├── UnitTests-Encryption.py
└── app.py

Paso a Paso para Abrir Encryptation Program
Aquí tienes los pasos detallados para abrir y utilizar el Encriptador de Texto:

Opción 1: Descargar desde GitHub:

Descarga de Archivos:

Descarga el archivo comprimido "EncriptacionCodLimpio" desde el enlace proporcionado o desde donde te hayan entregado el archivo.

Extracción de Archivos:

Abre el archivo comprimido "EncriptacionCodLimpio-main.zip" utilizando un programa de extracción de archivos, como WinRAR o 7-Zip.
Extrae todos los archivos de la carpeta en una ubicación de tu elección en tu computadora.

Opción 2: Clonar el Repositorio desde Github:

Clonar el Repositorio:

Abre la terminal o línea de comandos en tu computadora.
Navega hasta el directorio donde deseas clonar el repositorio utilizando el comando cd.
Utiliza el siguiente comando para clonar el repositorio desde GitHub:
git clone https://github.com/usuario/EncriptacionCodLimpio.git

Reemplaza usuario por el nombre de usuario de GitHub donde se encuentra el repositorio.

Conexión a la base de datos:
Accede al sitio web de Neon: Ve a Neon.Tech desde tu navegador web.

Regístrate o inicia sesión: Si aún no tienes una cuenta, regístrate en la plataforma. De lo contrario, inicia sesión con tus credenciales.

Crea un nuevo proyecto: Una vez dentro, crea un nuevo proyecto. Elige un título para el proyecto y nombra la base de datos como "Encryptation_Program".

Accede al panel de control (Dashboard): Después de crear el proyecto y la base de datos, ve al panel de control.

Obtén la cadena de conexión: En el panel de control, busca la opción de "Connection string" y selecciónala. Luego elige la opción "Parameters only". Esto te proporcionará una cadena de conexión que necesitarás más adelante.

Copia la cadena de conexión: Copia todo el contenido del campo de texto proporcionado con la cadena de conexión.

Ubica el archivo SecretConfigSample.py: En el repositorio de tu proyecto, busca la carpeta "src" y luego la carpeta "Database". Dentro de esta carpeta, encontrarás un archivo llamado "SecretConfigSample.py".

Pega la cadena de conexión: Abre el archivo "SecretConfigSample.py" y pega los parámetros de la cadena de conexión que copiaste en el paso anterior.

Renombra el archivo: Por último, cambia el nombre del archivo "SecretConfigSample.py" por "SecretConfig.py". Esto asegurará que el sistema reconozca la configuración de la base de datos.

## Uso

Para ejecutar las pruebas unitarias de la encriptacion, desde la carpeta src, use el comando

`
  python tests\UnitTests-Encryption.py
`

Para ejecutar las pruebas unitarias de la base de datos para el usuario, use el comando

`
  python src\Database\tests\ControllerUserTest.py
`

Para ejecutar las pruebas unitarias de la base de datos para las claves del usuario, use el comando

`
  python src\Database\tests\ControllerEncryptionKey.py
`

Para poder ejecutarlas desde la carpeta raiz, debe indicar la ruta de busqueda donde se encuentran los
módulos, incluyendo las siguientes lineas al inicio del módulo de pruebas

- Este programa cuenta con tres interfaces de usuario:
1. Consola
2. Kivy
3. Web 

### Para ejecutar la interfaz por consola, se debe utilizar el siguiente comando:

`
  python src\Console\EncryptionUi_Console.py
`
### Para ejecutar la interfaz de Kivy

`
  python src\Gui\Kivy\EncryptionGUI_Kivy
`
### Para ejecutar la interfaz Web ubiquese en la raíz del archivo y ejecute

`
  python app.py
`
Presiona Enter para ejecutar el comando. Aparecerá un mensaje similar a este:
     ```
     * Running on http://127.0.0.1:5000
     Press CTRL+C to quit
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 501-583-688
     ```
Copia el enlace de "Running on" (en este caso, `http://127.0.0.1:5000`) y pégalo en tu navegador, o presiona Ctrl y haz clic en el enlace para seguirlo directamente.
Ahora podrás acceder a tu aplicación web en el navegador utilizando la dirección proporcionada.



## El orden de ejecucion del programa en consola consiste en:

1. Se ingresa un mensaje
2. Seleccionar el tamaño de la clave, que sera una matrix, nxn elementos adentro **Solo se permiten numeros**
3. Seleccionar si esta clave quiere ser creada de forma automatica (valores aleatorios) o de forma manual con datos especificos.
4. Seleccionar si se quiere encriptar o desincriptar, si no se ha encriptado anteriormente, saldra un error si se selecciona desencriptar.
   Una vez que se encripte, se puede continuar el programa para utilizar la funcionalidad de desencriptacion, si selecciona "n", el programa
   Volvera ejecutarse desde el inicio.


## El orden de ejecucion del programa en Kivy consiste en:
1. Ingresa a tu base de datos y crea una tabla con el comando que se encuentra en la carpeta sql en la raiz del proyecto, allí encontrarás dos archivos:
-CreateEncryptionKey.sql
-CreateUser.sql
A continuación copia el contenido de esos archivos, ingresalos en tu editor sql y ejecútalos.
2. Haz la conexión a la base de datos.
3. Ingresa un usuario y una contraseña y dale click en el botón registrate. En caso de ya estar registrado en tu base de datos simplemente dale click en iniciar sesión.
4. Se ingresa un mensaje y se verifica si es valido para la encriptacion si se presiona Enter.
5. Seleccionar el tamaño de la clave en el menu y ingresar los datos de la matriz:
	- Escribir la clave en el formato "1,2,3,7,8,9" donde tiene que haber una cantidad de elementos igual a
	  Tamaño de la matriz ^ 2
	- Si no se escribe correctamente, se dispara una excepcion dependiendo del error.
6. Seleccionar si se quiere encriptar o desincriptar, si no se ha encriptado anteriormente, saldra una excepcion si se selecciona desencriptar.

## El orden de ejecución del programa en la interfaz web:
1. Ingresa a tu base de datos y crea una tabla con el comando que se encuentra en la carpeta sql en la raiz del proyecto, allí encontraráás el siguiente archivo:
-CreateUser.sql
A continuación copia el contenido de ese archivo, ingresalo en tu editor sql y ejecútalo.
2. haz la conexión a la base de datos.
3. Ingresa un usuario y una contraseña y dale click en el botón registrarse. En caso de ya estar registrado en tu base de datos simplemente dale click en iniciar sesión.
4. Seleccionar el tamaño de la clave en el menu.
5. Escriba el mensaje que desea encriptar o desencriptar, presione el botón correspondiente.
6. Cierre sesión.

- En caso que no funcione alguno de los modulos, ingrese el siguiente comando: 

`
  import sys
  sys.path.append("src")
`
#   E n c r i p t a c i o n C o d L i m p i o  
 