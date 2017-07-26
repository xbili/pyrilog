from nose import with_setup

from pyrilog import Wire
from pyrilog import Layer

from ..utils import reset_counts


@with_setup(reset_counts,)
def test_layer_columns():
    layer = Layer()

    # Default number of columns should be 0
    assert layer.get_columns() == 0


@with_setup(reset_counts,)
def test_layer_rows():
    layer = Layer()

    # Default number of rows should be 0
    assert layer.get_rows() == 0


@with_setup(reset_counts,)
def test_layer_add_wire():
    layer = Layer()

    # Add a wire to the 1 column position of the layer
    # NOTE: Index from 0, so we are actually having 2 columns in the layer now
    wire_1 = Wire(1)
    layer.add_wire(wire_1)

    assert layer.get_columns() == 2
    assert layer.get_rows() == 1

    # Get wires in the layer
    wires = layer.get_wires()

    assert len(wires) == 1
    assert wires[0] == wire_1

    # Get wires in column position 1
    col_1_wires = layer.get_wires(col=1)
    assert len(col_1_wires) == 1
    assert col_1_wires[0] == wire_1

    # Column 2 should have no wires
    assert len(layer.get_wires(col=2)) == 0

    wire_2 = Wire(1)
    layer.add_wire(wire_2)

    assert layer.get_columns() == 2
    assert layer.get_rows() == 2
