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
Basados en el gráfico de ejemplo, se puede concluir que el tiempo de ejecución del programa se comporta de manera inesperada con los diferentes números de hilos (observable en el gráfico "Tiempo de Ejecución vs Número de Hilos"):
1. Con la versión secuencial (sin hilos o línea roja punteada), el programa es muy rápido, tomando solo 0.000001 segundos.
2. Al agregar hilos (línea azul continua con puntos), se puede ver que:

    - Con 1 hilo: el tiempo aumenta a 0.000005 segundos
    - Con 2 hilos: sube drásticamente a 0.00004 segundos
    - Con 4 y 8 hilos: sigue aumentando gradualmente

Esto se refleja también en el gráfico de "Speedup vs Número de Hilos", donde:

- La línea roja punteada muestra el speedup ideal (lo que esperaríamos en un caso perfecto)
- La línea verde con puntos muestra el speedup real, que está muy por debajo de lo ideal

Este comportamiento muestra que agregar más hilos en realidad hace el programa más lento, no más rápido como esperaríamos. Lo que lleva a preguntarse, ¿por qué pasa esto?:
1. Principalmente porque el problema (calcular factoriales hasta N=20) es demasiado pequeño
2. El tiempo que toma crear y gestionar los hilos es mayor que el tiempo que toma hacer los cálculos

Para mejorar esto se debería:
1. Aumentar el valor de N significativamente
2. Hacer cálculos más complejos que realmente justifiquen el uso de varios hilos
