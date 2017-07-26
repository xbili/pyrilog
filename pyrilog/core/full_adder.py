class FullAdder(object):
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
        self._out_sum = out_sum
        self._out_carry = out_carry

        FullAdder._count += 1

    def get_output_wires(self):
        """Returns the output wires of the full adder"""
        return self._out_sum, self._out_carry

    def get_input_wires(self):
        """Returns the input wires of the full adder"""
        return self._in_1, self._in_2, self._in_3

    @classmethod
    def reset_count(clf):
        clf._count = 0

    @classmethod
    def get_count(clf):
        return clf._count
