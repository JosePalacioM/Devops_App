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

Para la ejecución local del proyecto, es nevcsario cambiar el nombre del archivo **application.py** por **app.py**. Asi mismo, dentro de este archivo, se debe cambiar la palabra **application** por **app**, debido a que así se podrá ejecutar por Flask.

1. Crear ambiente virtual: `python3 -m venv .venv`
2. Activar ambiente virtual: `source .venv/bin/activate`
3. Validar en la consola que se tiene activo el ambiente virtual, para desactivar env: `deactivate`
4. Instalar requirements: `python3 -m pip install -r requirements.txt`
5. Configurar base de datos SQLite: `export DATABASE_URL="sqlite:///block_email.db"`
6. Ejecutar aplicación Flask: `flask run`
7. La aplicación queda ejecutando en el puerto 5000 del localhost: `http://localhost:5000`

## Ejecución de pruebas unitarias
1. Para ejecutar todas las pruebas: `python -m unittest discover -s test -v`
2. Para ejecutar un conjunta de pruebas test_users.py: `python -m unittest test/test_blacklist.py`
3. Para conocer la cobertura de pruebas: `python -m coverage run -m unittest` en caso de que no funcione esta, sebe ejecutar: `coverage run -m unittest tests/test_trayectos.py -v`
4. Para el reporte de pruebas en consola: `python -m coverage report`
5. Para el reporte detallado de las pruebas en archivo html: `python -m coverage html`


# Estructura de carpetas

├── .ebextensions # Archivos de información de despliege en en Elastic Beanstalk  
├── collections # Collecciones individuales de la aplicación  
├── flaskr # Código de la aplicación 
├── test # Pruebas unitarias  
├── application.py # Punto de entrada de la aplicación   
├── requirements.txt # Archivo de requirements para funcionameinto de la aplicación   
└── README.md # Estás aquí

# Despliegue en AWS
La aplicación se encuentra desplegada y administrada en Amazon Elastic Beanstalk, que es un servicio que ofrece AWS para la adminitración integral de aplicaciones WEB. También se configuro un Pipe line de integración continua en Amazon Code Pipeline para realizar las pruebas unitarias de la aplicación y compilar el proyecto.

- Para más información del despliegue en estos servicios, consultar la documentación adjunta de la entrega.
- La documentación de las colecciones se puede revisar en la siguiente URL [Colecciones The Code Team](https://documenter.getpostman.com/view/20261140/2s93XyU3Nt) o revisar la carpeta **collections**
- Para cualquier duda adicional, por favor ponerse en contacto con cualquier miembro del equipo.


