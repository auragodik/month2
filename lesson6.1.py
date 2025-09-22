def printer(func):
    def wrapper(*args, **kwargs):
        print(f'до вызова функции {func.__name__}')
        result = func(*args, **kwargs)
        print(f'после вызова функции {func.__name__}')
        return result
    return wrapper()
@printer
def hello_world():
    print('hello worldik')
@printer
def add_numbers(n1, n2):
    return add_numbers(n1 + n2)
print(add_numbers(5, 12))
hello_world()
add_numbers()