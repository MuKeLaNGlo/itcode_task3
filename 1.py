day: int = 10
month: str = 'июня'
temperature: float = 30.0

if temperature >= 0:
    print(f'Сегодня {day} {month}. На улице {temperature} градусов.')
else:
    print('Холодно, лучше остаться дома.')