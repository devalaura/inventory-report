import pathlib
import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):

    @staticmethod
    def import_data(file_name):
        file_ext = pathlib.Path(file_name).suffix
        if file_ext != ".json":
            raise ValueError("Arquivo inválido")
        else:
            with open(file_name) as file:
                content = file.read()
                json_data = json.loads(content)

            return json_data
