from threading import Thread
import time


def hello_doe():
    time.sleep(3)
    print('Wait a moment...\nHave a great day!')


t = Thread(target=hello_doe)
t.start()

print('Hello, John Doe!')
