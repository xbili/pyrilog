from .utils import chunks, result_bit_width
from .layer import Layer
from .wire import Wire
from .half_adder import HalfAdder
from .full_adder import FullAdder

class Wallace(object):
    """
    Wallace encapsulates a Partial Product Reduction Tree (PPRT) structure.
    Wires are grouped together with the Wallace tree algorithm, resulting
    in log(n) layers.
    """

    def __init__(self, k, width):
        """
        Construct a new 'Wallace' object.

        :param n: The total number of inputs into the reduction tree
        :param width: The max width of each input
        """

        self._k = k
        self._width = width
        self._layers = []
        self._full_adders = []
        self._half_adders = []

        # 2D list to represent the input wires
        self._input_wires = []

        self._result_bit_width = result_bit_width(self._k,
                                                  self._width)

        self._build_tree()


    @property
    def operands(self):
        return self._k


    @property
    def width(self):
        return self._width


    @property
    def result_width(self):
        return self._result_bit_width


    @property
    def layers(self):
        return self._layers


    @property
    def input_layer(self):
        return self._layers[0]


    @property
    def result(self):
        """Returns the layer that contains the result bits."""

        # This layer should only have 1 row
        assert self._layers[-1].get_rows() == 1

        return self._layers[-1]


    def _build_tree(self):
        """Builds the PPRT using full and half adders"""

        cpa_layer = self._build_csa_layer()
        result = self._build_cpa_layer(cpa_layer)
        self._layers.append(result)


    def _build_csa_layer(self):
        """
        Builds the Carry Save Adder layers.

        Returns the layer for CPA.
        """

        # Build the first layer with all the input bits first
        curr = Layer(columns=self._result_bit_width)
        for col in range(0, self._width):
            for j in range(0, self._k):
                wire = Wire(col)
                curr.add_wire(wire)

        self._layers.append(curr)

        # Recursively build layers given the next row
        while curr.get_rows() > 2:
            next_layer = self._build_layer(curr)
            self._layers.append(next_layer)

            curr = next_layer

        return curr


    def _build_layer(self, layer):
        """Returns the next layer of the PPRT given the current layer"""

        FULL_ADDER_CHUNK = 3
        HALF_ADDER_CHUNK = 2

        next_layer = Layer(columns=self._result_bit_width)

        for col in range(0, next_layer.get_columns()):
            col_wires = layer.get_wires(col=col)

            for chunk in chunks(col_wires, FULL_ADDER_CHUNK):
                # Make sure that size of each chunk is consistent
                assert len(chunk) <= FULL_ADDER_CHUNK

                if len(chunk) == FULL_ADDER_CHUNK:
                    # Group into a full adder, send outputs into next layer
                    in_1, in_2, in_3 = chunk
                    out_sum = Wire(col)
                    out_carry = Wire(col+1)

                    full_adder = FullAdder(in_1, in_2, in_3,
                                           out_sum, out_carry)

                    self._full_adders.append(full_adder)
                    next_layer.add_wire(out_sum)
                    next_layer.add_wire(out_carry)

                elif len(chunk) == HALF_ADDER_CHUNK:
                    # Group into a half adder, send outputs into next layer
                    in_1, in_2 = chunk
                    out_sum = Wire(col)
                    out_carry = Wire(col+1)

                    half_adder = HalfAdder(in_1, in_2, out_sum, out_carry)

                    self._half_adders.append(half_adder)
                    next_layer.add_wire(out_sum)
                    next_layer.add_wire(out_carry)

                else: # Length 1
                    # Send the bit into the next layer
                    next_layer.add_wire(chunk[0])

        return next_layer


    def _build_cpa_layer(self, layer):
        """
        Returns the result layer that is the result of a Carry Propagate Adder.
        """

        # Ensure that input layer only has 2 rows
        assert layer.get_rows() == 2

        result = Layer(columns=self._result_bit_width)

        # Store the carry in each column
        carry = None

        for col in range(0, layer.get_columns()):
            # Wires in the current column
            wires = layer.get_wires(col=col)

            assert len(wires) <= 2

            if len(wires) == 0:
                continue
            elif len(wires) == 2:
                out_sum = Wire(col)
                out_carry = Wire(col)
                fa = FullAdder(wires[0], wires[1], carry, out_sum, out_carry)

                self._full_adders.append(fa)
                result.add_wire(out_sum)

                carry = out_carry
            elif carry == None:
                result.add_wire(wires[0])
            else: # One wire with carry
                out_sum = Wire(col)
                out_carry = Wire(col)
                ha = HalfAdder(wires[0], carry, out_sum, out_carry)

                self._half_adders.append(ha)
                result.add_wire(out_sum)

                carry = out_carry

        return result
