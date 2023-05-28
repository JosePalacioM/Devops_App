# Entrega No. 4 - Monitoreo Continuo: The Code Team 

## Integrantes

|Nombre| Correo Uniandes|
|------|------|
|Oscar Andrés Alba Barragán| o.alba@uniandes.edu.co|
|Edwin Andrés Tapia Lasso| e.tapia@uniandes.edu.co|
|Manuel Fernando Morales Sanchez| mf.moraless1@uniandes.edu.co|
|José Alexander Palacio Muñoz| j.palaciom@uniandes.edu.co|

# Microservicio Gestión de correos

El microservicio de gestión de correos permite añadir cuentas de correo en la lista negra y consultar los correos agregados.

## API

1. **Agregar correo:** Agrega un correo a la lista negra con los datos brindados, el token se puede introducir como una palabra estática. Los campos email, app_uuid y blocked_reason deben estar presentes en la solicitud, el correo no debe existir y el app_uuid no debe estar vacío. POST `/blacklists`
2. **Consultar correo:** Retorna la información de un correo agregado previamente en la lista negra, solo un usuario autorizado puede realizar esta operación, el token se puede introducir como una palabra estática. GET `/blacklists/<string:email>`
3. **Consultar salud del microservicio:** Retorna un código 200, si el microservicio se encuentra en línea. GET `/`

## Ejecución local con Docker
1. Cambiar la variable de entorno para la base de datos: Por defecto la base de datos esta apuntando al RDS creado en AWS, pero se puede cambiar en el archivo Dockerfile en la variable **DATABASE_URL** y colocar un valor como: **sqlite:///block_email.db**
2. Se debe estar en la raíz del proyecto y crear la imagen de Docker con: `docker build -t devops_app .`
3. Luego se debe crear el contenedor con: `docker run -d -p 5000:5000 devops_app`
4. La aplicación queda ejecutando en el puerto 5000 del localhost: `http://localhost:5000`
 
## Ejecución de pruebas unitarias (Windows)
1. Crear ambiente virtual: `python3 -m venv .venv`
2. Activar ambiente virtual: `source .venv/bin/activate`
3. Validar en la consola que se tiene activo el ambiente virtual, para desactivar env: `deactivate`
4. Instalar requirements: `python3 -m pip install -r requirements.txt`
5. Para ejecutar todas las pruebas: `python -m unittest discover -s test -v`
6. Para ejecutar un conjunta de pruebas test_users.py: `python -m unittest test/test_blacklist.py`
7. Para conocer la cobertura de pruebas: `python -m coverage run -m unittest` en caso de que no funcione esta, sebe ejecutar: `coverage run -m unittest tests/test_trayectos.py -v`
8. Para el reporte de pruebas en consola: `python -m coverage report`
9. Para el reporte detallado de las pruebas en archivo html: `python -m coverage html`


# Estructura de archivos y carpetas

├── .ebextensions # Archivos de información de despliege en Elastic Beanstalk  
├── collections # Collecciones de la aplicación (Recomendado usar Postman)  
├── flaskr # Código de la aplicación  
├── test # Pruebas unitarias   
├── .gitignore # Archivos ignorados para git  
├── application.py # Punto de entrada de la aplicación  
├── appspec.json # Archivo utilizado por CodeDeploy para gestionar un despliegue  
├── buildspec_v1.yml # Archivo con los comandos de CodeBuild que ejecutará durante cada fase de la compilación (Entrega dos)   
├── buildspec_v2.yml # Archivo con los comandos de CodeBuild que ejecutará durante cada fase de la compilación (Entrega tres)
├── buildspec_v3.yml # Archivo con los comandos de CodeBuild que ejecutará durante cada fase de la compilación (Entrega cuatro)     
├── Dockerfile # Archivo de Docker para despliegue  
├── README.md # **Estás aquí**  
├── requirements.txt # Archivo de requirements para funcionameinto de la aplicación    
└── taskdef.json # Archivo que contiene toda la definición de tareas que utiliza ECS

# Despliegue en AWS
La aplicación se encuentra desplegada y administrada en **AWS Elastic Beanstalk** que es un servicio para implementar y escalar servicios y aplicaciones web.
Por otro lado se configuró un Pipeline en **AWS CodePipeline** que es un servicio de integración y entrega continuas (CI/CD), para realizar actualizaciones de aplicaciones e infraestructura rápidas y confiables. CodePipeline compila, prueba e implementa el código cada vez que se produce un cambio, de acuerdo con los modelos de procesamiento de lanzamiento que defina.

- Para más información del despliegue en estos servicios, consultar la documentación adjunta de la entrega.
- La documentación de las colecciones se puede revisar en la siguiente URL [Colecciones The Code Team](https://documenter.getpostman.com/view/20261140/2s93XyU3Nt) o revisar la carpeta **collections**
- Para cualquier duda adicional, por favor ponerse en contacto con cualquier miembro del equipo.