# Devops_App

# Entrega No. 1: The Code Team -
Integrantes:
|Nombre|Usuario Github|Correo Uniandes|
|----|----|----|
|Oscar Andrés Alba Barragán|AAlbaB|o.alba@uniandes.edu.co|
|Edwin Andrés Tapia Lasso|casetl|e.tapia@uniandes.edu.co|
|Manuel Fernando Morales Sanchez|manuel-morales-sa|mf.moraless1@uniandes.edu.co|
|José Alexander Palacio Muñoz|JosePalacioM|j.palaciom@uniandes.edu.co|

# Microservicio Gestión de correos
El microservicio de gestión de correos permite crear cuentas de correo en la lista negra y consultar los correos creados.

## API
1. **Creación de correos:** Crea un correo con los datos brindados, el token se puede introducir como una palabra estática. Los campos email, app_uuid y blocked_reason deben estar presentes en la solicitud, el correo no debe existir y el app_uuid no debe estar vacío. POST ```/blacklists```
2. **Consultar correo:** Retorna la información de un correo creado previamente en la lista negra, solo un usuario autorizado puede realizar esta operación, el token se puede introducir como una palabra estática. GET ```/blacklists/<string:email>```

## Ejecución manual (En Linux - Ubuntu)
Se debe estar en la carpeta **flaskr**
1. Crear ambiente virtual: `python3 -m venv .venv`
2. Activar ambiente virtual: `source .venv/bin/activate`
3. Validar en la consola que se tiene activo el ambiente virtual, para desactivar env: `deactivate`
4. Instalar requirements: `python3 -m pip install -r requirements.txt`
5. Configurar base de datos SQLite: `export DATABASE_URL="sqlite:///correos.db"`
5. Cambiar el directorio: `cd flaskr`
6. Ejecutar aplicación Flask: `flask run`
7. La aplicación queda ejecutando en el puerto 5000 del localhost: ```http://localhost:5000```



# Estructura de carpetas
├── collections # Collecciones individuales de la aplicación

├── flaskr # Código de la aplicación

└── requirements.txt # Archivo de requirements para funcionameinto de la aplicación

└── README.md # Estás aquí