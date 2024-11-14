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
      pip install pandas
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

### Ejercicio 2: Simulación de Incrementos en Valores Aleatorios
Este ejercico consisten en crear un arreglo de N números enteros inicializados en cero. Paraleliza el proceso en el cual cada hilo incrementa un valor aleatorio del arreglo en un bucle de M iteraciones.

#### Compilación y Ejecución
1. **Compilar el Programa**
   
   Una vez activado el entorno virtual, debe dirigirse a la carpeta del ejercicio 2
    ```bash
      cd Ejercicio_2
    ```

   Luego, para compilar el programa, utilice el siguiente comando:
    ```bash
      gcc -fopenmp random_increments.c -o random_increments
    ```
2. **Ejecutar Programa**
   
   Ejecutar el archivo creado:
    ```bash
      ./random_increments
    ```
3. **Generar Gráficos de Rendimiento**
   
   Para evidenciar a través de gráficos los resultados, utilice el script de python, ya que importa al archivo **_random_increments_**
    ```bash
      python plot_increments.py
    ```

#### Estructura de archivos
- `random_increments.c`: Implementación del programa de incrementos aleatorios
- `plot_increments.py`: Script para visualización de resultados

#### Funcionalidades
- Inicialización de array con números aleatorios
- Implementación sin sincronización y con sección crítica
- Medición de tiempos de ejecución y precisión
- Comparación de rendimiento con diferentes números de hilos

#### Resultados
Como ejemplo en la ejecución del programa, al crear el gráfico, entrega este resumen para entender mejor los resultados:

| N° Hilos | Tiempo Sin Sync (s) | Tiempo Con Sync (s) | Suma Sin Sync (% error) | Suma Con Sync (% error) |
|-----------|-------------------|--------------------|----------------------|---------------------|
| 1         | 0.0002           | 0.0005            | 0.0                  | 0.0                 |
| 2         | 0.0004           | 0.0011            | 0.0                  | 0.0                 |
| 4         | 0.0006           | 0.0024            | 0.0                  | 0.0                 |
| 8         | 0.0020           | 0.0045            | 0.0                  | 0.0                 |

A continuación se muestran los gráficos de ejemplo al ejecutar el programa:

![image](https://github.com/user-attachments/assets/576faa02-ef67-492b-a973-5af5bcbc551b)

#### Análisis de Resultados
Las diferencias entre la versión con y sin sección crítica son notables:

1. **Tiempos de Ejecución**
   - **Sin Sincronización:** Más rápido en todos los casos,  lo que indica una reducción en el overhead de procesamiento
   - **Con Sincronización:** Aproximadamente 2-4 veces más lento debido al overhead de la sección crítica. Este overhead es causado por el mecanismo de sincronización, que asegura el acceso controlado a los recursos compartidos, pero introduce un costo adicional en términos de rendimiento y tiempo

2. **Precisión**
   - Ambas versiones muestran 0% de error en estas pruebas específicas
   - Este comportamiento sugiere que el tamaño de las pruebas podría ser insuficiente para evidenciar condiciones de carrera

3. **Escalabilidad**
   - La diferencia en tiempos se amplía al aumentar el número de hilos
   - Con 8 hilos, la versión sincronizada es más del doble de lenta que la no sincronizada
   - Al no observarse errores, es posible que el volumen de datos y la frecuencia de acceso a los recursos compartidos no hayan sido suficientes para ocasionar inconsistencias.

#### Pruebas futuras
En este caso particular, la sección crítica añade overhead sin beneficio aparente en la precisión. Esto podría deberse a que el tamaño de las pruebas es relativamente pequeño y las condiciones de carrera no fueron evidentes en estos datos específicos.

Para obtener resultados más representativos, se recomienda aumentar significativamente los valores de N y M en las pruebas. En el archivo **_random_increments.c** se puede modificar la siguiente sección:

```c
// Valores originales
int N_values[] = {1000, 10000, 100000};       // Tamaño del array
int M_values[] = {1000, 10000, 100000};       // Número de iteraciones
```

Modificarlo a:

```c
// Nuevos valores de prueba
int N_values[] = {100000, 1000000, 10000000}; // Tamaño del array
int M_values[] = {100000, 1000000, 10000000}; // Número de iteraciones
```

