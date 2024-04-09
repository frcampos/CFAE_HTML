# This is a sample Python script.
# from typing import TextIO
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import re
from datetime import datetime, timedelta
from htmlcode import str_html_init, str_html_final


def print_hi(name: object) -> object:
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm - teste leitura ficheiro com acoes de formacao ativas')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Olá, Aplicação de conversão de ficheiro excel com ações de formação em
# código HTML para inserção no sítio web do CFAECA.

# Caminho relativo e nome do arquivo Excel
excel_file_path = "formacoesativas.xlsx"
# configurar o número de colunas e de registos existentes
# O número de registos é igual à linha -1 (desconto do cabeçalho)
num_colunas = 16
num_registos = 16

# o numero de registos deve ser calculado a partir do registo do excel. Por exemplo se no excel
# A LINHA FOR 21 O num_registos =  20

# Caminho para o arquivo HTML original
html_file_path = "codigoformacoesativa.html"

# Caminho para o arquivo HTML comprimido
compressed_html_file_path = "compressed.html"

# Cabeçalho personalizado para as 15 colunas
header = ["Coluna_1", "Coluna_2", "Coluna_3", "Coluna_4", "Coluna_5",
          "Coluna_6", "Coluna_7", "Coluna_8", "Coluna_9", "Coluna_10",
          "Coluna_11", "Coluna_12", "Coluna_13", "Coluna_14", "Coluna_15", "Coluna_16"]
# Cabeçalho personalizado para as 16 colunas

# print(str_html_init)

# Carregar o arquivo Excel


