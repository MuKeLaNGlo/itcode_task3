def fib(index: int) -> int:
    '''
    Возвращает значение в ряду Фибоначчи по переданному индексу
    '''
    current: int = 1
    num_prev1: int = 1

    i = 2
    while i < index:
        tmp = current
        current += num_prev1
        num_prev1 = tmp
        i += 1
    return current


number: int = int(input('Введите число: '))
print(fib(number))