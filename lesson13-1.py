# Написать декоратор и менеджер контекста который будет подавлять все ошибки возникающие в теле вашей функции.
def decor(a):
    def wrap(b):
        print('begin')

        try:
            r = a(b)
        except:
            return 'mistake'
        print('end')
        return r

    return wrap


from contextlib import ContextDecorator
class my_context_decorator(ContextDecorator):

        def __init__(self):

            print('init')


        def __enter__(self):
            print('enter')

        def __exit__(self, exc_type, exc_val, exc_tb):
            print('exit')
            return True


@my_context_decorator()
def delen(b):
    return 5 / b
print(delen(0))

with my_context_decorator():
    print(delen(0))

@decor
def delen(b):
    return 5 / b
print(delen(0))