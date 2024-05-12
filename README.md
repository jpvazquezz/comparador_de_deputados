# Comparador de Deputados: Desvendando as diferenças nas proposições legislativas

Este projeto apresenta um aplicação que tem o intuito de aprimorar o conhecimento da sociedade brasileira a respeito de seus representantes ao fornecer uma forma rápida e fácil de conhecer e diferenciar os deputados federais brasileiros.

Essa aplicaçao é construída com Python, utilizando a API de Dados Abertos da Câmara dos Deputados e a inteligência artificial do Gemini IA, oferece uma análise comparativa profunda das atividades legislativas de dois deputados à sua escolha.

## Objetivo:
Este código visa:
- Permitir a busca e seleção de dois deputados a partir de seus nomes.
- Coletar as últimas 100 proposições de cada deputado, extraindo suas ementas.
- Submeter as ementas à análise do modelo de linguagem Google Gemini, buscando similaridades e divergências.
- Fornecer um relatório conciso, em formato Markdown, que destaca:
  - Os principais temas abordados por cada deputado.
  - O grau de similaridade entre os temas abordados.
  - As diferenças mais significativas entre as proposições dos deputados.
  - Uma tabela com a frequência de palavras-chave relevantes para cada deputado.

## Destaques:
- Combina a riqueza da API de Dados Abertos da Câmara com o poder analítico do Google Gemini.
- Vai além de simples comparações, oferecendo insights sobre os focos de atuação de cada deputado.
- Apresenta resultados em um formato claro e de fácil leitura (Markdown).
- Interface interativa que facilita a seleção dos deputados a serem comparados.

## Tecnologias Empregadas:
- Python: Linguagem de programação central do projeto.
- Requests: Biblioteca para realizar requisições HTTP à API da Câmara.
- Pandas: Biblioteca para manipulação e análise de dados, utilizada para organizar as proposições.
- Google Gemini: Modelo de linguagem avançado que analisa as ementas e gera a comparação.
- FuzzyWuzzy: Biblioteca para correspondência de strings fuzzy, utilizada na busca pelos deputados.
- IPython: Ferramentas interativas para exibição de dados e formatação Markdown.

## Como Executar:
1. Clone o repositório:
   ```
   git clone https://github.com/seu_usuario/comparador-deputados.git
   ```
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Insira sua API Key do Google Gemini:
   Substitua 'YOUR_API_KEY' no código pela sua chave de API do Google Gemini.
4. Execute o código:
   ```
   python comparador_deputados.py
   ```
5. Siga as instruções: O programa solicitará que você digite o nome completo dos deputados que deseja comparar.

## Desafio:
Este projeto foi desenvolvido como um desafio para explorar o potencial da API de Dados Abertos da Câmara e da IA do Google Gemini na análise comparativa de atividades legislativas.

## Contribuições:
Contribuições são encorajadas! Sinta-se à vontade para abrir issues, reportar bugs ou enviar pull requests com sugestões de melhorias, novos recursos ou correções.

Com este projeto, você poderá mergulhar no mundo das proposições legislativas, desvendando as nuances e diferenças entre os deputados!

## Autor
Meu nome é João Pedro Vazquez, sou cientista de dados e entrego soluções de dados de excelência com o objetivo de resolver problemas reais de negócio. Fique à vontade para entrar em contato!

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://jpvazquezz.github.io/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/joao-pedro-vazquez/)
[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@jpvazquez)
