from nose import with_setup

from pyrilog import Wire
from pyrilog import HalfAdder
from pyrilog import FullAdder
from pyrilog import Generator
from pyrilog import Wallace
from pyrilog import Layer


def reset_counts():
    Wire.reset_count()
    HalfAdder.reset_count()
    FullAdder.reset_count()


@with_setup(reset_counts,)
def test_full_adder():
    in_1 = Wire(1)
    in_2 = Wire(2)
    in_3 = Wire(3)
    out_sum = Wire(1)
    out_carry = Wire(2)

    fa = FullAdder(in_1, in_2, in_3,
                   out_sum, out_carry)

    assert fa.id == 0
    assert fa.get_output_wires() == (out_sum, out_carry)
    assert fa.get_input_wires() == (in_1, in_2, in_3)


@with_setup(reset_counts,)
def test_half_adder():
    in_1 = Wire(1)
    in_2 = Wire(2)
    out_sum = Wire(1)
    out_carry = Wire(2)

    ha = HalfAdder(in_1, in_2,
                   out_sum, out_carry)

    assert ha.id == 0
    assert ha.get_output_wires() == (out_sum, out_carry)
    assert ha.get_input_wires() == (in_1, in_2)


@with_setup(reset_counts,)
def test_wire():
    column = 1
    wire_1 = Wire(column)

    assert wire_1.id == 0
    assert wire_1.column == column

    wire_2 = Wire(column)
    assert wire_2.id == 1
    assert wire_2.column == column

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
