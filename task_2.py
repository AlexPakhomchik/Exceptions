class Counter:
    now_step = 0

    def __init__(self, start: int, step=None, stop=None):
        self.start = start
        self.step = step
        self.stop = stop

    @classmethod
    def __str__(cls):
        return f'Значение на данный момент: {cls.now_step}'

    def do_step(self):
        """изменяет значение текущего шага на 1 или на значение step (если оно задано)"""
        if self.now_step == 0:
            self.now_step = self.start
        if self.step is None:
            if self.stop is None:
                self.now_step += 1
            elif (self.now_step + 1) == self.stop:
                raise LookupError('Превышено значение stop')
            else:
                self.now_step += 1
        else:
            if self.stop is None:
                self.now_step += self.step
            else:
                if (self.now_step + self.step) >= self.stop:
                    raise LookupError('Превышено значение stop')
                else:
                    self.now_step += self.step
