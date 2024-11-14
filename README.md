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

![alt text](https://github.com/user-attachments/assets/576faa02-ef67-492b-a973-5af5bcbc551b)

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

### Ejercicio 3: Suma Acumulativa de Números Flotantes usando Reducción
Este ejemplo genera un arreglo de N números flotantes aleatorios entre 0 y 1. Paraleliza el cálculo de la suma de estos números usando OpenMP.

#### Compilación y Ejecución
1. **Compilar el Programa**
   
   Una vez activado el entorno virtual, debe dirigirse a la carpeta del ejercicio 3
    ```bash
      cd Ejercicio_3
    ```

   Luego, para compilar el programa, utilice el siguiente comando:
    ```bash
      gcc -fopenmp float_sum.c -o float_sum
    ```
2. **Ejecutar Programa**
   
   Ejecutar el archivo creado:
    ```bash
      ./float_sum
    ```
3. **Generar Gráficos de Rendimiento**
   
   Para evidenciar a través de gráficos los resultados, utilice el script de python, ya que importa al archivo **_float_sum_**
    ```bash
      python plot_reduction.py
    ```

#### Estructura de archivos
- `float_sum.c`: Implementación de suma acumulativa con reducción
- `plot_reduction.py`: Script para visualización de resultados

#### Resultados

**Resultados Detallados por Tamaño de Array**

Al ejecturar **_float_sum_** entrega estos resultados:

| Tamaño del Array | Hilos | Tiempo Secuencial (s) | Tiempo Paralelo (s) | Speedup |
|------------------|-------|----------------------|-------------------|---------|
| 1,000,000        | 2     | 0.002265            | 0.002410         | 0.94    |
| 1,000,000        | 4     | 0.002265            | 0.002908         | 0.78    |
| 1,000,000        | 8     | 0.002265            | 0.002981         | 0.76    |
| 10,000,000       | 2     | 0.022355            | 0.022533         | 0.99    |
| 10,000,000       | 4     | 0.022355            | 0.042176         | 0.53    |
| 10,000,000       | 8     | 0.022355            | 0.048893         | 0.46    |
| 100,000,000      | 2     | 0.253545            | 0.268584         | 0.94    |
| 100,000,000      | 4     | 0.253545            | 0.251687         | 1.01    |
| 100,000,000      | 8     | 0.253545            | 0.274796         | 0.92    |

> **Nota**: Speedup = Tiempo Secuencial / Tiempo Paralelo.
> Valores > 1 indican mejora de rendimiento.

**Resumen de Resultados**

Y luego al ejecutar **_python plot_reduction.py_** da un resumen:

| Hilos | Tiempo Secuencial (s) | Tiempo Paralelo (s) |
|-------|----------------------|-------------------|
| 2     | 0.096306            | 0.088834         |
| 4     | 0.096306            | 0.089156         |
| 8     | 0.096306            | 0.095355         |

A continuación se muestran los gráficos de ejemplo al ejecutar el programa:

![alt text](https://github.com/NigsefCode/OpenMP/blob/main/Ejercicio_3/analisis_reduccion.png?raw=true)

#### Análisis de Resultados

1. **Impacto del Tamaño del Array**:

   a) Arrays Pequeños (1M):
   * El rendimiento en paralelo fue inferior al secuencial
   * La eficiencia (speedup) disminuye a medida que se usan más hilos (0.94 a 0.76)
   * El overhead de paralelización supera los beneficios

   b) Arrays Medianos (10M):
   * Con 2 hilos mantiene un rendimiento similar al secuencial (speedup 0.99)
   * Con 4 y 8 hilos, el rendimiento cae considerablemente (speedup cae a 0.46)
   * Aquí se observa que el tiempo extra de coordinación entre hilos es aún mayor

   c) Arrays Grandes (100M):
   * Único caso de mejora real con 4 hilos (speedup 1.01)
   * Con 2 hilos, el rendimiento sigue siendo cercano al secuencial (0.94)
   * Con 8 hilos, el rendimiento baja levemente (0.92), pero es mucho más estable

2. **Escalabilidad**:
   - Mejor escalabilidad en arrays grandes (100M)
   - El mejor rendimiento se observa con 4 hilos en arrays grandes
   - En todos los casos, el rendimiento disminuye cuando se utilizan 8 hilos

3. **Eficiencia de la Paralelización**:
   - La paralelización es efectiva solo para problemas grandes (100 M) y al usar 4 hilos
   - En arrays pequeños, la paralelización es incluso contraproducente
   - Balance óptimo entre overhead y beneficio en 100M y 4 hilos

4. **Recomendaciones**:
   - Usar paralelización solo para arrays grandes (>100M)
   - Limitar el número de hilos a 4
   - Evitar paralelización en arrays pequeños

#### Explicación de cómo la Reducción Evita Condiciones de Carrera
La reducción (`reduction(+:suma)`) previene condiciones de carrera a través de estos mecanismos clave:

1. **Creación de Copias Privadas**:
   - Cada hilo recibe una copia privada de la variable suma
   - Cada hilo acumula su resultado parcial sin interferir con otros
   - Evita conflicto con otros hilos

2. **Proceso de Combinación de Resultados**:
   - Al finalizar los cálculos parciales, OpenMP:
     * Combina automáticamente todas las sumas individuales en una sola
     * Realiza la combinación en un orden definido
     * Garantiza que no se pierdan actualizaciones

