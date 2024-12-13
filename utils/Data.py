import json

class Data:
    def read_json(self,route):
        """
        @:param route  ruta del archivo json
        :return data   retorna un directorio con la informacion
        """
        with open(route, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def wire_json(self, route, data):
        """
        @:param route  ruta del archivo json
        :return data   retorna un directorio con la informacion
        """
        with open(route, 'w', encoding='utf-8') as file:
            json.dump(data, fp=file, ensure_ascii=False, indent=4)

    def wire_txt(self, route, mode, data):
        """
        @:param route  ruta del archivo json
        :return data   retorna un directorio con la informacion
        """
        with open(route, mode, encoding='utf-8') as file:
            file.write(data)

    def read_txt(self, route):
        """
        @:param route  ruta del archivo json
        :return data   retorna un directorio con la informacion
        """
        with open(route, 'r', encoding='utf-8') as file:
            return file.read()



