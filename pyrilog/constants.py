# Templates for Verilog code

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
