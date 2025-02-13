import matplotlib.pyplot as plt
import numpy as np

dados = {
    "Merge Sort": {"min": 94354, "max": 126900},
    "Quick Sort": {"min": 540075, "max": 662992},
    "Bubble Sort": {"min": 173274, "max": 199743},
    "Counting Sort": {"min": 962050, "max": 1164863}
}

algoritmos = list(dados.keys())
valores_media = [(dados[alg]["min"] + dados[alg]["max"]) / 2 for alg in algoritmos]

x = np.arange(len(algoritmos))  # Posições no eixo X
cores = ['blue', 'green', 'orange', 'red']  # Cores diferentes para cada coluna

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