# Carregar o arquivo Excel
try:
    df = pd.read_excel(excel_file_path, usecols=range(num_colunas), nrows=num_registos, header=0, names=header)

    # Imprime os nomes das colunas para depuração
    print("Nomes das colunas:")
    print(df.columns)
    print()


    # Função para converter o número em data ou retornar o texto original

    def convert_to_date_or_text(value):

        if isinstance(value, int):
            # return (datetime(1899, 12, 30) + timedelta(days=value)).strftime('%d/%m/%Y')
            return (datetime(30, 12, 1899) + timedelta(days=value)).strftime('%d/%m/%Y')
        else:
            return value


    # Aplica a função de conversão à coluna de data de início devido à conversão das celulas quando
    # se transferem os dados via M365 Edu

    df['Coluna_6'] = df['Coluna_6'].apply(convert_to_date_or_text)

    print('stop to check data inicio')
    # Abre o arquivo HTML para gravação

    with open("codigoformacoesativa.html", "w", encoding='utf-8') as file:
        # Escreve o cabeçalho do HTML

        html_content_inicial = "Introduzir o código inicial aqui\n"
        # Obter a data e hora atual no formato YYYY-MM-DD HH:MM
        data_atualizacao = datetime.now().strftime('%Y-%m-%d %H:%M')
        # HTML para a linha adicional com a data de atualização
        linha_data_atualizacao = f'<li style="font-size: 9px;">Data de atualização - {data_atualizacao}</li>'
        try:
            file.write(str_html_init)

            # Itera sobre as linhas do DataFrame
            for index, row in df.iterrows():
                # Extrai as informações das colunas especificadas
                imagem_src = row.get('Coluna_12', '')  # Use get para evitar erros se a coluna estiver ausente
                link_href = row.get('Coluna_2', '')  # Use get para evitar erros se a coluna estiver ausente
                codigo_itemprop_name = row.get('Coluna_1', '')  # Use get para evitar erros se a coluna estiver ausente
                grupos_recrutamento = row.get('Coluna_5', '')  # Use get para evitar erros se a coluna estiver ausente
                data_inicio = row.get('Coluna_6', '')  # Use get para evitar erros se a coluna estiver ausente
                hora_inicio = row.get('Coluna_7', '')  # Use get para evitar erros se a coluna estiver ausente
                horas_acreditadas = row.get('Coluna_9', '')  # Use get para evitar erros se a coluna estiver ausente
                modalidade = row.get('Coluna_10', '')  # Use get para evitar erros se a coluna estiver ausente
                regime_frequencia = row.get('Coluna_11', '')  # Use get para evitar erros se a coluna estiver ausente
                artigos_rjfcp = row.get('Coluna_15', '')  # obter os artigos do ECD para os quais releva a formação
                # Escreve o código HTML no arquivo
                file.write(f"""<div class="box-wrap" itemprop="event" itemscope itemtype="http://schema.org/Course">\n
                                            <div class="img-wrap" itemprop="image"><img src="{imagem_src}" alt="imagem da formação"></div>\n
                                            <a href="{link_href}" class="learn-desining-banner" itemprop="name">{codigo_itemprop_name}</a>\n
                                            <div class="box-body" itemprop="description">\n
                                            <p><br></p>\n
                                            <section itemprop="time">\n
                                            <p><span>Grupo(s) Recrutamento:</span> {grupos_recrutamento}</p>\n
                                             <p><span>Data início:</span> {data_inicio}</p>\n
                                             <p><span>Hora início:</span> {hora_inicio}</p>\n
                                             <p><span>Horas Acreditadas:</span> {horas_acreditadas}</p>\n
                                             <p><span>Modalidade:</span> {modalidade}</p>\n
                                             <p><span>Regime de frequência:</span> {regime_frequencia}</p>\n
                                              <p><span>Artigo(s) do RJFCP que relevam:</span> {artigos_rjfcp}</p>\n
                                             </section>\n
                                            </div>\n
                                        </div>\n""")

                # Escreve o final do arquivo HTML

            print("O arquivo HTML 'codigoformacoesativa.html' foi gerado com sucesso.")

            file.write(str_html_final)


            # print(str_html_final)

            # Função para remover espaços e caracteres de retorno de carro e alimentação de linha entre tags <a>, e
            # remover alguns erros de html específicos

            def compress_html(file_path, compressed_file_path):
                with open(file_path, 'r') as f_in:
                    html_content = f_in.read()

                # Use expressão regular para remover espaços e quebras de linha entre tags <a>
                # compressed_content = re.sub(r'(<a[^>]*>)\s*(.*?)\s*(</a>)', r'\1\2\3', html_content, flags=re.DOTALL)
                # Use expressão regular para remover espaços, quebras de linha e retorno de carro entre tags <a>
                # ferramenta semelhante ao minifier HTML
                compressed_content: str = re.sub(r'(<a[^>]*>)[\s\r\n]*(.*?)[\s\r\n]*(</a>)', r'\1\2\3', html_content,
                                                 flags=re.DOTALL)

                # Substituir \n e \r por espaços em branco

                compressed_content = compressed_content.replace("\n", '').replace("\r", '')
                compressed_content = re.sub(r'>\s+<', '><', html_content)

                # Remover linhas que contenham comentários HTML
                compressed_content = re.sub(r'<!--.*?-->', '', compressed_content, flags=re.DOTALL)

                # Remover "00:00:00" caso seja encontrado, devido aos formatos do Excel e processo de conversão
                compressed_content = compressed_content.replace("00:00:00", "")
                # Remoção devido ao processo de conversão
                compressed_content = compressed_content.replace('" "', '"')
                compressed_content = compressed_content.replace('</a></li></ul></li></li><li',
                                                                '</a ></li></ul><li').replace('</a></li></ul></li><li',
                                                                                              '</a></li></ul><li')

                with open(compressed_file_path, 'w', encoding='utf-8') as f_out:
                    f_out.write(compressed_content)


            # Comprimir o arquivo HTML
            compress_html(html_file_path, compressed_html_file_path)
            print("Feito ficheiro comprimido - compressed.html")

        except FileNotFoundError:
            print("O arquivo 'formacoesativas.xlsx' não foi encontrado.")

finally:
    print('')
