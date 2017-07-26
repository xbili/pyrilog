from nose import with_setup

from pyrilog import Wire
from pyrilog import FullAdder

from ..utils import reset_counts


@with_setup(reset_counts,)
def test_full_adder():
    in_1 = Wire(1)
    in_2 = Wire(2)
    in_3 = Wire(3)
    out_sum = Wire(1)
    out_carry = Wire(2)

    fa = FullAdder(in_1, in_2, in_3,
                   out_sum, out_carry)

    assert fa.id == 0
    assert fa.get_output_wires() == (out_sum, out_carry)
    assert fa.get_input_wires() == (in_1, in_2, in_3)

    fa_2 = FullAdder(in_1, in_2, in_3,
                     out_sum, out_carry)
    assert fa_2.id == 1
    assert FullAdder.get_count() == 2
