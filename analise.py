import matplotlib.pyplot as plt

# Configuração para melhorar a exibição de fontes (opcional, mas recomendado)
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']

def criar_graficos_estoque():
    """
    Cria e exibe uma grade 2x2 de gráficos de estoque usando Matplotlib.
    """

    # Cria uma figura e um conjunto de eixos (subplots) 2x2
    # figsize define o tamanho da janela em polegadas (largura, altura)
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    # --- 1. Gráfico de Linha (Tendência de Estoque Diário) ---
    dias = [1, 2, 3, 4, 5, 6, 7]
    estoque_produto_A = [100, 95, 110, 105, 120, 115, 130]

    axs[0, 0].plot(dias, estoque_produto_A, marker='o', linestyle='-', color='b', label='Produto A')
    axs[0, 0].set_title('Tendência de Estoque Diário')
    axs[0, 0].set_xlabel('Dia')
    axs[0, 0].set_ylabel('Quantidade em Estoque')
    axs[0, 0].legend()
    axs[0, 0].grid(True, linestyle='--', alpha=0.6)

    # --- 2. Gráfico de Barras (Comparação de Produtos) ---
    produtos = ['Teclado', 'Mouse', 'Monitor', 'Webcam']
    quantidades = [50, 75, 30, 60]

    # Criando barras com cores diferentes
    cores_barras = ['#4A90E2', '#50E3C2', '#F5A623', '#D0021B']
    axs[0, 1].bar(produtos, quantidades, color=cores_barras)
    axs[0, 1].set_title('Comparação de Quantidade por Produto')
    axs[0, 1].set_xlabel('Produto')
    axs[0, 1].set_ylabel('Quantidade em Estoque')

    # Adiciona rótulos de dados no topo de cada barra
    for i, v in enumerate(quantidades):
        axs[0, 1].text(i, v + 1, str(v), ha='center', fontweight='bold')

    # --- 3. Gráfico de Pizza (Proporção de Categorias) ---
    categorias = ['Eletrônicos', 'Vestuário', 'Alimentos']
    valores = [15000, 8000, 5000]

    # 'explode' destaca uma fatia (opcional)
    explode = (0.05, 0, 0)
    cores_pizza = ['#FFC300', '#FF5733', '#C70039']

    axs[1, 0].pie(valores,
                  labels=categorias,
                  autopct='%1.1f%%',
                  startangle=140,
                  colors=cores_pizza,
                  explode=explode,
                  shadow=True)
    axs[1, 0].set_title('Proporção do Valor Total de Estoque por Categoria')
    axs[1, 0].axis('equal')  # Garante que a pizza seja um círculo

    # --- 4. Gráfico de Dispersão (Preço vs. Quantidade) ---
    precos = [50, 120, 300, 80, 20]
    estoque_dispersao = [80, 25, 10, 70, 150]

    # 's' define o tamanho dos pontos
    axs[1, 1].scatter(precos, estoque_dispersao, alpha=0.7, color='green', s=100)
    axs[1, 1].set_title('Relação Preço (R$) vs. Quantidade em Estoque')
    axs[1, 1].set_xlabel('Preço Unitário (R$)')
    axs[1, 1].set_ylabel('Quantidade em Estoque')
    axs[1, 1].grid(True, linestyle='--', alpha=0.6)

    # --- Finalização ---

    # Adiciona um título geral para toda a figura
    fig.suptitle('Análise Visual de Dados de Estoque', fontsize=16, fontweight='bold')

    # Ajusta o layout para evitar sobreposição de títulos e rótulos
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    # Exibe o gráfico
    plt.show()

# Ponto de entrada do script
if __name__ == "__main__":
    criar_graficos_estoque()