3. **Ventajas sobre una Sección Crítica**:
    - No requiere bloqueos manuales
    - Mejor rendimiento que `#pragma omp critical`
    - Optimizado para operaciones de reducción

4. **Beneficios Reflejados en Nuestros Resultados**:
    - Los valores de suma obtenidos en paralelo son consistentes
    - No hay pérdida de actualizaciones de datos
    - Se mantiene la integridad y precisión de los datos


### Ejercicio 4: Multiplicación de Matrices con Paralelización por Filas
Este ejemplo se implementa la multiplicación de dos matrices cuadradas de NxN.

#### Compilación y Ejecución
1. **Compilar el Programa**
   
   Una vez activado el entorno virtual, debe dirigirse a la carpeta del ejercicio 4
    ```bash
      cd Ejercicio_4
    ```

   Luego, para compilar el programa, utilice el siguiente comando:
    ```bash
      gcc -fopenmp matrix_mult.c -o matrix_mult
    ```
2. **Ejecutar Programa**
   
   Ejecutar el archivo creado:
    ```bash
      ./matrix_mult
    ```
3. **Generar Gráficos de Rendimiento**
   
   Para evidenciar a través de gráficos los resultados, utilice el script de python, ya que importa al archivo **_matrix_mult_**
    ```bash
      python plot_matrix.py
    ```
#### Estructura de archivos
- `matrix_mult.c`: Implementación de la multiplicación de matrices
- `python plot_matrix.py`: Script para visualización de resultados

#### Resultados

**Resultados Detallados por Tamaño de Array**

Al ejecturar **_matrix_mult_** entrega estos resultados:

| Tamaño | Hilos | Tiempo Secuencial (s) | Tiempo Paralelo (s) | Speedup |
|--------|-------|----------------------|-------------------|---------|
| 100    | 2     | 0.003034            | 0.008263         | 0.37    |
| 100    | 4     | 0.003034            | 0.003474         | 0.87    |
| 100    | 8     | 0.003034            | 0.003889         | 0.78    |
| 500    | 2     | 0.618824            | 0.672384         | 0.92    |
| 500    | 4     | 0.618824            | 0.710492         | 0.87    |
| 500    | 8     | 0.618824            | 0.632947         | 0.98    |
| 1000   | 2     | 10.281138           | 10.098008        | 1.02    |
| 1000   | 4     | 10.281138           | 10.262693        | 1.00    |
| 1000   | 8     | 10.281138           | 10.199403        | 1.01    |

Y luego al ejecutar **_python plot_matrix.py_** da un resumen:

| Hilos | Tiempo Secuencial (s) | Tiempo Paralelo (s) |
|-------|----------------------|-------------------|
| 2     | 3.919147            | 3.992622         |
| 4     | 3.919147            | 3.845377         |
| 8     | 3.919147            | 4.086769         |

> **Nota**: Speedup = Tiempo Secuencial / Tiempo Paralelo. Valores > 1 indican mejora de rendimiento.

A continuación se muestran los gráficos de ejemplo al ejecutar el programa:

![alt text](https://github.com/NigsefCode/OpenMP/blob/main/Ejercicio_4/analisis_matrices.png?raw=true)

#### Análisis del Impacto del Tamaño de Matriz y Número de Hilos

1. **Por Tamaño de Matriz**:

    a) **Matrices Pequeñas (N=100)**:

     * Secuencial: 0.003034 segundos
       * El rendimiento paralelo varía:
           - 2 hilos: Más lento (0.008263s)
           - 4 hilos: Ligero incremento (0.003474s)
           - 8 hilos: Degradación moderada (0.003889s)
       * La paralelización no es beneficiosa debido al overhead
  
    b) **Matrices Medianas (N=500)**:

     * Secuencial: 0.618824 segundos
       * Comportamiento paralelo:
           - 2 hilos: 8% más lento
           - 4 hilos: 15% más lento
           - 8 hilos: Solo 2% más lento
       * El overhead sigue superando los beneficios
    
    c) **Matrices Grandes (N=1000)**:

     * Secuencial: 10.281138 segundos
       * Rendimiento paralelo:
           - 2 hilos: Ligera mejora (10.098008s)
           - 4 y 8 hilos: Similar al secuencial
       * Mejores resultados con matrices grandes

3. **Impacto del Número de Hilos**:

    a) **2 Hilos**:

   * Peor en matrices pequeñas
   * Mejor rendimiento en matrices grandes
   * Menos overhead de sincronización
    
    b) **4 Hilos**:

   * Rendimiento variable
   * Mejor en matrices pequeñas que 2 hilos
   * Similar al secuencial en matrices grandes
  
    c) **8 Hilos**:

   * No muestra beneficios significativos
   * Mayor overhead de sincronización
   * Rendimiento inconsistente
    
5. **Conclusiones**:
    
    a) El tamaño de la matriz es crítico:

   * Matrices pequeñas: La paralelización es contraproducente
   * Matrices grandes: Beneficios modestos con 2 hilos
    
    b) El número de hilos afecta inversamente al rendimiento:

   * Más hilos no significa mejor rendimiento
   * El overhead aumenta con el número de hilos
   * Punto óptimo parece estar en 2 hilos para matrices grandes

7. **Recomendaciones**:
   - Usar paralelización solo para matrices grandes (N>1000)
   - Limitar el número de hilos a 2-4
   - Considerar otros enfoques de paralelización para matrices más pequeñas
