#intervalo de 0 a 8 de 100.000 posições
import matplotlib.pyplot as plt
import numpy as np

dados = {
    "Counting Sort": {"min": 5922685, "max": 7411703},  # ✅ Mais rápido
    "Merge Sort": {"min": 12567672, "max": 16003937},
    "Quick Sort": {"min": 336762104, "max": 340039347},
    "Bubble Sort": {"min": 4682802808, "max": 4756328790}  # ❌ Mais lento
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
