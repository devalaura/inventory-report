import csv
import json
import pathlib
from xml.etree import ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_path, relatory_type):
        file_ext = pathlib.Path(file_path).suffix
        if file_ext == ".csv":
            return Inventory.csv_reader(file_path, relatory_type)
        elif file_ext == ".json":
            return Inventory.json_reader(file_path, relatory_type)
        elif file_ext == ".xml":
            return Inventory.xml_reader(file_path, relatory_type)

    def csv_reader(file_path, relatory_type):
        with open(file_path, encoding='utf-8') as file:
            header, *csv_data = csv.reader(file)

            data_formated = []
            for row in csv_data:
                data_formated.append(dict(zip(header, row)))

            if relatory_type == "simples":
                return SimpleReport.generate(data_formated)
            if relatory_type == "completo":
                return CompleteReport.generate(data_formated)

    def json_reader(file_path, relatory_type):
        with open(file_path) as file:
            content = file.read()
            json_data = json.loads(content)

            if relatory_type == "simples":
                return SimpleReport.generate(json_data)
            elif relatory_type == "completo":
                return CompleteReport.generate(json_data)

    def xml_reader(file_path, relatory_type):
        tree = ET.parse(file_path)
        roots = list(tree.getroot())

        xml_data = []
        xml_tags_text = {}
        for index in range(len(roots)):
            for root in roots[index]:
                xml_tags_text[root.tag] = root.text

            xml_data.append(xml_tags_text)
            xml_tags_text = {}

        if relatory_type == "simples":
            return SimpleReport.generate(xml_data)
        elif relatory_type == "completo":
            return CompleteReport.generate(xml_data)
