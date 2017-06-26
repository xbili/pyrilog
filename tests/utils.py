from pyrilog import Wire
from pyrilog import HalfAdder
from pyrilog import FullAdder
from pyrilog import Layer


def reset_counts():
    Wire.reset_count()
    HalfAdder.reset_count()
    FullAdder.reset_count()
    Layer.reset_count()
