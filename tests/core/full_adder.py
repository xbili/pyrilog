from nose import with_setup

from pyrilog.core.wire import Wire
from pyrilog.core.full_adder import FullAdder

from ..test_utils import reset_counts


@with_setup(reset_counts,)
def test_full_adder():
    in_1, in_2, in_3 = Wire(), Wire(), Wire()
    out_sum, out_carry = Wire(), Wire()

    fa = FullAdder(in_1, in_2, in_3, out_sum, out_carry)

    assert fa.inputs == [in_1, in_2, in_3]
    assert fa.outputs == [out_sum, out_carry]
