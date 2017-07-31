from pyrilog.core.wire import Wire

def generate(inputs, outputs, entities):
    """
    Given the wires and entities of a hardware design, this method generates
    the Verilog code that is synthesizable.

    :type inputs, outputs: List[List[Wire]]
    :type entities: List[Entity]
    """

    res = []
    res += _declare_module(inputs, outputs)
    res += _declare_ports(inputs, outputs)
    res += _declare_wires()
    res += _declare_entities(entities)
    res += 'endmodule'

    return '\n'.join(res)


def _declare_module(inputs, outputs):
    inpt = ['in_{}'.format(i) for i in range(len(inputs))]
    output = ['out_{}'.format(i) for i in range(len(outputs))]
    res = 'module({}, {})'.format(', '.join(inpt), ', '.join(outpt))

    return [res]


def _declare_ports(inputs, outputs):
    """
    Declares and assigns the input and output ports of the HDL design to their
    associated wires.

    :type inputs, outputs: List[List[Wire]]
    :rtype: List[string]
    """

    # Declare inputs and outputs
    declare_in = 'input [{}:0] {}'.format(len(inputs[0]),
                                          ['in_{}'.format(i)
                                           for i in range(len(inputs))])

    declare_out = 'output [{}:0] {}'.format(len(outputs[0]),
                                            ['out_{}'.format(i)
                                             for i in range(len(outputs))])

    # Assign the associated wires
    assign_in = []
    for input_num, inpt in enumerate(inputs):
        for col, wire in inpt:
            fmt = 'assign wires[{wire_id}] = in_{input_num}[{col}]'.format(
                wire_id=wire.id,
                input_num=input_num,
                col=col,
            )
            assign_in += [fmt]

    assign_out = []
    for output_num, output in enumerate(outputs):
        for col, wire in output:
            fmt = 'assign wires[{wire_id}] = out_{output_num}[{col}]'.format(
                wire_id=wire.id,
                output_num=output_num,
                col=col,
            )
            assign_out += [fmt]

    return [declare_in, declare_out, *assign_in, *assign_out]


def _declare_wires():
    """
    Declares the wires to be used in the HDL.

    :rtype: List[string]
    """
    return ['wire [{}:0] wires'.format(Wire.count)]


def _declare_entities(entities):
    """
    Converts the entities present into Verilog. Returns a list of string, with
    each element representing the Verilog representation of the entity.

    :type entities: List[Entity]
    :rtype: List[string]
    """
    res = []
    for entity in entities:
        res += [entity.verilog]

    return res
