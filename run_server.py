import subprocess
import webbrowser
import threading

def run_server():
    subprocess.run(["waitress-serve", "--host=192.168.0.101", "--port=5000", "project4.app:app"])

def open_browser():
    webbrowser.open("http://192.168.0.101:5000")

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

    # Затримка для того, щоб сервер успішно запустився перед відкриттям браузера
    import time
    time.sleep(2)

    open_browser()
