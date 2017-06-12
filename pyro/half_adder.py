class HalfAdder(object):
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
        self._out_sum = out_sum
        self._out_carry = out_carry

        HalfAdder._count += 1

    def get_output_wires(self):
        """Returns the output wires of the full adder"""
        return self._out_sum, self._out_carry

    def get_input_wires(self):
        """Returns the input wires of the full adder"""
        return self._in_1, self._in_2

    def reset_count():
        HalfAdder._count = 0
