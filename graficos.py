from scipy.interpolate import splrep, splev
import matplotlib.pyplot as plt
import numpy as np
import os

def matrizEnergetica():
    labels = ['Não Renováveis', 'Renováveis']
    sizes = [9.6, 90.4]

    colors = ['#d3d3d3', '#68D391']
    explode = (0.06, 0)

    fig, ax = plt.subplots(figsize=(7, 7), facecolor='none')

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


    plt.title('Distribuição da Matriz Energética', fontsize=18, fontweight='bold', color='#247552')

    plt.setp(autotexts, size=15, weight="bold", color="#247552")

    plt.tight_layout()
    plt.savefig('static/imagens/matrizEnergetica.png')
    
def crescimentoEmpregados():
    x = [2020, 2021, 2022, 2023]
    y = [1.2, 1.27, 1.4, 1.57]

    fig, ax = plt.subplots(figsize=(7, 7), facecolor='none')
    ax.plot(x, y, color='#68D391', linewidth=2)

    plt.title('Crescimento de empregados', fontsize=18, fontweight='bold', color='#247552')
    plt.xticks(x)
    plt.yticks(y)
    ax.set_xlabel('Ano', fontsize=14, fontweight='bold', color='#247552')
    ax.set_ylabel('Empregados (Milhão)', fontsize=14, fontweight='bold', color='#247552')

    ax.grid(True, linestyle='--', color='#d3d3d3', alpha=0.6)

    plt.tight_layout()

    plt.savefig('static/imagens/crescimentoEmpregados.png')

def aumentoEconomiaSolar():
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
    
def energiaSolarSetor():
    labels = ['Residencial', 'Comercial', 'Industrial', 'Público', 'Agrícolo']
    sizes = [30, 40, 15, 10, 5]
    colors = ['#FFB3B3', '#B3FFB3', '#B3C6FF', '#FFB3D9', '#FFCC99']  # Cores mais suaves

    # Criando o gráfico de pizza
    fig, ax = plt.subplots(figsize=(7, 7), facecolor='none')  # Fundo transparente
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        autopct='%.1f%%',
        startangle=120,
        colors=colors,
        wedgeprops=dict(width=0.5, edgecolor='white'),
        textprops=dict(color="#247552", fontsize=14, fontweight='bold')
    )

    # Centraliza o título e aumenta a fonte
    plt.title('Distribuição de uso por setor', fontsize=18, fontweight='bold', color='#247552')

    # Remove o círculo central para visual mais limpo
    plt.setp(autotexts, size=15, weight="bold", color="#247552")

    plt.tight_layout()
    plt.savefig('static/imagens/energiaSolarSetor.png')
    
def energiaHidreletrica():
    # Dados de exemplo
    x = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    y = [375000, 370000, 390000, 402000, 429000, 415000, 390000, 373000, 360000, 380000, 371000, 390000]

    # Criando a interpolação suave
    spl = splrep(x, y, s=0)
    x_new = np.linspace(min(x), max(x), 500)  # Gerando mais pontos no eixo X
    y_new = splev(x_new, spl)  # Avaliando a interpolação para os novos pontos

    # Criando o gráfico de linha
    fig, ax = plt.subplots(figsize=(7, 7), facecolor='none')  # Fundo transparente
    ax.plot(x_new, y_new, color='#68D391', linewidth=2)  # Linha suave sem marcadores

    # Adicionando os pontos originais com marcador
    ax.plot(x, y, color='#68D391', linestyle='', marker='o', markersize=6, markerfacecolor='#247552', markeredgewidth=2, markeredgecolor='#247552')  # Pontos com marcador

    # Adicionando anotações para os pontos originais
    for i in range(len(x)):
        ax.annotate(f'{y[i]}', (x[i], y[i]), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=12, fontweight='bold', color='#247552')

    # Personalização do título
    plt.title('Geração de energia em GWh ', fontsize=18, fontweight='bold', color='#247552')

    # Adicionando rótulos aos eixos com formatação
    plt.xticks(x)

    # Adicionando uma grade leve
    ax.grid(True, linestyle='--', color='#d3d3d3', alpha=0.6)

    # Ajuste de layout para evitar cortes
    plt.tight_layout()
    # Exibindo o gráfico
    plt.savefig('static/imagens/energiaHidreletrica.png')

def setorEnergiaHidrica():
    labels = ['Usinas Grandes', 'Usinas Pequenas e médias', 'Usinas de Reservatório', 'Usinas de Fluxo']
    sizes = [40, 10, 60, 40]
    colors = ['#d3d3d3', '#68D391', '#FFD700', '#FF6347']  # Cinza claro e verde escuro

    # Criando o gráfico de pizza
    fig, ax = plt.subplots(figsize=(7, 7), facecolor='none')  # Fundo transparente
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        autopct='%.1f%%',
        startangle=120,
        colors=colors,
        wedgeprops=dict(width=0.5, edgecolor='white'),
        textprops=dict(color="#247552", fontsize=14, fontweight='bold')
    )

    # Centraliza o título e aumenta a fonte
    plt.title('Distribuição da Energia Hídrica por setor', fontsize=18, fontweight='bold', color='#247552')

    # Remove o círculo central para visual mais limpo
    plt.setp(autotexts, size=15, weight="bold", color="#247552")

    plt.tight_layout()
    plt.savefig('static/imagens/setorEnergiaHidrica.png')
    
