def log(func):
    def wrapper():
        print('call %s:' % func)
        return func()
    return wrapper

@log
def now():
    print('2015-3-25')


now()