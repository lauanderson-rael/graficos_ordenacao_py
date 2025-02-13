import matplotlib.pyplot as plt
import numpy as np
# array = [7, 8, 6, 2, 3, 5, 2, 3, 4, 5]

dados = {
    "Merge Sort": {"min": 714824, "max": 781739},
    "Quick Sort": {"min": 724393, "max": 999707},
    "Bubble Sort": {"min": 790000, "max": 1214479},
    "Counting Sort": {"min": 1882080, "max": 2002992}
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
