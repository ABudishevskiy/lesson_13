# Создать менеджер контекста который будет подсчитывать время выполнения блока инструкций
from contextlib import ContextDecorator
import time
class my_context_decorator(ContextDecorator):

        def __init__(self):

            print('init')


        def __enter__(self):
            print('enter')
            self.k = time.time()

        def __exit__(self, exc_type, exc_val, exc_tb):
            print('exit')
            print(time.time() - self.k)
            return True

with my_context_decorator():
    for i in range(100000):
        print('kgjhg')