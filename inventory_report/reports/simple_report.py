from datetime import date
from typing import Counter


class SimpleReport:
    def generate(dados):
        lista_datas_fabricacao = []
        lista_datas_validade = []
        lista_empresas = []
        for dado in dados:
            lista_datas_fabricacao.append(dado["data_de_fabricacao"])

            ano_val, mes_val, dia_val = dado["data_de_validade"].split("-")
            lista_datas_validade.append(date(
              int(ano_val), int(mes_val), int(dia_val)
            ))

            lista_empresas.append(dado["nome_da_empresa"])

        data_fabricacao_mais_antiga = min(lista_datas_fabricacao)
        data_validade_mais_proxima = min(
          lista_datas_validade, key=lambda valor: abs(valor - date.today())
        )

        empresa_com_mais_produtos = Counter(lista_empresas).most_common()[0][0]

        return (
          f"Data de fabricação mais antiga: {data_fabricacao_mais_antiga}\n"
          f"Data de validade mais próxima: {data_validade_mais_proxima}\n"
          f"Empresa com mais produtos: {empresa_com_mais_produtos}"
        )
