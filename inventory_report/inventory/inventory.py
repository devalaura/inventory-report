import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_path, relatory_type):
        with open(file_path, encoding='utf-8') as file:
            header, *data = csv.reader(file)
            data_formated = []
            for row in data:
                data_formated.append(dict(zip(header, row)))

        if relatory_type == "simples":
            return SimpleReport.generate(data_formated)
        if relatory_type == "completo":
            return CompleteReport.generate(data_formated)
