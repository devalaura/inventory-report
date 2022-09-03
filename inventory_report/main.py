import sys
import pathlib

from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) != 3:
        return print("Verifique os argumentos", file=sys.stderr)
    else:
        file_name = sys.argv[1]
        report_type = sys.argv[2]
        file_ext = pathlib.Path(file_name).suffix
        if file_ext == '.csv':
            inventory = InventoryRefactor(CsvImporter)
            report_data = inventory.import_data(file_name, report_type)
            return sys.stdout.write(report_data)
        elif file_ext == '.json':
            inventory = InventoryRefactor(JsonImporter)
            report_data = inventory.import_data(file_name, report_type)
            return sys.stdout.write(report_data)
        elif file_ext == '.xml':
            inventory = InventoryRefactor(XmlImporter)
            report_data = inventory.import_data(file_name, report_type)
            return sys.stdout.write(report_data)
        else:
            raise ValueError("Arquivo não suportado.")
