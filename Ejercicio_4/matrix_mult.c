#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

void initialize_matrix(double** matrix, int N) {
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            matrix[i][j] = (double)rand() / RAND_MAX;
        }
    }
}

double** allocate_matrix(int N) {
    double** matrix = (double**)malloc(N * sizeof(double*));
    for(int i = 0; i < N; i++) {
        matrix[i] = (double*)malloc(N * sizeof(double));
    }
    return matrix;
}

void free_matrix(double** matrix, int N) {
    for(int i = 0; i < N; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

double sequential_multiply(double** A, double** B, double** C, int N) {
    double start_time = omp_get_wtime();
    
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            C[i][j] = 0.0;
            for(int k = 0; k < N; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    
    return omp_get_wtime() - start_time;
}

double parallel_multiply(double** A, double** B, double** C, int N, int num_threads) {
    double start_time = omp_get_wtime();
    
    #pragma omp parallel for num_threads(num_threads)
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            C[i][j] = 0.0;
            for(int k = 0; k < N; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    
    return omp_get_wtime() - start_time;
}

int main() {
    int sizes[] = {100, 500, 1000};
    int thread_counts[] = {2, 4, 8};
    srand(time(NULL));
    
    printf("Tamaño,Hilos,Tiempo Secuencial,Tiempo Paralelo\n");
    
    for(int s = 0; s < 3; s++) {
        int N = sizes[s];
        
        // Asignar matrices
        double** A = allocate_matrix(N);
        double** B = allocate_matrix(N);
        double** C = allocate_matrix(N);
        
        // Inicializar matrices A y B
        initialize_matrix(A, N);
        initialize_matrix(B, N);
        
        // Multiplicación secuencial
        double time_seq = sequential_multiply(A, B, C, N);
        
        // Multiplicaciones paralelas
        for(int t = 0; t < 3; t++) {
            double time_par = parallel_multiply(A, B, C, N, thread_counts[t]);
            printf("%d,%d,%f,%f\n", N, thread_counts[t], time_seq, time_par);
        }
        
        // Liberar memoria
        free_matrix(A, N);
        free_matrix(B, N);
        free_matrix(C, N);
    }
    
    return 0;
}
