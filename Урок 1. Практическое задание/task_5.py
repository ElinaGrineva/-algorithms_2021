"""
Задание 5.

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]
"""


class Plates:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        self.elems.insert(0, el)
        self.notify()

    def pop_out(self):
        return self.elems.pop(0)

    def get_val(self):
        return self.elems[0]

    def stack_size(self):
        return len(self.elems)

    def notify(self):
        max_place = 3
        if len(self.elems) >= max_place:
            print('Используйте новый стек')
        else:
            print(f'Будьте внимательны. Лимит тарелок 3 шт.')


plates = Plates()

plates.push_in(10)
plates.push_in(2)
plates.push_in(1)



