from nose import with_setup

from pyrilog.core.wire import Wire
from pyrilog.core.half_adder import HalfAdder

from ..test_utils import reset_counts

@with_setup(reset_counts,)
def test_half_adder():
    in_1, in_2 = Wire(), Wire()
    out_sum, out_carry = Wire(), Wire()

    ha = HalfAdder(in_1, in_2, out_sum, out_carry)

    assert ha.inputs == [in_1, in_2]
    assert ha.outputs == [out_sum, out_carry]
