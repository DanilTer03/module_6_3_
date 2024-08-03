class Horse:
    sound = 'Frrr'  # Звук, который издает лошадь

    def __init__(self):
        self.x_distance = 0  # Начальная точка пути

    def run(self, dx):
        self.x_distance += dx  # Изменение пройденного пути на dx


class Eagle:
    sound = 'I train, eat, sleep, and repeat'  # Звук, который издает орел

    def __init__(self):
        self.y_distance = 0  # Начальная высота полета

    def fly(self, dy):
        self.y_distance += dy  # Изменение высоты полета на dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)  # Инициализируем родительский класс Horse
        Eagle.__init__(self)  # Инициализируем родительский класс Eagle

    def move(self, dx, dy):
        self.run(dx)  # Вызов метода run из класса Horse
        self.fly(dy)  # Вызов метода fly из класса Eagle

    def get_pos(self):
        return self.x_distance, self.y_distance  # Возврат текущего положения

    def voice(self):
        print(self.sound)  # Вывод звука


# Пример работы программы
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

print(Pegasus.mro())
