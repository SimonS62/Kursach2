from functools import total_ordering

@total_ordering
class Vacancy:
    __slots__ = ['id', 'name', 'salary', 'url']

    def __init__(self, id: str, name: str, salary: float, url: str):
        self.id = id
        self.name = name
        self.salary = self.__validate_salary(salary)
        self.url = url

    def __validate_salary(self, salary):
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


