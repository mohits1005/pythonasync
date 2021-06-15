from celery import Celery
from time import sleep

app = Celery('tasks', broker='amqp://guest@localhost//', backend='db+sqlite:///db.sqlite3')

@app.task
def reverse(text):
    sleep(5)
    return text[::-1]
