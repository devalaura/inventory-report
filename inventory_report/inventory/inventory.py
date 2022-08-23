import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_path, relatory_type):
        with open(file_path, encoding='utf-8') as file:
            if file_path.endswith(".csv"):
                return Inventory.csv_reader(file, relatory_type)
            elif file_path.endswith(".json"):
                return Inventory.json_reader(file, relatory_type)
            elif file_path.endswith(".xml"):
                return Inventory.xml_reader(file, relatory_type)

    def csv_reader(file, relatory_type):
        header, *csv_data = csv.reader(file)

        data_formated = []
        for row in csv_data:
            data_formated.append(dict(zip(header, row)))

        if relatory_type == "simples":
            return SimpleReport.generate(data_formated)
        if relatory_type == "completo":
            return CompleteReport.generate(data_formated)

    def json_reader(file, relatory_type):
        content = file.read()
        json_data = json.loads(content)

        if relatory_type == "simples":
            return SimpleReport.generate(json_data)
        elif relatory_type == "completo":
            return CompleteReport.generate(json_data)

    def xml_reader(file, relatory_type):
        content = file.read()
        xml_data = xmltodict.parse(content)["dataset"]["record"]

        if relatory_type == "simples":
            return SimpleReport.generate(xml_data)
        elif relatory_type == "completo":
            return CompleteReport.generate(xml_data)
