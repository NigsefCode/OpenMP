# Evaluación 4: OpenMP
- Integrante: Nicolás Sepúlveda Falcón
  
- Curso: Administración de Sistemas



## Introducción
Este proyecto tiene como objetivo implementar y evaluar diferentes algoritmos utilizando programación paralela con OpenMP. Se analizan los tiempos de ejecución y el rendimiento al utilizar diferentes números de hilos, comparando las versiones secuenciales y paralelas de cada implementación.


## Instrucciones de Instalación y Ejecución
### Requisitos Previos
Antes de comenzar con la ejecución del proyecto, asegurarse de tener lo siguiente instalado en su equipo de trabajo:
1. **OpenMP**
2. **Python y Dependencias**

En caso de no tener instalador **_OpenMP_**, puede instalarlo de la siguiente manera:
  ```bash
  sudo apt-get install gcc
  ```
En caso de no tener instalador **_Python_**, puede instalarlo de la siguiente manera:
  ```bash
  sudo apt install python3-full python3-venv
  ```

### Configuración y Ejecución
Una vez corroborada la instalación de los requisitos previos, puede seguir los siguientes pasos:

1. **Actualizar el Sistema Operativo.**
    ```bash
      sudo apt update
      sudo apt upgrade
    ```
2. **Clonar el Repositorio.**
    ```bash
      git clone <url-del-repositorio>
      cd <nombre-del-directorio>
    ```
3. **Configurar el Entorno Virtual en Python.**
    ```bash
      python3 -m venv venv
      source venv/bin/activate
      pip install matplotlib numpy
    ```

### Ejercicio 1: Cálculo de Factoriales en Paralelo
Este ejercicio implementa el cálculo de factoriales utilizando paralelización con OpenMP. Se comparan los tiempos de ejecución entre la versión secuencial y versiones paralelas con diferentes números de hilos. Se armarán gráficos que evidencien los resultados.

#### Compilación y Ejecución
1. **Compilar el Programa**
   
   Una vez activado el entorno virtual, debe dirigirse a la carpeta del ejercicio 1
    ```bash
      cd Ejercicio_1
    ```

   Luego, para compilar el programa, utilice el siguiente comando:
    ```bash
      gcc -fopenmp factorial_parallel.c -o factorial_parallel
    ```
2. **Ejecutar Programa**
   
   Ejecutar el archivo creado:
    ```bash
      ./factorial_parallel
    ```
3. **Generar Gráficos de Rendimiento**
   
   Para evidenciar a través de gráficos los resultados, utilice el script de python, ya que importa al archivo **_factorial_parallel_**
    ```bash
      python graficar_automatico.py
    ```

#### Estructura de archivos
- `factorial_parallel.c`: Implementación del cálculo de factoriales
- `graficar_automatico.py`: Script para visualización de resultados mediante gráficos

#### Funcionalidades
- Cálculo de factoriales de 1 a N
- Comparación de tiempos entre versión secuencial y paralela
- Medición de speedup con diferentes números de hilos (1, 2, 4, 8)
- Generación automática de gráficos de rendimiento

#### Visualización de Resultados
El Script de visualización genera dos gráficos
1. Tiempo de ejecución vs Número de hilos
2. Speedup vs Número de hilos

Los gráficos se guardan automáticamente con un timestamp en el formato: `analisis_rendimiento_factorial_YYYYMMDD_HHMMSS.png`, como lo puede observar en la siguiente imagen:

![alt text](https://github.com/NigsefCode/OpenMP/blob/main/Ejercicio_1/analisis_rendimiento_factorial_20241111_155002.png?raw=true)

#### Análisis de resultados

