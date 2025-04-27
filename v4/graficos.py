import matplotlib.pyplot as plt
import os

def matrizEnergetica():
    labels = ['Não Renováveis', 'Renováveis']
    sizes = [9.6, 90.4]
    colors = ['#d3d3d3', '#68D391']  # Cinza claro e verde escuro
    explode = (0.06, 0)              # Explode sutil para Não Renováveis

    # Criando o gráfico de pizza
    fig, ax = plt.subplots(figsize=(7, 7), facecolor='none')  # Fundo transparente
    wedges, texts, autotexts = ax.pie(
        sizes,
        explode=explode,
        labels=labels,
        autopct='%.1f%%',
        startangle=120,
        colors=colors,
        wedgeprops=dict(width=0.5, edgecolor='white'),
        textprops=dict(color="#247552", fontsize=14, fontweight='bold')
    )

    # Centraliza o título e aumenta a fonte
    plt.title('Distribuição da Matriz Energética', fontsize=18, fontweight='bold', color='#247552')

    # Remove o círculo central para visual mais limpo
    plt.setp(autotexts, size=15, weight="bold", color="#247552")

    plt.tight_layout()
    plt.savefig('static/imagens/matrizEnergetica.png')