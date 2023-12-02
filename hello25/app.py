from flask import Flask, session
import webbrowser
import threading

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World 25!'

@app.route('/api/v1/hello-world-25')
def hello_world_25():
    # Відкриття браузера у власному потоці
    threading.Thread(target=open_browser).start()
    return 'Hello World 25', 200

def open_browser():
    webbrowser.open("http://192.168.0.101:5000")

if __name__ == '__main__':
    from waitress import serve

    # Запуск сервера у власному потоці
    threading.Thread(target=serve, args=(app,), kwargs={'host': '0.0.0.0', 'port': 5000}).start()

    # main.py

from db_config import create_connection

# Отримання з'єднання
connection = create_connection()

# Тут ви можете виконувати ваші операції з базою даних
