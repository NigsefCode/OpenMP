#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

// Función para sumar todos los elementos del array
long long sum_array(int* arr, int N) {
    long long sum = 0;
    for(int i = 0; i < N; i++) {
        sum += arr[i];
    }
    return sum;
}

// Función para realizar incrementos sin sincronización
double increment_no_sync(int* arr, int N, int M, int num_threads) {
    double start_time = omp_get_wtime();
    
    #pragma omp parallel num_threads(num_threads)
    {
        unsigned int seed = omp_get_thread_num(); // Semilla única para cada hilo
        for(int i = 0; i < M; i++) {
            int pos = rand_r(&seed) % N;
            arr[pos]++;
        }
    }
    
    return omp_get_wtime() - start_time;
}

// Función para realizar incrementos con sincronización
double increment_with_sync(int* arr, int N, int M, int num_threads) {
    double start_time = omp_get_wtime();
    
    #pragma omp parallel num_threads(num_threads)
    {
        unsigned int seed = omp_get_thread_num();
        for(int i = 0; i < M; i++) {
            int pos = rand_r(&seed) % N;
            #pragma omp critical
            {
                arr[pos]++;
            }
        }
    }
    
    return omp_get_wtime() - start_time;
}

int main() {
    // Parámetros de prueba
    int N_values[] = {1000, 10000, 100000};
    int M_values[] = {1000, 10000, 100000};
    int thread_counts[] = {1, 2, 4, 8};
    
    printf("Tamaño Array,Iteraciones,Num Hilos,Tiempo Sin Sync,Tiempo Con Sync,Suma Sin Sync,Suma Con Sync,Suma Esperada\n");
    
    // Pruebas con diferentes combinaciones
    for(int n = 0; n < 3; n++) {
        int N = N_values[n];
        
        for(int m = 0; m < 3; m++) {
            int M = M_values[m];
            
            for(int t = 0; t < 4; t++) {
                int num_threads = thread_counts[t];
                
                // Arrays para pruebas sin y con sincronización
                int* arr_no_sync = (int*)calloc(N, sizeof(int));
                int* arr_sync = (int*)calloc(N, sizeof(int));
                
                // Realizar incrementos sin sincronización
                double time_no_sync = increment_no_sync(arr_no_sync, N, M, num_threads);
                long long sum_no_sync = sum_array(arr_no_sync, N);
                
                // Realizar incrementos con sincronización
                double time_with_sync = increment_with_sync(arr_sync, N, M, num_threads);
                long long sum_sync = sum_array(arr_sync, N);
                
                // Suma esperada (M incrementos por cada hilo)
                long long expected_sum = (long long)M * num_threads;
                
                // Imprimir resultados
                printf("%d,%d,%d,%f,%f,%lld,%lld,%lld\n", 
                       N, M, num_threads, 
                       time_no_sync, time_with_sync,
                       sum_no_sync, sum_sync, expected_sum);
                
                free(arr_no_sync);
                free(arr_sync);
            }
        }
    }
    
    return 0;
}
