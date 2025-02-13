# intervalo de 0 a 8 em 10.000 posições
import matplotlib.pyplot as plt
import numpy as np


dados = {
    "Counting Sort": {"min": 2100403, "max": 3055201},  # ✅ Mais rápido
    "Merge Sort": {"min": 2291910, "max": 3016933},
    "Quick Sort": {"min": 14143838, "max": 18967565},
    "Bubble Sort": {"min": 54081589, "max": 60027552}  # ❌ Mais lento
}

algoritmos = list(dados.keys())
valores_media = [(dados[alg]["min"] + dados[alg]["max"]) / 2 for alg in algoritmos]

x = np.arange(len(algoritmos))  # Posições no eixo X
cores = ['green', 'blue', 'orange', 'red']  # Destaque para o mais rápido e o mais lento

fig, ax = plt.subplots()
barras = ax.bar(x, valores_media, color=cores)

ax.set_xlabel('Algoritmos')
ax.set_ylabel('Tempo Médio (ns)')
ax.set_title('Comparação de Desempenho dos Algoritmos de Ordenação')
ax.set_xticks(x)
ax.set_xticklabels(algoritmos)

# Adicionando os valores da média acima das colunas
for barra, valor in zip(barras, valores_media):
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2, altura, f'{int(valor)}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.show()
