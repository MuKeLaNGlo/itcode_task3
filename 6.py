def is_prime(number: int) -> bool:
    '''
    Принимает на вход число, возвращает True, если число простое,
    возвращает False, если число сложное (составное, более двух делителей)
    '''
    # Обработаем исключение с отрицательными числами, а также 0 и 1
    if number < 0:
        raise ValueError('Число должно быть неотрицательным')
    elif number <= 1:
        return False

    # Перебираем все числа от 2 до sqrt(n)+1 и находим среди них делители
    # Если делители найдены (кроме 1 и n), то возвращаем False
    i = 2
    while i < int(number**0.5) + 1:
        if number % i == 0:
            return False
        i += 1
    return True


number: int = int(input('Введите число: '))
if is_prime(number):
    print('Число простое')
else:
    print('Число сложное')