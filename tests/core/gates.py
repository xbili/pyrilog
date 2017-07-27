from nose import with_setup

from pyrilog.core.wire import Wire
from pyrilog.core.gates import And, Or

from ..test_utils import reset_counts


@with_setup(reset_counts,)
def test_and_gate():
    in_1, in_2 = Wire(), Wire()
    out = Wire()

    and_gate = And(in_1, in_2, out)

    assert and_gate.inputs == [in_1, in_2]
    assert and_gate.outputs == [out]


@with_setup(reset_counts,)
def test_or_gate():
    in_1, in_2 = Wire(), Wire()
    out = Wire()

    or_gate = Or(in_1, in_2, out)

    assert or_gate.inputs == [in_1, in_2]
    assert or_gate.outputs == [out]
