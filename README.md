# Entrega No. 1: The Code Team 

**Integrantes:**

|Nombre|Usuario Github|Correo Uniandes|
|----|----|----|
|Oscar Andrés Alba Barragán|AAlbaB|o.alba@uniandes.edu.co|
|Edwin Andrés Tapia Lasso|casetl|e.tapia@uniandes.edu.co|
|Manuel Fernando Morales Sanchez|manuel-morales-sa|mf.moraless1@uniandes.edu.co|
|José Alexander Palacio Muñoz|JosePalacioM|j.palaciom@uniandes.edu.co|

# Microservicio Gestión de correos

El microservicio de gestión de correos permite añadir cuentas de correo en la lista negra y consultar los correos agregados.

## API

1. **Agregar correo:** Agrega un correo a la lista negra con los datos brindados, el token se puede introducir como una palabra estática. Los campos email, app_uuid y blocked_reason deben estar presentes en la solicitud, el correo no debe existir y el app_uuid no debe estar vacío. POST `/blacklists`
2. **Consultar correo:** Retorna la información de un correo agregado previamente en la lista negra, solo un usuario autorizado puede realizar esta operación, el token se puede introducir como una palabra estática. GET `/blacklists/<string:email>`

3. **Consultar salud del microservicio:** Retorna un código 200, si el microservicio se encuentra en línea. GET `/healthcheck`

## Ejecución manual (Windows)

Para la ejecución local del proyecto, es nevcsario cambiar el nombre del archivo **application.py** por **app.py**, asi mismo, dentro de este archivo, se debe cambiar la palabra **application** por **app**, debido a que así se podrá ejecutar por Flask.

1. Crear ambiente virtual: `python3 -m venv .venv`
2. Activar ambiente virtual: `source .venv/bin/activate`
3. Validar en la consola que se tiene activo el ambiente virtual, para desactivar env: `deactivate`
4. Instalar requirements: `python3 -m pip install -r requirements.txt`
5. Configurar base de datos SQLite: `export DATABASE_URL="sqlite:///correos.db"`
6. Ejecutar aplicación Flask: `flask run`
7. La aplicación queda ejecutando en el puerto 5000 del localhost: `http://localhost:5000`

# Estructura de carpetas

├── .ebextensions # Archivos de información de despliege en en Elastic Beanstalk
├── collections # Collecciones individuales de la aplicación
├── flaskr # Código de la aplicación
├── application.py # Punto de entrada de la aplicación
├── requirements.txt # Archivo de requirements para funcionameinto de la aplicación
└── README.md # Estás aquí

# Despliegue en AWS - Elastic Beanstalk
La aplicación se encuentra desplegada y administrada en Amazon Elastic Beanstalk, que es un servicio que ofrece AWS para la adminitración integral de aplicaciones WEB. Así mismo, la base de datos se encuentra administrada por el servicio de RDS también de AWS.

- Para más información del despliegue en estos servicios, consultar la documentación adjunta de la entrega.
- La documentación de las colecciones se puede revisar en la siguiente URL [Colecciones The Code Team](https://documenter.getpostman.com/view/20261140/2s93XyU3Nt) o revisar la carpeta **collections**
- Para cualquier duda adicional, por favor ponerse en contacto con cualquier miembro del equipo.


