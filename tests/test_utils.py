from pyrilog.core.wire import Wire
from pyrilog.core.half_adder import HalfAdder
from pyrilog.core.full_adder import FullAdder


def reset_counts():
    Wire.reset_count()
    HalfAdder.reset_count()
    FullAdder.reset_count()
