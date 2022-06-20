class Tomato:
    states = {1:'flover', 2:'green', 3:'medium', 4:'ripe'}
    def __init__(self, index):
        self._index = index
        self._state = self.states[1]
    def grow(self):
        m = 0
        for i in self.states:
            if self._state == self.states[i]:
                m = i+1
        self._state = self.states[m]
        print('Текущая стадия ', self._state)
        return self._state
    def is_ripe(self):
        if self._state == 'ripe':
            return True
        else:
            return False

class TomatoBush:
    def __init__(self, count):
        self.count = count
        self.tomatoes = list()
        for i in range (self.count):
            self.tomatoes.append(Tomato(i))
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()
    def all_are_ripe(self):
        n = 0
        for i in self.tomatoes:
            if i.is_ripe():
                n += 1
        if n == len(self.tomatoes):
                return True
    def give_away_all(self):
        self.tomatoes.clear()
        print('Урожай собран! ')

class Gardener:
    def __init__(self, name, object):
        self.name = name
        self._plant = object
    def work(self):
        print('work:')
        self._plant.grow_all()
    def harvest(self):
        print('harvest:')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print('Not all tomatoes are ripe!')
    @staticmethod
    def knowledge_base():
        print('Томаты любят тепло и свет. Хороший урожай помидоров вырастает на кустах, освещенных интенсивным, ярким, светом. \nПасмурная погода сильно задерживает рост кустов и формирование помидоров. \nПомидоры при недостатке света созревают медленно, кислые на вкус, имеют слабый аромат.'
        '\nТепло крайне важно для томатов. \nСемена томата начинают прорастать при температуре +15 °C, но оптимальная температура намного выше — +25 °С. \nПри низкой температуре, ниже +10°C, рост томатов прекращается. '
        '\nТоматы не плодоносят при температуре ниже +15°C и выше +35°C. \nЦветение томатов прекращается при температуре ниже +12°C и выше +30°C. \nЦветки томатов опадают при сильном, резком, похолодании, скажем с +25°C до +10°C.\n')

Gardener.knowledge_base()
tomato_bush = TomatoBush(7)
gardener = Gardener('Maxim', tomato_bush)
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()









