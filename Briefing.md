# Trabalho Final: Briefing
Aluno: Lucas Bryan Treuke

---

## Escolha da base
A base escolhida foi "_[Macros of popular high protein foods](https://www.kaggle.com/datasets/fydrose/macros-of-popular-high-protein-foods)_", no Kaggle.
A escolha foi feita, pois eu estava com um pouco de curiosidade sobre como montar uma visualização para alimentos, e encontrei esse dataset explorando o Kaggle (sendo um espaço que eu já conhecia e que possui diversos datasets interessantes), e como ele parecia estar bom para uso eu decidi utilizá-lo. Além disso, eu queria submeter-me a um desafio que seria montar uma visualização sobre uma base muito diferente das que estou habituado.

## Inspirações
A inspiração para a visualização veio da falta de opções criativas e interativas para exibir dados nutricionais de alimentos. Ao pesquisar visualizações de nutrientes em alimentos eu não encontrei nada que se distanciasse da tabela de informação nutricional, ou alguns infográficos simples, então pensei em fazer um gráfico que mostrasse a distribuição dos alimentos em um plano conforme sua quantidade de gordura e proteína, então vou usar um scatterplot, já que é um bom gráfico para exibir distribuições.

## Objetivo
A minha ambição para o projeto final de visualização seria criar uma visualização interativa que explorasse a funcionalidade de _hover_ na exibição, isso, pois eu acredito no poder informativo de um gráfico simples, apenas com uma visão mais superficial de informação, integrado a uma visualização mais detalhada à medida que um tópico é escolhido. No meu caso, essa escolha seria feita ao passar o mouse sobre um item.

## Ideias
Como a base é de alimentos, será muito útil vincular cada alimento a uma imagem, já que isso deixaria muito mais agradável ao utilizador, além das demais informações sobre o alimento em questão.
A base escolhida tem os seguintes dados: `proteins_100g`, `carbohydrates_100g`, `fat_100g`, `energy_100g` e `food_name`, `category_name`, `origin` e `diet_type`. Como é possível perceber, não há dado de imagem, então para resolver isso vou ter que adicionar uma coluna com urls de imagens para renderizar usando html.

## Ferramentas
Para explorar os dados pretendo usar bibliotecas que me permitam plotar gráficos rapidamente, como o matplotlib. Para as visualizações mais em detalhes pretendo usar o Plotly pois ele me atraiu para fazer gráficos interativos, e para a apresentação pretendo hospedar a página final online, com a intenção de usar o Streamlit (acabei mudando para Render, pois usei Dash para a imagem aparecer ao passar o mouse por cima e então tive que usar outra saída).
Para as imagens, pretendo fazer um webScrapping com o Beautyful Soup, obtendo o primeiro resultado da pesquisa pelo Google Imagens.
Além disso acabei usando uma I.A. para montar uma paleta de cores para mim. O chat GPT sugeriu-me as cores que estou usando para as categorias dos alimentos.
