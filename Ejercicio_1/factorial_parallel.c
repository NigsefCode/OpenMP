#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

// Función para calcular factorial
unsigned long long factorial(int n) {
    unsigned long long fact = 1;
    for(int i = 2; i <= n; i++) {
        fact *= i;
    }
    return fact;
}

// Función para medir tiempo de ejecución secuencial
double calcular_secuencial(int N, unsigned long long* resultados) {
    double inicio = omp_get_wtime();
    
    for(int i = 1; i <= N; i++) {
        resultados[i-1] = factorial(i);
    }
    
    double fin = omp_get_wtime();
    return fin - inicio;
}

// Función para medir tiempo de ejecución paralela
double calcular_paralelo(int N, unsigned long long* resultados, int num_hilos) {
    double inicio = omp_get_wtime();
    
    #pragma omp parallel for num_threads(num_hilos)
    for(int i = 1; i <= N; i++) {
        resultados[i-1] = factorial(i);
    }
    
    double fin = omp_get_wtime();
    return fin - inicio;
}

int main() {
    int N = 20; // Número máximo para calcular factoriales
    unsigned long long* resultados = (unsigned long long*)malloc(N * sizeof(unsigned long long));
    
    // Prueba secuencial
    printf("Versión Secuencial:\n");
    double tiempo_sec = calcular_secuencial(N, resultados);
    printf("Tiempo de ejecución secuencial: %f segundos\n\n", tiempo_sec);
    
    // Pruebas paralelas con diferentes números de hilos
    int num_hilos[] = {1, 2, 4, 8};
    double tiempos_paralelos[4];
    
    printf("Versiones Paralelas:\n");
    for(int i = 0; i < 4; i++) {
        tiempos_paralelos[i] = calcular_paralelo(N, resultados, num_hilos[i]);
        printf("Tiempo con %d hilos: %f segundos\n", 
               num_hilos[i], tiempos_paralelos[i]);
        printf("Speedup con %d hilos: %f\n\n", 
               num_hilos[i], tiempo_sec/tiempos_paralelos[i]);
    }
    
    // Verificación de resultados
    printf("Primeros 5 resultados de verificación:\n");
    for(int i = 0; i < 5; i++) {
        printf("Factorial de %d: %llu\n", i+1, resultados[i]);
    }
    
    free(resultados);
    return 0;
}
