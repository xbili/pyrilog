from nose import with_setup

from pyrilog.core.wire import Wire
from pyrilog.multiplier import create
from pyrilog.verilog import generate

from .test_utils import reset_counts

@with_setup(reset_counts,)
def test_generate():
    multiplier = [Wire() for _ in range(4)]
    multiplicand = [Wire() for _ in range(4)]

    output, entities = create(multiplier, multiplicand, 4)

    generated = generate([multiplier, multiplicand], [output], entities)

    # TODO: Find out how to test this
