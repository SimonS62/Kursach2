import json
from src.files.abstract_file import AbstractFile

class JSONFile(AbstractFile):
    def __init__(self, filename='vacancies.json'):
        super().__init__(filename)
        self.data = self.read_data()

    def read_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def write_data(self, data):
        # Объединяем текущие данные с новыми, избегая дубли по 'id'
        existing_ids = {vac['id'] for vac in self.data}
        new_entries = [vac for vac in data if vac['id'] not in existing_ids]
        self.data.extend(new_entries)
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def delete_data(self, data):
        # Удаляем по id
        ids_to_delete = {vac['id'] for vac in data}
        self.data = [vac for vac in self.data if vac['id'] not in ids_to_delete]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)




