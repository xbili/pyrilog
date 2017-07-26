from nose import with_setup

from pyrilog import Wallace
from pyrilog.utils import result_bit_width

from ..utils import reset_counts

@with_setup(reset_counts,)
def test_wallace_constructor():
    k = 5
    width = 8
    wallace = Wallace(k, width)

    assert wallace.operands == k
    assert wallace.width == width
    assert wallace.result_width == result_bit_width(k, width)
    assert wallace.input_layer.get_columns() == result_bit_width(k, width)
    assert wallace.result.get_columns() == result_bit_width(k, width)
