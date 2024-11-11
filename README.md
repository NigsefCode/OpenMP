# Evaluación 3: Microservicios Docker Compose

- Integrante: Nicolás Sepúlveda Falcón
  
- Curso: Administración de Sistemas



## Introducción
Este proyecto tiene como objetivo implementar y configurar un entorno de microservicios utilizando Docker, que incluye una aplicación web, una base de datos PostgresSQL, Redis para caché, Nginx como proxy inverso y un servicio de autenticación.


## Instrucciones de Instalación y Ejecución
### Requisitos Previos
Antes de comenzar con la ejecución del proyecto, asegurarse de tener lo siguiente instalado en su equipo de trabajo:
1. **Docker**
2. **Docker Compose**

En caso de no posee Docker, puede instalarlo de la siguiente manera según el tutorial de [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-es). Cabe mencionar que el objetivo de este proyecto no es esta instalación.

### Configuración y Ejecución
Una vez corroborada la instalación de `Docker` y `Docker Compose`, puede seguir los siguientes pasos:

1. **Actualizar el Sistema Operativo.**
    ```bash
      sudo apt update
      sudo apt upgrade
    ```
2. **Clonar el Repositorio.**
    ```bash
      git clone <url-del-repositorio>
      cd <nombre-del-directorio>
