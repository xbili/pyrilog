import click

from pyrilog.core.wire import Wire
from pyrilog.fma import create
from pyrilog.verilog import generate


@click.command()
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
def main(size, width, output_dir, with_cpa, with_pipeline):
    print('WARNING: Current implementation only includes a multiplier')

    inputs, output, entities = create(width, size, cpa=with_cpa)
    generated = generate(inputs, [output], entities)

    with open(output_dir, 'w') as f:
        f.write(generated)

    print('Success! Generated Verilog file saved at {}'.format(output_dir))

if __name__ == '__main__':
    main()
