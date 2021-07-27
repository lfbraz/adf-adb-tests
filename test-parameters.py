import argparse
import sys

def main(args_sys, args_parser):
    print(f'My args (using sys.argv):{args_sys}')
    print(f'My args (using argparse):{args_parser}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('first_arg', type=str)
    args_parser = parser.parse_args()
    main(sys.argv, args_parser)
