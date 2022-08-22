from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(dados):
        resultado_simples = SimpleReport.generate(dados)

        nomes_empresa = []
        for empresa in dados:
            nomes_empresa.append(empresa["nome_da_empresa"])

        quantidade_por_empresa = []
        for nome_empresa in nomes_empresa:
            dado_a_ser_inserido = (nome_empresa,
                                   nomes_empresa.count(nome_empresa))
            if dado_a_ser_inserido not in quantidade_por_empresa:
                quantidade_por_empresa.append(dado_a_ser_inserido)

        resultado_final = (
          f"{resultado_simples}"
          f"\nProdutos estocados por empresa:\n"
        )
        for empresa in quantidade_por_empresa:
            resultado_final += (f"- {empresa[0]}: {empresa[1]}\n")

        return resultado_final
