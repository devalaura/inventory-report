from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def product_list_mock():
    return [{
      "id": 1,
      "nome_da_empresa": "Farinini",
      "nome_do_produto": "farinha",
      "data_de_fabricacao": "2021-05-01",
      "data_de_validade": "2023-06-02",
      "numero_de_serie": "AA22",
      "instrucoes_de_armazenamento": "ao abrigo de luz"
    }, {
      "id": 2,
      "nome_da_empresa": "Forces of Nature",
      "nome_do_produto": "CADEIRA",
      "data_de_fabricacao": "2022-04-04",
      "data_de_validade": "2023-02-09",
      "numero_de_serie": "FR48",
      "instrucoes_de_armazenamento": "Conservar em local fresco"
    }, {
      "id": 3,
      "nome_da_empresa": "Forces of Nature",
      "nome_do_produto": "CADEIRA",
      "data_de_fabricacao": "2022-04-04",
      "data_de_validade": "2023-02-09",
      "numero_de_serie": "FR48",
      "instrucoes_de_armazenamento": "Conservar em local fresco"
    }]


def test_decorar_relatorio():
    colored_report = ColoredReport(SimpleReport).generate(product_list_mock())

    green_phrases = [
        "\033[32mData de fabricação mais antiga:\033[0m",
        "\033[32mData de validade mais próxima:\033[0m",
        "\033[32mEmpresa com mais produtos:\033[0m",
    ]

    for phrase in green_phrases:
        assert phrase in colored_report

    blue_values = [
      "\033[36m2021-05-01\033[0m",
      "\033[36m2023-02-09\033[0m"
    ]

    for value in blue_values:
        assert value in colored_report 

    red_value = "\033[31mForces of Nature\033[0m"

    assert red_value in colored_report
    
