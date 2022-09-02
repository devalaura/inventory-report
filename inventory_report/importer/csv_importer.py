import pathlib
import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):

    @staticmethod
    def import_data(file_name):
        file_ext = pathlib.Path(file_name).suffix
        if file_ext != ".csv":
            raise ValueError("Arquivo inválido")
        else:
            with open(file_name, encoding='utf-8') as file:
                header, *csv_data = csv.reader(file)

                data_dict = []
                for row in csv_data:
                    data_dict.append(dict(zip(header, row)))

            return data_dict
