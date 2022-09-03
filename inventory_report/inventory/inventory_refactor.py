from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, file_name, file_type):
        self.data.extend(self.importer.import_data(file_name))

        if file_type == "simples":
            SimpleReport.generate(self.data)
        elif file_type == "completo":
            CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
