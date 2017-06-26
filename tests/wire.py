from nose import with_setup

from pyrilog import Wire

from .utils import reset_counts


@with_setup(reset_counts,)
def test_wire():
    column = 1
    wire_1 = Wire(column)

    assert wire_1.id == 0
    assert Wire.get_count() == 1
    assert wire_1.column == column

    wire_2 = Wire(column)
    assert Wire.get_count() == 2
    assert wire_2.id == 1
    assert wire_2.column == column
