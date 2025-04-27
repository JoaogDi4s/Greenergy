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
    
def crescimentoEmpregados():
    # Dados de exemplo
    x = [2020, 2021, 2022, 2023]
    y = [1.2, 1.27, 1.4, 1.57]

    # Criando o gráfico de linha
    fig, ax = plt.subplots(figsize=(7, 7), facecolor='none')  # Fundo transparente
    ax.plot(x, y, color='#68D391', linewidth=2)  # Cor verde escuro para a linha

    # Personalização do título
    plt.title('Crescimento de empregados', fontsize=18, fontweight='bold', color='#247552')

    # Adicionando rótulos aos eixos com formatação
    plt.xticks(x)
    plt.yticks(y)
    ax.set_xlabel('Ano', fontsize=14, fontweight='bold', color='#247552')
    ax.set_ylabel('Empregados (Milhão)', fontsize=14, fontweight='bold', color='#247552')

    # Adicionando uma grade leve
    ax.grid(True, linestyle='--', color='#d3d3d3', alpha=0.6)

    # Ajuste de layout para evitar cortes
    plt.tight_layout()

    # Salvando a imagem com fundo transparente
    plt.savefig('static/imagens/crescimentoEmpregados.png')

def aumentoEconomiaSolar():
# Dados de exemplo
    x = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    y = [110, 275, 495, 770, 1100, 1485, 1925, 2370, 2870, 3420, 4020, 4670]

    # Criando o gráfico de linha
    fig, ax = plt.subplots(figsize=(7, 7), facecolor='none')  # Fundo transparente
    ax.plot(x, y, color='#68D391', linewidth=2, marker='o', markersize=4, markerfacecolor='#247552', markeredgewidth=2, markeredgecolor='#247552') # Cor verde escuro para a linha

    for i in range(len(x)):
            ax.annotate(f'{y[i]}', (x[i], y[i]), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=12, fontweight='bold', color='#247552')
            
    # Personalização do título
    plt.title('Economia com placas solares', fontsize=18, fontweight='bold', color='#247552')

    # Adicionando rótulos aos eixos com formatação
    plt.xticks(x)
    plt.yticks(y)
    ax.set_xlabel('Ano', fontsize=14, fontweight='bold', color='#247552')
    ax.set_ylabel('Economia Total Acumulada (Mi)', fontsize=14, fontweight='bold', color='#247552')

    # Adicionando uma grade leve
    ax.grid(True, linestyle='--', color='#d3d3d3', alpha=0.6)

    # Ajuste de layout para evitar cortes
    plt.tight_layout()
    # Salvando a imagem com fundo transparente
    plt.savefig('static/imagens/aumentoEconomiaSolar.png')