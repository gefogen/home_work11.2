from flask import Flask  # Импортируем Flask
import json  # Импортируем json

with open("candidates.json", "r", encoding="utf-8") as file:
    content: list = json.load(file)  # Импортируем данные из candidates.json в приложение

app = Flask(__name__)  # Создаем экземпляр Flask'а

if __name__ == "__main__":
    app.run(debug=True)     # Запускаем