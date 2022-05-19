from flask import Flask, request, render_template  # Импортируем Flask
from utils import *  # Импортируем функции

app = Flask(__name__)  # Создаем экземпляр Flask'а


@app.route("/")  # Главная страница
def load_main_page():
    content = load_content()
    return render_template("list_of_candidates.html", content=content, quantity=len(content))


@app.route("/candidate/<int:id>")  # Поиск кандидата по id
def load_candidate_by_id(id):
    content = get_candidate(id)
    return render_template("page_of_candidate.html", content=content)


@app.route('/search/')
@app.route("/search/<name>")  # Поиск кандидата по имени
def load_candidates_by_name(name=None):
    if name is None:
        name = request.args.get('query')
    content = get_candidates_by_name(name)
    return render_template("search.html", content=content, quantity=len(content))


@app.route('/skill/')
@app.route("/skill/<skill_name>")  # Поиск кандидатов по навыкам
def load_candidates_by_skills(skill_name=None):
    if skill_name is None:
        skill_name = request.args.get('query')
    content = get_candidates_by_skill(skill_name)
    return render_template("skill.html", content=content, quantity=len(content))


if __name__ == "__main__":
    app.run(debug=True)  # Запускаем
