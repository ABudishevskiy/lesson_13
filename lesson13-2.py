# Написать декоратор c аргументом который будет подавлять определенные ошибки возникающие в теле вашей функции.
# Ошибки которые должен будет подавить ваш декоратор вы должны передать ему в качестве аргумента
def decor1(k):
    def decor(a):
        def wrap(b):
            print('begin')

            try:
                r = a(b)
            except k as e:
                print(e)
                return 'mistake'
            print('end')
            return r

        return wrap
    return decor


@decor1(ZeroDivisionError)
def delen(b):
    return 5 / b
print(delen(0))