from .entity import Entity


class Gate(Entity):

    def __init__(self, in_1, in_2, out):
        self._in_1 = in_1
        self._in_2 = in_2
        self._out = out

    @property
    def inputs(self):
        return [self._in_1, self._in_2]

    @property
    def outputs(self):
        return [self._out]


class And(Gate):
    pass


class Or(Gate):
    pass


class Not(Gate):
    pass
