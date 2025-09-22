from datetime import datetime as dt

def checktime(func):
    def wrapper():
        now = dt.now()
        formatted_time = f"{now.hour:02}:{now.minute:02}:{now.second:02} {now.day:02}/{now.month:02}/{now.year}"
        print(f"Функция была вызвана в {formatted_time}")
        print(func.__name__)
        return func()
    return wrapper

@checktime
def hello_world():
    print("hello world")

hello_world()