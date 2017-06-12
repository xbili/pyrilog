import sys
import getopt

from wallace import Wallace
from generator import Generator

USAGE = 'Usage: {} -k <operands> -w <width> -n <name of module> -o <output file>'

if __name__ == '__main__':
    try:
        myopts, args = getopt.getopt(sys.argv[1:], 'k:w:o:n:')
    except getopt.GetoptError as e:
        print(str(e))
        print(USAGE.format(sys.argv[0]))

    for option, value in myopts:
        if option == '-k':
            operands = int(value)
        elif option == '-w':
            width = int(value)
        elif option == '-n':
            name = value
        elif option == '-o':
            output_file = value

    wallace = Wallace(operands, width)
    generator = Generator(name)

    with open(output_file, 'w') as f:
        f.write(wallace.generate(generator))
