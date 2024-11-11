import matplotlib.pyplot as plt
import numpy as np
import subprocess
import re

def ejecutar_factorial_parallel():
    # Ejecuta el programa y captura su salida
    resultado = subprocess.run(['./factorial_parallel'], capture_output=True, text=True)
    return resultado.stdout

def extraer_datos(output):
    # Extraer tiempo secuencial
    tiempo_sec_match = re.search(r'Tiempo de ejecución secuencial: ([0-9.]+) segundos', output)
    tiempo_secuencial = float(tiempo_sec_match.group(1)) if tiempo_sec_match else 0

    # Extraer tiempos paralelos y speedups
    tiempos = []
    speedups = []
    hilos = []
    
    # Buscar todas las ocurrencias de tiempos y speedups
    tiempo_matches = re.finditer(r'Tiempo con (\d+) hilos: ([0-9.]+) segundos', output)
    speedup_matches = re.finditer(r'Speedup con \d+ hilos: ([0-9.]+)', output)
    
    for t_match, s_match in zip(tiempo_matches, speedup_matches):
        hilos.append(int(t_match.group(1)))
        tiempos.append(float(t_match.group(2)))
        speedups.append(float(s_match.group(1)))

    return tiempo_secuencial, hilos, tiempos, speedups

def crear_graficos(tiempo_secuencial, hilos, tiempos, speedups):
    plt.rcParams['figure.figsize'] = (15, 6)
    plt.rcParams['axes.grid'] = True

    fig, (ax1, ax2) = plt.subplots(1, 2)

    # Gráfico 1: Tiempo de ejecución
    ax1.plot(hilos, tiempos, 'b-o', linewidth=2, markersize=8, label='Tiempo Paralelo')
    ax1.axhline(y=tiempo_secuencial, color='r', linestyle='--', label='Tiempo Secuencial')
    ax1.set_xlabel('Número de Hilos')
    ax1.set_ylabel('Tiempo de Ejecución (segundos)')
    ax1.set_title('Tiempo de Ejecución vs Número de Hilos')
    ax1.grid(True)
    ax1.legend()
    ax1.set_yscale('log')
    ax1.set_xticks(hilos)

    # Gráfico 2: Speedup
    ax2.plot(hilos, speedups, 'g-o', linewidth=2, markersize=8, label='Speedup Real')
    ax2.plot(hilos, hilos, 'r--', label='Speedup Ideal')
    ax2.set_xlabel('Número de Hilos')
    ax2.set_ylabel('Speedup')
    ax2.set_title('Speedup vs Número de Hilos')
    ax2.grid(True)
    ax2.legend()
    ax2.set_xticks(hilos)

    plt.tight_layout()
    fig.suptitle('Análisis de Rendimiento: Cálculo de Factoriales en Paralelo', y=1.05, fontsize=14)
    
    # Guardar el gráfico con timestamp
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plt.savefig(f'analisis_rendimiento_factorial_{timestamp}.png', bbox_inches='tight', dpi=300)
    
    plt.show()

def main():
    try:
        # Ejecutar el programa y obtener su salida
        output = ejecutar_factorial_parallel()
        
        # Extraer los datos de la salida
        tiempo_secuencial, hilos, tiempos, speedups = extraer_datos(output)
        
        # Imprimir los datos extraídos
        print("\nDatos extraídos:")
        print(f"Tiempo Secuencial: {tiempo_secuencial:.6f} segundos")
        print("\nTiempos Paralelos:")
        for h, t, s in zip(hilos, tiempos, speedups):
            print(f"Hilos: {h}, Tiempo: {t:.6f} s, Speedup: {s:.6f}")
        
        # Crear los gráficos
        crear_graficos(tiempo_secuencial, hilos, tiempos, speedups)
        
    except Exception as e:
        print(f"Error: {e}")
        print("Asegúrate de que el programa factorial_parallel está compilado y en el mismo directorio")

if __name__ == "__main__":
    main()
