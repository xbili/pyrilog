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

    @property
    def verilog(self):
        pass


class And(Gate):
    @property
    def verilog(self):
        return 'and({}, {}, {});'.format(
            self._out.verilog,
            self._in_1.verilog,
            self._in_2.verilog,
        )


class Or(Gate):
    @property
    def verilog(self):
        return 'or({}, {}, {});'.format(
            self._out.verilog,
            self._in_1.verilog,
            self._in_2.verilog,
        )


class Not(Gate):
    @property
    def verilog(self):
        return 'not({}, {});'.format(
            self._out.verilog,
            self._in_1.verilog,
        )
