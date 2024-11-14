import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import subprocess
import io

def run_and_get_data():
    # Ejecutar el programa C y capturar la salida
    result = subprocess.run(['./random_increments'], capture_output=True, text=True)
    # Convertir la salida a DataFrame
    return pd.read_csv(io.StringIO(result.stdout))

def create_plots(df):
    # Configurar el estilo básico
    plt.rcParams['figure.figsize'] = (12, 15)
    plt.rcParams['axes.grid'] = True
    
    # Crear una figura con tres subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    
    # Colores para diferentes tamaños de array
    colors = ['blue', 'red', 'green']
    
    # Para cada tamaño de array
    for i, N in enumerate(df['Tamaño Array'].unique()):
        data_n = df[df['Tamaño Array'] == N]
        
        # 1. Gráfico de tiempo de ejecución
        ax1.plot(data_n['Num Hilos'], data_n['Tiempo Sin Sync'], 
                color=colors[i], marker='o', label=f'Sin Sync (N={N})')
        ax1.plot(data_n['Num Hilos'], data_n['Tiempo Con Sync'], 
                color=colors[i], marker='s', linestyle='--', label=f'Con Sync (N={N})')
    
    ax1.set_xlabel('Número de Hilos')
    ax1.set_ylabel('Tiempo (segundos)')
    ax1.set_title('Tiempo de Ejecución vs Número de Hilos')
    ax1.legend()
    
    # 2. Gráfico de precisión
    for i, N in enumerate(df['Tamaño Array'].unique()):
        data_n = df[df['Tamaño Array'] == N]
        error_no_sync = abs(data_n['Suma Sin Sync'] - data_n['Suma Esperada']) / data_n['Suma Esperada'] * 100
        error_sync = abs(data_n['Suma Con Sync'] - data_n['Suma Esperada']) / data_n['Suma Esperada'] * 100
        
        ax2.plot(data_n['Num Hilos'], error_no_sync, 
                color=colors[i], marker='o', label=f'Sin Sync (N={N})')
        ax2.plot(data_n['Num Hilos'], error_sync, 
                color=colors[i], marker='s', linestyle='--', label=f'Con Sync (N={N})')
    
    ax2.set_xlabel('Número de Hilos')
    ax2.set_ylabel('Error Porcentual')
    ax2.set_title('Error en la Suma vs Número de Hilos')
    ax2.legend()
    
    # 3. Gráfico de speedup
    for i, N in enumerate(df['Tamaño Array'].unique()):
        data_n = df[df['Tamaño Array'] == N]
        time_sequential = data_n[data_n['Num Hilos'] == 1]['Tiempo Con Sync'].iloc[0]
        speedup_sync = time_sequential / data_n['Tiempo Con Sync']
        speedup_no_sync = time_sequential / data_n['Tiempo Sin Sync']
        
        ax3.plot(data_n['Num Hilos'], speedup_no_sync, 
                color=colors[i], marker='o', label=f'Sin Sync (N={N})')
        ax3.plot(data_n['Num Hilos'], speedup_sync, 
                color=colors[i], marker='s', linestyle='--', label=f'Con Sync (N={N})')
    
    ax3.plot(df['Num Hilos'].unique(), df['Num Hilos'].unique(), 
            'k--', label='Speedup Ideal')
    ax3.set_xlabel('Número de Hilos')
    ax3.set_ylabel('Speedup')
    ax3.set_title('Speedup vs Número de Hilos')
    ax3.legend()
    
    plt.tight_layout()
    plt.savefig('analisis_incrementos.png', bbox_inches='tight', dpi=300)
    plt.show()

if __name__ == "__main__":
    df = run_and_get_data()
    create_plots(df)
    
    # Imprimir estadísticas resumidas
    print("\nEstadísticas Resumidas:")
    print("\nPromedio de tiempos y errores por número de hilos:")
    summary = df.groupby('Num Hilos').agg({
        'Tiempo Sin Sync': 'mean',
        'Tiempo Con Sync': 'mean',
        'Suma Sin Sync': lambda x: (abs(x - df['Suma Esperada'])/df['Suma Esperada']*100).mean(),
        'Suma Con Sync': lambda x: (abs(x - df['Suma Esperada'])/df['Suma Esperada']*100).mean()
    }).round(4)
    print(summary)
