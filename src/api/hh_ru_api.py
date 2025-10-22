import requests
from src.api.abstract_api import AbstractAPI


class HHRuAPI(AbstractAPI):
    __base_url = "https://api.hh.ru/vacancies"

    def __init__(self):
        self.__session = requests.Session()

    def get_vacancies(self, keyword: str):
        params = {
            'text': keyword,
            'per_page': 10
        }
        try:
            response = self.__session.get(self.__base_url, params=params)
            response.raise_for_status()  # Важно: Поднимаем исключение для не-200 ответов

            data = response.json()
            return [item for item in data.get('items', [])]
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении вакансий: {e}")
            return []  # Возвращаем пустой список при ошибке

