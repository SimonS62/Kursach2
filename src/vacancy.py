from functools import total_ordering


@total_ordering
class Vacancy:
    __slots__ = ['id', 'name', 'salary', 'url']

    def __init__(self, id: str, name: str, salary: float, url: str):
        self.id = id
        self.name = name
        self.salary = Vacancy.__validate_salary(salary)  # Вызываем статический метод через класс
        self.url = url

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'salary': self.salary,
            'url': self.url
        }

    @staticmethod  # Декоратор для статического метода
    def __validate_salary(salary):
        if salary is None or salary < 0:
            return 0
        return salary

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary


