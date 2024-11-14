import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import subprocess
import io

def run_and_get_data():
    result = subprocess.run(['./float_sum'], capture_output=True, text=True)
    return pd.read_csv(io.StringIO(result.stdout))

def create_plots(df):
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['axes.grid'] = True

    fig, (ax1, ax2) = plt.subplots(1, 2)

    colors = ['blue', 'red', 'green']
    
    for i, size in enumerate(df['Tamaño'].unique()):
        data_n = df[df['Tamaño'] == size]
        
        # Tiempo de ejecución
        ax1.plot(data_n['Hilos'], data_n['Tiempo Paralelo'], 
                color=colors[i], marker='o', 
                label=f'N={size}')
        ax1.axhline(y=data_n['Tiempo Secuencial'].iloc[0], 
                    color=colors[i], linestyle='--', 
                    label=f'Secuencial N={size}')
    
    ax1.set_xlabel('Número de Hilos')
    ax1.set_ylabel('Tiempo (segundos)')
    ax1.set_title('Tiempo de Ejecución vs Número de Hilos')
    ax1.legend()
    
    # Speedup
    for i, size in enumerate(df['Tamaño'].unique()):
        data_n = df[df['Tamaño'] == size]
        speedup = data_n['Tiempo Secuencial'].iloc[0] / data_n['Tiempo Paralelo']
        
        ax2.plot(data_n['Hilos'], speedup, 
                color=colors[i], marker='o', 
                label=f'N={size}')
    
    ax2.plot(df['Hilos'].unique(), df['Hilos'].unique(), 
            'k--', label='Speedup Ideal')
    ax2.set_xlabel('Número de Hilos')
    ax2.set_ylabel('Speedup')
    ax2.set_title('Speedup vs Número de Hilos')
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('analisis_reduccion.png', bbox_inches='tight', dpi=300)
    plt.show()

if __name__ == "__main__":
    df = run_and_get_data()
    create_plots(df)
    
    print("\nEstadísticas Resumidas:")
    print(df.groupby('Hilos').agg({
        'Tiempo Secuencial': 'mean',
        'Tiempo Paralelo': 'mean'
    }).round(6))
