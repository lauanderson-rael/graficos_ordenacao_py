# em intervalos com 1000 posições de números entre 1 a 1000
# sem repeticao
import matplotlib.pyplot as plt
import numpy as np

dados = {
    "Merge Sort": {"min": 812246, "max": 1147482},
    "Quick Sort": {"min": 1422444, "max": 1528043},
    "Bubble Sort": {"min": 4174725, "max": 4399540},
    "Counting Sort": {"min": 1279201, "max": 1483973}
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
