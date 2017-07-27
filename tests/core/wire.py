from nose import with_setup

from pyrilog.core.wire import Wire

from ..test_utils import reset_counts

@with_setup(reset_counts,)
def test_wire():
    w1 = Wire()
    assert w1.value == None

    w2 = Wire(1)
    assert w2.value == 1

    w3 = Wire(w2)
    assert w3.value == w2

    w3.value = w1
    assert w3.value == w1
