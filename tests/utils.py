from pyrilog import Wire
from pyrilog import HalfAdder
from pyrilog import FullAdder


def reset_counts():
    Wire.reset_count()
    HalfAdder.reset_count()
    FullAdder.reset_count()
