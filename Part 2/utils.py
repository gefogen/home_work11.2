import json


def load_content():
    """ Импортируем данные из candidates.json """
    with open("candidates.json", "r", encoding="utf-8") as file:
        content: list = json.load(file)  # Импортируем данные из candidates.json в приложение
        return content


def get_candidate(id):
    """ Возвращает данные кандидата """
    content = load_content()  # Загружаем контент из json
    for people in content:  # Перебор по списку
        if people['id'] == id:  # Проверяем наличие кандидата
            return people


def get_candidates_by_skill(skill):
    """ Функция, которая возвращает кандидатов по навыкам """
    content = load_content()  # Загружаем контент из json
    men = []  # Список, который мы будем возвращать в качестве результат
    for people in content:  # Перебор по списку
        chel = people["skills"].lower().split(", ")  # Переменная для поиска точного совпадения, а не соответствий
        if skill in chel:
            men.append(people)
    return men


def get_candidates_by_name(candidate_name):
    """ Функция, которая возвращает кандидатов по имени """
    content = load_content()  # Загружаем контент из json
    men = []  # Список, который мы будем возвращать в качестве результат
    for people in content:  # Перебор по списку
        if candidate_name.lower() in people["name"].lower():
            men.append(people)
    return men

# print(get_candidates_by_name(""))
