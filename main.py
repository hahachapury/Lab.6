
class Lamp:
    def __init__(self, name, power, consump, life):
        self.name = name
        self.power = power
        self.consump = consump
        self.life = life

    def Rat(self):
        print(f'Соотношение мощности излучения к энергопотреблению = '
              f'{self.power / self.consump}')
    def Info(self):
        print(f'Название модели: {self.name}')
        print(f'Мощность излучения: {self.power} Вт')
        print(f'Потребление энергии: {self.consump} Вт/ч')
        print(f'Срок службы: {self.life} ч')

class Bulb(Lamp):
    def __init__(self, name, power, consump, life, length):
        super().__init__(name, power, consump, life)
        self.length = length
    def Work(self):
        print(f'Лампа дневного освещения прослужит около '
              f'{self.life /(8*24)} дней при работе 8 часов в сутки')
    def Info(self):
        super().Info()
        print(f'Длина лампы дневного освещения: {self.length} мм')

class Projector(Lamp):
    def __init__(self,name, power, consump, life, weight):
        super().__init__(name ,power, consump, life)
        self.weight = weight

    def Work(self):
        print(f'Прожектор прослужит около {self.life / 8} часов'
              f' или {self.life /(8*24*365)} лет при работе 8 часов в сутки')

    def Info(self):
        super().Info()
        print(f'Вес прожектора: {self.weight} г')

Lamp1 = Bulb('Lampa',36, 40, 10000, 1200)
Lamp1.Info()
Lamp1.Work()
Lamp1.Rat()
print('\n')

Lamp2 = Projector('Jazz', 500, 50, 87600, 0.7)
Lamp2.Info()
Lamp2.Work()
Lamp2.Rat()
print('\n')

class H():
    def __init__(self, h):
        self.h = h

    def __add__(self, o):
        return self.h + o.h

print('Хотите внести информацию о модели?')
b = input('(Да или Нет): ')
if b == 'Да':
    print('Нажмите 1, если вы вносите характеристики Лампы дневного освещения')
    print('Нажмите 2, если вы вносите характеристики Прожектора')
    a = int(input())
    while a != 0:
        print('Пожалуйста, вводите данные')
        n = input('Название: ')
        p = int(input('Мощность освещения (Вт): '))
        c = int(input('Потребляемая энергия (Вт/ч): '))
        l = int(input('Срок службы (ч): '))
        print('Хотите увеличить введённые данные модели?')
        k = input('(Да или Нет): ')
        if k == 'Да':
            print('Какие данные хотите увеличить?')
            d = input("1 - мощность освещения, 2 - потребляемая энергия: ")
            print('На сколько хотите увеличить?')
            f = H(int(input('Введите целое число: ')))
            if d == '1':
                p = int(H.__add__(H(p), f))
            else:
                c = int(H.__add__(H(c), f))
        else:
            print('Хорошо')
        if a == 1:
            l2 = int(input('Длина изделия (мм): '))
            L = Bulb(n,p, c, l, l2)
        else:
            w = int(input('Вес (г): '))
            L = Projector(n, p, c, l, w)
        print('Вот полученная информация:')
        L.Info()
        L.Work()
        L.Rat()
        print('Нажмите 0, если хотите закончить, или другую цифру, если хотите продолжить')
        a = int(input())
        if a == 0:
            break
        print('Нажмите 1, если вы вносите характеристики Лампы дневного освещения')
        print('Нажмите 2, если вы вносите характеристики Прожектора')
        a = int(input())
    print('Спасибо за заполнение!')
else:
    print('Хорошо, до свидания!')

