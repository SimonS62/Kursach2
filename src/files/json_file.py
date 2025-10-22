import json
from abc import ABC, abstractmethod

class AbstractFile(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def read_data(self):
        pass  # Абстрактный метод

    @abstractmethod
    def write_data(self, data):
        pass  # Абстрактный метод

    @abstractmethod
    def delete_data(self, data):
        pass  # Абстрактный метод

class JSONFile(AbstractFile):
    def read_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def write_data(self, data):
        # Читаем текущие данные
        existing_data = self.read_data()
        # Объединяем текущие данные с новыми, избегая дубли по 'id'
        existing_ids = {vac['id'] for vac in existing_data}
        new_entries = [vac for vac in data if vac['id'] not in existing_ids]
        updated_data = existing_data + new_entries
        self._write_json(updated_data)

    def delete_data(self, data):
        # Читаем текущие данные
        existing_data = self.read_data()

        # Удаляем по id
        ids_to_delete = {vac['id'] for vac in data}
        updated_data = [vac for vac in existing_data if vac['id'] not in ids_to_delete]
        self._write_json(updated_data)

    def _write_json(self, data):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)