def geracaoEolica():
    # Dados de potência de geração em MW para os estados do Brasil
    estados = [
    "Rio Grande do Norte",
    "Bahia",
    "Piauí",
    "Ceará",
    "Rio Grande do Sul",
    "Pernambuco",
    "Paraíba",
    "Maranhão",
    "Santa Catarina",
    "Sergipe",
    "Rio de Janeiro",
    "Paraná"
]

    potenciaGeracao = [
        7872,  # Rio Grande do Norte
        7633,  # Bahia
        3583,  # Piauí
        6204,  # Ceará (corrigido de acordo com o ranking)
        1358,  # Rio Grande do Sul
        1061,  # Pernambuco
        765,   # Paraíba
        426,   # Maranhão
        242,   # Santa Catarina
        110,   # Sergipe
        28.05, # Rio de Janeiro
        24.1   # Paraná
    ]
    # Criando o gráfico de barras
    plt.figure(figsize=(12, 6))
    plt.bar(estados, potenciaGeracao, color='green')
    plt.title('Potências de Geração Eólica nos Estados do Brasil')
    plt.xlabel('Estados')
    plt.ylabel('Potência de Geração (GWh)')
    plt.grid(axis='y', alpha=0.8)
    plt.xticks(rotation=45)
    plt.savefig('static/imagens/geracaoEolica.png')

def geracaoBiomassa():
    #Dados das fontes de energia
    fontes_energia = ['Biomassa (62,2%)', 'Gás industrial (0,9%)', 'Biodiesel (2,1%)',
    'Outros energéticos da biomassa (2,2%)','Lenha (4,7%)',
    'Lixivia (27,0%)','Resíduos sólidos (0,9%)']
    proporcoes = [62.2,0.9,2.1, 2.2,4.7,27.0, 0.9]

    #Criando o gráfico de pizza
    plt.figure(figsize=(8, 5))
    plt.pie(proporcoes, labels=fontes_energia, autopct= None, startangle=140)
    plt.title('Tipos de Biomassa mais utilizados no Brasil')
    plt.axis('equal') # Para garantir que o gráfico seja um círculo
    plt.savefig('static/imagens/geracaoBiomassa.png')

def geracaoGeotermica():
# Dados de capacidade máxima de armazenamento em MW
    regioes = ['Sudeste/Centro-Oeste', 'Sul', 'Nordeste', 'Norte']
    capacidades = [204615.328, 20459.242, 51691.227, 15302.397]

    # Calcular o total
    total_capacidade = sum(capacidades)

    # Calcular as porcentagens
    proporcoes = [(capacidade / total_capacidade) * 100 for capacidade in capacidades]

    # Criando o gráfico de pizza
    plt.figure(figsize=(8, 5))
    wedges, texts, autotexts = plt.pie(proporcoes, labels=regioes, autopct='%1.1f%%', startangle=140)

    plt.title('Capacidade máxima de armazenamento MW/mês por estado', fontsize=16)
    plt.axis('equal')  # Para garantir que o gráfico seja um círculo
    plt.savefig('static/imagens/geracaoGeotermica.png')

def geracaoOceanica():
    # Dados da tabela
    regioes = ['Norte (marés)', 'Nordeste (ondas)', 'Sudeste (ondas)', 'Sul (ondas)']
    potencia_gw = [27, 22, 30, 35]
    cor_total = 'firebrick'  # Cor para a barra do total

    # Criar gráfico
    plt.figure(figsize=(10, 6))
    bars = plt.bar(regioes, potencia_gw, color=['#4CAF50', '#2196F3', '#FFC107', '#9C27B0'], alpha=0.8, edgecolor='black')

    # Adicionar barra do TOTAL (opcional)
    plt.bar('TOTAL', sum(potencia_gw), color=cor_total, alpha=0.6, hatch='//', edgecolor=cor_total)

    # Personalização
    plt.title('Potencial Energético Teórico por Região do Brasil\n(Fonte: ENERGIAS RENOVÁVEIS E SUSTENTABILIDADE, 2012)', 
            fontsize=14, pad=20, fontweight='bold')
    plt.xlabel('Regiões e Fonte de Energia', fontsize=12)
    plt.ylabel('Potência (GW)', fontsize=12)
    plt.xticks(rotation=45, ha='right')  # Rotacionar rótulos para legibilidade
    plt.grid(axis='y', linestyle='--', alpha=0.4)

    # Adicionar valores nas barras
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f'{height} GW', 
                ha='center', va='bottom', fontsize=10)

    # Destacar o total
    plt.text(3.8, sum(potencia_gw)+2, f'TOTAL: {sum(potencia_gw)} GW', 
            color=cor_total, fontsize=12, fontweight='bold')

    plt.tight_layout()  # Ajustar layout
    plt.savefig('static/imagens/geracaoOceanica.png')

