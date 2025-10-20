from src.api.hh_ru_api import HHRuAPI
from src.vacancies.vacancy import Vacancy
from src.files.json_file import JSONFile


def main():
    api = HHRuAPI()
    file_handler = JSONFile()

    keyword = input("Введите ключевое слово для поиска вакансий: ")
    vacancies_data = api.get_vacancies(keyword)

    vacancies_list = []
    for item in vacancies_data:
        vacancy = Vacancy(
            id=str(item.get('id')),
            name=item.get('name'),
            salary=(item.get('salary', {}).get('from') or 0),
            url=item.get('alternate_url')
        )
        vacancies_list.append(vars(vacancy))

    file_handler.write_data(vacancies_list)
    print("Вакансии сохранены в файл.")


if __name__ == '__main__':
    main()
