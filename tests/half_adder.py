from nose import with_setup

from pyrilog import Wire
from pyrilog import HalfAdder

from .utils import reset_counts


@with_setup(reset_counts,)
def test_half_adder():
    in_1 = Wire(1)
    in_2 = Wire(2)
    out_sum = Wire(1)
    out_carry = Wire(2)

    ha = HalfAdder(in_1, in_2,
                   out_sum, out_carry)

    assert ha.id == 0
    assert ha.get_output_wires() == (out_sum, out_carry)
    assert ha.get_input_wires() == (in_1, in_2)
