Análise Visual de Dados de Estoque

Este script Python foi criado para facilitar a análise de dados de estoque. Em vez de olhar apenas para tabelas, ele usa a biblioteca matplotlib para gerar um painel (dashboard) 2x2 com quatro gráficos diferentes, permitindo uma compreensão visual e rápida da situação do estoque.

Ao rodar o script, ele abre uma única janela que exibe os quatro gráficos a seguir:
Gráfico de Linha (Tendência Diária): Permite ver a variação da quantidade de um produto específico ao longo de 7 dias.
Gráfico de Barras (Comparação): Coloca lado a lado a quantidade em estoque de quatro produtos diferentes (Teclado, Mouse, Monitor, Webcam).
Gráfico de Pizza (Proporção das Categorias): Mostra a participação percentual de cada categoria (Eletrônicos, Vestuário, Alimentos) no valor total do estoque.
Gráfico de Dispersão (Preço vs. Quantidade): Ajuda a analisar a correlação entre o preço unitário de um item e a quantidade disponível em estoque.

Requisitos:
Este script requer a biblioteca matplotlib. O código recomenda o uso da fonte DejaVu Sans para uma melhor renderização, mas ela geralmente já vem incluída na instalação padrão do matplotlib.
Você pode instalar a biblioteca necessária usando pip:
pip install matplotlib


Como Executar:
Primeiro, certifique-se de que você tem o Python e o matplotlib instalados no seu computador.
Salve o código principal em um arquivo Python (por exemplo, analise_estoque.py).
Abra seu terminal e execute o script com o comando:
python analise_estoque.py


Após a execução, uma nova janela deve aparecer, exibindo o dashboard "Análise de Dados de Estoque" com os quatro gráficos.
