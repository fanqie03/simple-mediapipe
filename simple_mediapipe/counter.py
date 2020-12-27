class Counter:
    """The abstract class of counter."""

    def __init__(self, name): ...

    def increment(self): ...

    def incrementBy(self, amount: int): ...

    def get(self): ...


class BasicCounter(Counter):
    # TODO add mutex lock
    def __init__(self, name):
        super().__init__(name)
        self.value = 0

    def increment(self):
        self.value += 1

    def incrementBy(self, amount: int):
        self.value += amount

    def get(self):
        return self.value


class CounterFactory:
    """Generic counter factory"""

    def getCounter(self, name): ...


class BasicCounterFactory(CounterFactory):
    """Counter factory that makes the counters be our own basic counters."""

    def __init__(self):
        self._counter_set = dict()

    def getCounter(self, name: str):
        item = self._counter_set.get(name)
        if item is not None:
            return item
        else:
            counter = BasicCounter(name)
            self._counter_set[name] = counter
            return counter
