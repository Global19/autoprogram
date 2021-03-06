import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='An integer for the accumulator.')

calculator_opts = parser.add_argument_group('Calculator Options')
calculator_opts.add_argument(
    '-i', '--identity', type=int, default=0,
    help='the default result for no arguments ' '(default: 0)')
calculator_opts.add_argument(
    '--sum', dest='accumulate', action='store_const',
    const=sum, default=max,
    help='Sum the integers (default: find the max).')

if __name__ == '__main__':
    args = parser.parse_args()
    print(args.accumulate(args.integers))
