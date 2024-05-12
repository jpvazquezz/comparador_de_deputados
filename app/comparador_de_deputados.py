import requests
import pandas as pd
import os
from fuzzywuzzy import fuzz
import markdown2

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
import textwrap
import pathlib

class ComparadorDeDeputados():
    """
    Classe para comparar as atividades legislativas de dois deputados.
    
    Atributos:
        dep1 (str): Nome completo do primeiro deputado.
        dep2 (str): Nome completo do segundo deputado.
        lista_deputados (list): Lista de nomes de todos os deputados.
        deputado_encontrado1 (str): Nome do primeiro deputado encontrado na lista.
        deputado_encontrado2 (str): Nome do segundo deputado encontrado na lista.
        deputadoID1 (str): ID do primeiro deputado encontrado na API.
        deputadoID2 (str): ID do segundo deputado encontrado na API.
        df_props1 (DataFrame): DataFrame das proposições do primeiro deputado.
        df_props2 (DataFrame): DataFrame das proposições do segundo deputado.
        api_key (str): Chave de API para acesso aos serviços da Google GenerativeAI.
    """
    def __init__(self) -> None:
        self.dep1 = None
        self.dep2 = None
        self.lista_deputados = None
        self.deputado_encontrado1 = None
        self.deputado_encontrado2 = None
        self.deputadoID1 = None
        self.deputadoID2 = None
        self.df_props1 = None
        self.df_props2 = None
        self.api_key = 'YOUR_API_KEY'


    def escolherDeputados(self) -> None:

        """Método para escolher os deputados a serem comparados."""

        print('Favor digitar nome e sobrenome')
        dep1 = input('Selecione o primeiro deputado: ')
        #print('Deputado(a): ', dep1)
        self.dep1 = dep1
        dep2 = input('Selecione o segundo deputado: ')
        #print('Deputado(a): ', dep2)
        self.dep2 = dep2

    def listagemDeputados(self) -> None:
        
        """Método para obter a lista de todos os deputados."""

        url = f"https://dadosabertos.camara.leg.br/api/v2/deputados"
        response = requests.get(url)
        dados = response.json()
        deputados_list = []
        for deputado in dados['dados']:
            deputados_list.append(deputado['nome'].upper())
        
        self.lista_deputados = deputados_list

    def encontrarDeputado(self) -> None:

        """Método para encontrar os deputados na lista."""

        deputado_dict = {}
        lista_deputado_inserido = [self.dep1, self.dep2]
        self.listagemDeputados()
        deputado_encontrado = []

        for deputado_inserido in lista_deputado_inserido:
            melhor_pontuacao = 0
            for deputado in self.lista_deputados:
                pontuacao = fuzz.ratio(deputado, deputado_inserido.upper())
                if pontuacao > melhor_pontuacao:
                    melhor_pontuacao = pontuacao
                    deputado_dict = {pontuacao: deputado}
            deputado_encontrado.append(deputado_dict[melhor_pontuacao])
                    
        self.deputado_encontrado1 = deputado_encontrado[0]
        self.deputado_encontrado2 = deputado_encontrado[1]
    
    def getDeputadoID(self) -> None:

        """Método para obter os IDs dos deputados."""

        url = f"https://dadosabertos.camara.leg.br/api/v2/deputados"
        response = requests.get(url)
        dados = response.json()
        for deputado in dados['dados']:
            if self.deputado_encontrado1 == deputado['nome'].upper():
                self.deputadoID1 = deputado['id']
            if self.deputado_encontrado2 == deputado['nome'].upper():
                self.deputadoID2 = deputado['id']
        
    def getProposicoes(self) -> None:

        """Método para obter as proposições dos deputados."""

        self.getDeputadoID()
        # Primeiro Deputado
        url = f"https://dadosabertos.camara.leg.br/api/v2/proposicoes/?idDeputadoAutor={self.deputadoID1}&itens=100&pagina=2"
        response = requests.get(url)
        dados = response.json()

        tipo_proposicao = []
        numero_ano = []
        ementa =  []
        for dado in dados['dados']:
            tipo_proposicao.append(dado['siglaTipo'])
            numero_ano.append(str(dado['numero']) + '/' + str(dado['ano']))
            ementa.append(dado['ementa'])

        self.df_props1 = pd.DataFrame({
            'autor': self.deputado_encontrado1,
            'tipo_proposicao':tipo_proposicao,
            'numero_ano': numero_ano,
            'ementa': ementa})
        
        # Segundo Deputado
        url = f"https://dadosabertos.camara.leg.br/api/v2/proposicoes/?idDeputadoAutor={self.deputadoID2}&itens=100&pagina=2"
        response = requests.get(url)
        dados = response.json()

        tipo_proposicao = []
        numero_ano = []
        ementa =  []
        for dado in dados['dados']:
            tipo_proposicao.append(dado['siglaTipo'])
            numero_ano.append(str(dado['numero']) + '/' + str(dado['ano']))
            ementa.append(dado['ementa'])

        self.df_props2 = pd.DataFrame({
            'autor': self.deputado_encontrado2,
            'tipo_proposicao':tipo_proposicao,
            'numero_ano': numero_ano,
            'ementa': ementa}) 
    
    def to_markdown(self, text):

        """Método para formatar texto como markdown."""

        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True)) 
    
    def generateComparison(self):

        """
        Método para gerar uma comparação entre as atividades legislativas dos deputados.

        Retorna:
            Markdown: Texto em formato Markdown com a comparação gerada.
        """
        
        # Extrair as ementas dos dataframes
        ementas_deputado1 = self.df_props1['ementa'].tolist()
        ementas_deputado2 = self.df_props2['ementa'].tolist()

        # Criar o prompt para a API do Gemini
        prompt = f"""
        Analise e compare as ementas das últimas 100 proposições de dois deputados diferentes.

        **Ementas do Deputado {self.deputado_encontrado1}:**
        {ementas_deputado1}

        **Ementas do Deputado {self.deputado_encontrado2}:**
        {ementas_deputado2}

        **Solicitações:*

        1. Identifique os principais temas abordados por cada deputado.
        2. Compare a similaridade entre os temas abordados pelos dois deputados.
        3. Destaque as principais diferenças entre as ementas dos deputados.
        4. Apresente uma tabela com a frequência de palavras-chave relevantes para cada deputado.
        """
        genai.configure(api_key= self.api_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt, stream=True)
        response.resolve()
        # A aprimorar
        return print(response.text)
    
if __name__ == '__main__':
    comp = ComparadorDeDeputados()
    comp.escolherDeputados()
    comp.encontrarDeputado()
    comp.getProposicoes()
    comp.generateComparison()