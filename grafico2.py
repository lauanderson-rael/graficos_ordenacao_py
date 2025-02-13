'''
Array = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]

de 0 a 100 elementos
'''

import matplotlib.pyplot as plt
import numpy as np

dados = {
    "Quick Sort": {"min": 273430, "max": 657348},  # ✅ Mais rápido
    "Merge Sort": {"min": 949913, "max": 1262802},
    "Bubble Sort": {"min": 1009977, "max": 1423438},
    "Counting Sort": {"min": 1164955, "max": 2062904}  # ❌ Mais lento
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
