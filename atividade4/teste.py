import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def calcular_frequencias_modos(m1, m2, k):
    """
    Calcula as frequências naturais e modos normais para um sistema periódico de 2 átomos.
    
    Parâmetros:
    m1, m2: massas dos átomos (kg)
    k: constante da mola (N/m)
    
    Retorna:
    frequencias: frequências naturais (rad/s)
    modos: modos normais (autovetores)
    """
    # Matriz dinâmica para o sistema periódico
    D = np.array([[2*k/m1, -k/m1 - k/m1*np.exp(-1j*np.pi)],
                  [-k/m2 - k/m2*np.exp(1j*np.pi), 2*k/m2]])
    
    # Como estamos no ponto q=π (condição periódica), exp(iπ) = -1
    D = np.array([[2*k/m1, -k/m1*(1 - 1)],
                  [-k/m2*(1 - 1), 2*k/m2]])
    
    # Corrigindo a matriz dinâmica para condições periódicas
    # Na verdade, para q=0 e q=π (os pontos importantes da zona de Brillouin)
    # Vamos calcular para ambos os casos
    
    # Para q=0 (modo acústico)
    D_q0 = np.array([[2*k/m1, -k/m1*(1 + 1)],
                     [-k/m2*(1 + 1), 2*k/m2]])
    
    # Para q=π (modo óptico)
    D_qpi = np.array([[2*k/m1, -k/m1*(1 - 1)],
                      [-k/m2*(1 - 1), 2*k/m2]])
    
    # Calculando autovalores e autovetores para q=0
    eigvals_q0, eigvecs_q0 = np.linalg.eig(D_q0)
    freq_q0 = np.sqrt(np.abs(eigvals_q0))  # Frequências em rad/s
    
    # Calculando autovalores e autovetores para q=π
    eigvals_qpi, eigvecs_qpi = np.linalg.eig(D_qpi)
    freq_qpi = np.sqrt(np.abs(eigvals_qpi))  # Frequências em rad/s
    
    return (freq_q0, eigvecs_q0), (freq_qpi, eigvecs_qpi)

def plot_resultados(m2):
    m1 = 1.0  # kg
    k = 1.0   # N/m
    
    (freq_q0, modos_q0), (freq_qpi, modos_qpi) = calcular_frequencias_modos(m1, m2, k)
    
    plt.figure(figsize=(12, 8))
    
    # Plot das frequências
    plt.subplot(2, 2, 1)
    plt.bar(['q=0 (1)', 'q=0 (2)'], freq_q0, color=['blue', 'orange'])
    plt.title(f'Frequências para q=0\nm1={m1}kg, m2={m2}kg')
    plt.ylabel('Frequência (rad/s)')
    
    plt.subplot(2, 2, 2)
    plt.bar(['q=π (1)', 'q=π (2)'], freq_qpi, color=['blue', 'orange'])
    plt.title(f'Frequências para q=π\nm1={m1}kg, m2={m2}kg')
    plt.ylabel('Frequência (rad/s)')
    
    # Plot dos modos normais
    plt.subplot(2, 2, 3)
    for i, modo in enumerate(modos_q0.T):
        plt.plot([0, 1], modo, 'o-', label=f'Modo {i+1}')
    plt.title('Modos normais para q=0')
    plt.xticks([0, 1], ['Átomo 1', 'Átomo 2'])
    plt.ylabel('Deslocamento relativo')
    plt.legend()
    
    plt.subplot(2, 2, 4)
    for i, modo in enumerate(modos_qpi.T):
        plt.plot([0, 1], modo, 'o-', label=f'Modo {i+1}')
    plt.title('Modos normais para q=π')
    plt.xticks([0, 1], ['Átomo 1', 'Átomo 2'])
    plt.ylabel('Deslocamento relativo')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# Interface interativa
plt.figure(figsize=(10, 6))
axcolor = 'lightgoldenrodyellow'
ax_m2 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

s_m2 = Slider(ax_m2, 'Massa m2 (kg)', 1, 10, valinit=1, valstep=0.1)

def update(val):
    m2 = s_m2.val
    plot_resultados(m2)

s_m2.on_changed(update)

plot_resultados(1)  # Valor inicial
plt.show()
