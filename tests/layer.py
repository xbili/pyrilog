from nose import with_setup

from pyrilog import Wire
from pyrilog import Layer

from .utils import reset_counts


@with_setup(reset_counts,)
def test_layer():
    layer = Layer()

    # Default number of columns should be 0
    assert layer.get_columns() == 0

    # Default number of rows should be 0
    assert layer.get_rows() == 0

    # Add a wire to the layer
    wire_1 = Wire(1)
    layer.add_wire(wire_1)

    assert layer.get_columns() == 2
    assert layer.get_rows() == 1

    # Get wires in the layer
    wires = layer.get_wires()

    assert len(wires) == 1
    assert wires[0] == wire_1

    # Get wires in a single column
    col_1_wires = layer.get_wires(col=1)

    assert len(wires) == 1
    assert wires[0] == wire_1

    assert len(layer.get_wires(col=2)) == 0
