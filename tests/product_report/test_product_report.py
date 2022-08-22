from inventory_report.inventory.product import Product


def produto_mock():
    return {
      "id": 1,
      "nome_da_empresa": "Farinini",
      "nome_do_produto": "farinha",
      "data_de_fabricacao": "01-05-2021",
      "data_de_validade": "02-06-2023",
      "numero_de_serie": "AA22",
      "instrucoes_de_armazenamento": "ao abrigo de luz"
    }


def test_relatorio_produto():
    produto = produto_mock()

    cria_produto = Product(
        produto["id"],
        produto["nome_do_produto"],
        produto["nome_da_empresa"],
        produto["data_de_fabricacao"],
        produto["data_de_validade"],
        produto["numero_de_serie"],
        produto["instrucoes_de_armazenamento"]
    )

    resultado_esperado = ("O produto farinha fabricado em 01-05-2021 por" +
                          " Farinini com validade até 02-06-2023 precisa ser" +
                          " armazenado ao abrigo de luz.")

    assert cria_produto.__repr__() == resultado_esperado
