import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.linalg import eigh_tridiagonal

# Função usada para gerar o grafico estático do modo 0 (translação global)

# Parâmetros
N = 100
defect_fraction = 0.05
m = 1.0
k = 1.0
np.random.seed(0)

# Gerar massas (sem defeitos)
masses = np.full(N, m)

# Calcular matriz dinâmica
main_diag = np.zeros(N)
main_diag[0] = k / masses[0]
main_diag[-1] = k / masses[-1]
if N > 2:
    main_diag[1:-1] = 2 * k / masses[1:-1]

off_diag = np.zeros(N-1)
for i in range(N-1):
    off_diag[i] = -k / np.sqrt(masses[i] * masses[i+1])

# Obter autovalores e autovetores
eigenvals, eigenvecs = eigh_tridiagonal(main_diag, off_diag)

# Modo 0 (translação global)
mode_index = 0
omega = 0  # Forçar omega = 0
mode_vector = np.ones(N)  # Autovetor constante

# Configurar animação
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, N)
ax.set_ylim(-1.5, 1.5)
ax.set_title('Modo 0: Translação Global (ω=0) - Sem Vibração', fontsize=14)
ax.set_xlabel('Posição do Átomo', fontsize=12)
ax.set_ylabel('Deslocamento', fontsize=12)

# Elementos do gráfico
line, = ax.plot([], [], 'o-', markersize=4)
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=12)
info_text = ax.text(0.02, 0.85, 'Todos os átomos se movem juntos\nsem vibração relativa', 
                   transform=ax.transAxes, fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

# Função de inicialização
def init():
    line.set_data(np.arange(N), mode_vector)
    time_text.set_text('Tempo: 0.00 s')
    return line, time_text, info_text

# Função de animação (estática)
def animate(t):
    # Deslocamento constante (não muda com o tempo)
    line.set_data(np.arange(N), mode_vector)
    time_text.set_text(f'Tempo: {t:.2f} s')
    return line, time_text, info_text

# Criar animação (com tempo simulado)
ani = FuncAnimation(
    fig, animate,
    frames=np.linspace(0, 10, 100),  # 10 segundos de simulação
    init_func=init,
    blit=True,
    interval=50
)

plt.tight_layout()
ani.save('modo0_translacao_05defeitos.gif', writer='pillow', fps=20)
plt.close()

print("Animação do modo 0 (translação global) salva com sucesso!")