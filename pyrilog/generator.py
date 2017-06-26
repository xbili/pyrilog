from .wire import Wire

class Generator(object):
    """Generates Verilog HDL code."""

    FULL_ADDER = 'full_adder fa_{id}({out_sum}, {out_carry}, {in_1}, {in_2}, {in_3});'
    HALF_ADDER = 'half_adder ha_{id}({out_sum}, {out_carry}, {in_1}, {in_2});'
    WIRES = 'wire [{count}:0] wires;'
    WIRE = 'wires[{id}]'
    RESULT_WIRE = 'assign sum[{}] = {};'
    INPUT_WIRE = 'assign wires[{wire_id}] = in_{input_num}[{col}];'

    MODULE = 'module {name}({outputs}, {inputs});'
    INPUT = 'input [{input_width}:0] {inputs};'
    OUTPUT = 'output [{output_width}:0] {outputs};'
    ENDMODULE = 'endmodule'

    OUTPUT_WIRE_NAME = 'sum'

    def __init__(self, name):
        """Creates a new generator for the module"""
        self._name = name


    def ingest(self, wallace):
        """Takes in a Wallace tree and generates the code to internal memory"""

        # Get inputs of the Wallace tree
        inputs = self._get_inputs(wallace)
        start = self.MODULE.format(name=self._name,
                                   inputs=', '.join(inputs),
                                   outputs=self.OUTPUT_WIRE_NAME)

        declare_in = self.INPUT.format(input_width=wallace.get_width()-1,
                                       inputs=', '.join(inputs))

        declare_out = self.OUTPUT\
            .format(output_width=wallace.get_result_bit_width()-1,
                    outputs=self.OUTPUT_WIRE_NAME)

        self._lines = [start, declare_in, declare_out]
        self._lines.append(self._declare_wires())

        for inpt in self._assign_input_wires(wallace):
            self._lines.append(inpt)

        for ha in wallace._half_adders:
            self._lines.append(self._half_adder(ha))

        for fa in wallace._full_adders:
            self._lines.append(self._full_adder(fa))

        result = wallace.get_result()
        for idx, wire in enumerate(result.get_wires()):
            self._lines.append(self.RESULT_WIRE.format(idx,
                                                       self._wire(wire)))

        self._lines.append(self.ENDMODULE)


    def generate(self):
        return '\n'.join(self._lines)


    def _get_inputs(self, wallace):
        return ['in_{}'.format(i) for i in range(0, wallace.get_operands())]


    def _assign_input_wires(self, wallace):
        """Assign each input wire into their respective wires."""

        res = []

        layer = wallace.get_input_layer()
        for col in range(0, layer.get_columns()):
            for row, wire in enumerate(layer.get_wires(col=col)):
                res.append(self.INPUT_WIRE.format(wire_id=wire.id,
                                                  input_num=row,
                                                  col=col))

        return res


    def _declare_wires(self):
        return self.WIRES.format(count=Wire.get_count())


    def _half_adder(self, half_adder):
        out_sum, out_carry = half_adder.get_output_wires()
        in_1, in_2 = half_adder.get_input_wires()

        return self.HALF_ADDER.format(id=half_adder.id,
                                      out_sum=self._wire(out_sum),
                                      out_carry=self._wire(out_carry),
                                      in_1=self._wire(in_1),
                                      in_2=self._wire(in_2))


    def _full_adder(self, full_adder):
        out_sum, out_carry = full_adder.get_output_wires()
        in_1, in_2, in_3 = full_adder.get_input_wires()

        return self.FULL_ADDER.format(id=full_adder.id,
                                      out_sum=self._wire(out_sum),
                                      out_carry=self._wire(out_carry),
                                      in_1=self._wire(in_1),
                                      in_2=self._wire(in_2),
                                      in_3=self._wire(in_3))


    def _wire(self, wire):
        if wire == None:
            return ''

        return self.WIRE.format(id=wire.id)
