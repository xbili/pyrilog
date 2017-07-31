from .entity import Entity
from pyrilog.constants import HALF_ADDER


class HalfAdder(Entity):
    """HalfAdder encapsulates a hardware gate level half adder."""

    _count = 0

    def __init__(self, in_1, in_2, out_sum, out_carry):
        """
        Construct a new 'HalfAdder' object

        :param in_1, in_2: 2 input wires
        :param out_1, out_2: 2 output wires
        """
        self.id = HalfAdder._count
        self._in_1 = in_1
        self._in_2 = in_2
        self._sum = out_sum
        self._carry = out_carry

        HalfAdder._count += 1

    @property
    def outputs(self):
        """Returns the output wires of the full adder"""
        return [self._sum, self._carry]

    @property
    def inputs(self):
        """Returns the input wires of the full adder"""
        return [self._in_1, self._in_2]

    @property
    def verilog(self):
        return HALF_ADDER.format(
            id=self.id,
            out_sum=self._sum.verilog,
            out_carry=self._carry.verilog,
            in_1=self._in_1.verilog,
            in_2=self._in_2.verilog,
        )

    @classmethod
    @property
    def count(cls):
        return cls._count

    @classmethod
    def reset_count(cls):
        cls._count = 0
