import click

from pyrilog.core.wire import Wire
from pyrilog.fma import create
from pyrilog.verilog import generate
from pyrilog import multiplier as multiplier_creator


@click.group()
def main():
    pass

@main.command()
@click.option(
    '--size',
    default=4,
    help='size of the vectors that we want to perform dot product operations on.',
)
@click.option(
    '--width',
    default=4,
    help='bit width of each element in the vectors that we want to perform dot product on.'
)
@click.option(
    '--output-dir',
    default='./generated.v',
    help='the output directory of your generated Verilog file, defaults to your current directory.'
)
@click.option(
    '--with-cpa',
    is_flag=True,
    help='the final layer CPA will be generated if this flag is present.'
)
@click.option(
    '--with-pipeline',
    is_flag=True,
    help="we'll include latches in between the stages of the partial product reduction tree if this option is checked."
)
def fma(size, width, output_dir, with_cpa, with_pipeline):
    inputs, output, entities = create(width, size, cpa=with_cpa)
    generated = generate(inputs, [output], entities)

    with open(output_dir, 'w') as f:
        f.write(generated)

    print('Success! Generated Verilog file saved at {}'.format(output_dir))

@main.command()
@click.option(
    '--width',
    default=4,
    help='bit width of each number that we want to multiply.'
)
@click.option(
    '--output-dir',
    default='./generated.v',
    help='the output directory of your generated Verilog file, defaults to your current directory.'
)
@click.option(
    '--with-cpa',
    is_flag=True,
    help='the final layer CPA will be generated if this flag is present.'
)
@click.option(
    '--with-pipeline',
    is_flag=True,
    help="we'll include latches in between the stages of the partial product reduction tree if this option is checked."
)
def multiplier(width, output_dir, with_cpa, with_pipeline):
    print('Generating multiplier of two operands, {}-bits wide each.'.format(width))

    multiplier_in = [Wire() for _ in range(width)]
    multiplicand_in = [Wire() for _ in range(width)]

    output, entities = multiplier_creator.create(
        multiplier_in,
        multiplicand_in,
        width
    )
    generated = generate([multiplier_in, multiplicand_in], [output], entities)

    with open(output_dir, 'w') as f:
        f.write(generated)

    print('Success! Generated Verilog file saved at {}'.format(output_dir))


@main.command()
@click.option(
    '--size',
    default=4,
    help='size of the vectors that we want to perform dot product operations on.',
)
@click.option(
    '--width',
    default=4,
    help='bit width of each element in the vectors that we want to perform dot product on.'
)
@click.option(
    '--output-dir',
    default='./generated.v',
    help='the output directory of your generated Verilog file, defaults to your current directory.'
)
@click.option(
    '--with-cpa',
    is_flag=True,
    help='the final layer CPA will be generated if this flag is present.'
)
@click.option(
    '--with-pipeline',
    is_flag=True,
    help="we'll include latches in between the stages of the partial product reduction tree if this option is checked."
)
def pprt(size, width, output_dir, with_cpa, with_pipeline):
    print('Generating reduction tree of {} operands, {}-bits wide each.'.format(size, width))

    inputs = []
    for _ in range(size):
        inputs += [[Wire() for _ in range(width)]]
    penultimate, pprt_entities = multiplier_creator._reduce_partial_products(inputs)
    output, cpa_entities = multiplier_creator._carry_propagate(penultimate)

    generated = generate(inputs, [output], pprt_entities + cpa_entities)

    with open(output_dir, 'w') as f:
        f.write(generated)

    print('Success! Generated Verilog file saved at {}'.format(output_dir))


if __name__ == '__main__':
    main()
