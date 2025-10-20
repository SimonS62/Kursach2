from abc import ABC, abstractmethod

class AbstractAPI(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _connect(self):
        """Подключение к API"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str):
        """Получение вакансий по ключевому слову"""
        pass
