from inventory_report.inventory.product import Product


def produto_mock():
    return {
      "id": 1,
      "nome_da_empresa": "Forces of Nature",
      "nome_do_produto": "CADEIRA",
      "data_de_fabricacao": "2022-04-04",
      "data_de_validade": "2023-02-09",
      "numero_de_serie": "FR48",
      "instrucoes_de_armazenamento": "Conservar em local fresco"
    }


def test_cria_produto():
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

    instrucoes = "Conservar em local fresco"

    assert cria_produto.id == 1
    assert cria_produto.nome_da_empresa == "Forces of Nature"
    assert cria_produto.nome_do_produto == "CADEIRA"
    assert cria_produto.data_de_fabricacao == "2022-04-04"
    assert cria_produto.data_de_validade == "2023-02-09"
    assert cria_produto.numero_de_serie == "FR48"
    assert cria_produto.instrucoes_de_armazenamento == instrucoes
