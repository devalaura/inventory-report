import pathlib
from xml.etree import ElementTree as ET


from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
  
    @staticmethod
    def import_data(file_name):
        file_ext = pathlib.Path(file_name).suffix
        if file_ext != ".xml":
            raise ValueError("Arquivo inválido")
        else:
            tree = ET.parse(file_name)
            roots = list(tree.getroot())

            xml_data = []
            xml_tags_text = {}
            for index in range(len(roots)):
                for root in roots[index]:
                    xml_tags_text[root.tag] = root.text

                xml_data.append(xml_tags_text)
                xml_tags_text = {}

            return xml_data