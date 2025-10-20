import requests
from src.api.abstract_api import AbstractAPI


class HHRuAPI(AbstractAPI):
    __base_url = "https://api.hh.ru/vacancies"

    def __init__(self):
        self.__session = requests.Session()
        self.__connected = False

    def _connect(self):
        response = self.__session.get(self.__base_url)
        if response.status_code == 200:
            self.__connected = True
        else:
            raise ConnectionError(f"Failed to connect, status code: {response.status_code}")

    def get_vacancies(self, keyword: str):
        if not self.__connected:
            self._connect()
        params = {
            'text': keyword,
            'per_page': 10
        }
        response = self.__session.get(self.__base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return [item for item in data.get('items', [])]
        else:
            response.raise_for_status()

