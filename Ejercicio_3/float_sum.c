#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

void generate_random_array(float* arr, int size) {
    for(int i = 0; i < size; i++) {
        arr[i] = (float)rand() / RAND_MAX;
    }
}

double sequential_sum(float* arr, int size, float* result) {
    double start_time = omp_get_wtime();
    *result = 0.0f;
    
    for(int i = 0; i < size; i++) {
        *result += arr[i];
    }
    
    return omp_get_wtime() - start_time;
}

double parallel_sum(float* arr, int size, float* result, int num_threads) {
    double start_time = omp_get_wtime();
    float suma = 0.0f;
    
    #pragma omp parallel num_threads(num_threads) reduction(+:suma)
    {
        #pragma omp for
        for(int i = 0; i < size; i++) {
            suma += arr[i];
        }
    }
    
    *result = suma;
    return omp_get_wtime() - start_time;
}

int main() {
    int sizes[] = {1000000, 10000000, 100000000};
    int thread_counts[] = {2, 4, 8};
    
    printf("Tamaño,Hilos,Tiempo Secuencial,Tiempo Paralelo,Suma Secuencial,Suma Paralela\n");
    
    for(int s = 0; s < 3; s++) {
        int size = sizes[s];
        float* arr = (float*)malloc(size * sizeof(float));
        
        generate_random_array(arr, size);
        
        float sum_seq, sum_par;
        double time_seq = sequential_sum(arr, size, &sum_seq);
        
        for(int t = 0; t < 3; t++) {
            int num_threads = thread_counts[t];
            double time_par = parallel_sum(arr, size, &sum_par, num_threads);
            
            printf("%d,%d,%f,%f,%f,%f\n", 
                   size, num_threads, time_seq, time_par, sum_seq, sum_par);
        }
        
        free(arr);
    }
    
    return 0;
}
