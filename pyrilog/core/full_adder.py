from .entity import Entity


class FullAdder(Entity):
    """FullAdder encapsulates a hardware gate level full adder."""

    _count = 0

    def __init__(self, in_1, in_2, in_3, out_sum, out_carry):
        """
        Construct a new 'FullAdder' object

        :param in_1, in_2, in_3: 3 input wires
        :param out_1, out_2: 2 output wires
        """
        self.id = FullAdder._count

        self._in_1 = in_1
        self._in_2 = in_2
        self._in_3 = in_3
        self._sum = out_sum
        self._carry = out_carry

        FullAdder._count += 1

    @property
    def inputs(self):
        return [self._in_1, self._in_2, self._in_3]

    @property
    def outputs(self):
        return [self._sum, self._carry]

    @classmethod
    @property
    def count(clf):
        return clf._count

    @classmethod
    def reset_count(clf):
        clf._count = 0
