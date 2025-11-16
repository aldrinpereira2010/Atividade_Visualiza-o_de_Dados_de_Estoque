 Visualização de Dados de Estoque com Matplotlib

Este é um script Python que utiliza a biblioteca matplotlib para gerar um dashboard 2x2, apresentando quatro tipos diferentes de gráficos para análise de dados de estoque.

 Dashboard Gerado

O script gera uma única janela com os seguintes quatro gráficos:

Gráfico de Linha (Tendência de Estoque Diário): Mostra a variação da quantidade de um produto ao longo de 7 dias.

Gráfico de Barras (Comparação de Produtos): Compara a quantidade em estoque de quatro produtos diferentes (Teclado, Mouse, Monitor, Webcam).

Gráfico de Pizza (Proporção de Categorias): Exibe a proporção percentual do valor de estoque dividido por categorias (Eletrônicos, Vestuário, Alimentos).

Gráfico de Dispersão (Preço vs. Quantidade): Analisa a correlação entre o preço unitário de um item e a quantidade disponível em estoque.


Dica: Rode o script, tire um print screen (captura de tela) da janela do gráfico, salve como uma imagem (ex: dashboard_estoque.png) no seu repositório e descomente a linha abaixo para exibi-la aqui!



 Requisitos

Este script requer a biblioteca matplotlib. A fonte DejaVu Sans é recomendada no código para melhor renderização, mas geralmente já vem incluída na instalação padrão do matplotlib.

Você pode instalar a biblioteca necessária usando pip:

pip install matplotlib


 Como Executar

Certifique-se de que você tem o Python e o matplotlib instalados.

Salve o código principal em um arquivo Python (por exemplo, analise_estoque.py).

Execute o script através do seu terminal:

python analise_estoque.py


Após a execução, uma janela pop-up do Matplotlib será aberta, exibindo o dashboard "Análise Visual de Dados de Estoque" com os quatro gráficos.
