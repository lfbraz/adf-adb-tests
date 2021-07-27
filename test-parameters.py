import argparse
import sys

def main(args, args2):
    print(f'My args:{args}')
    print(f'My args 2:{args2}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str)
    parser.add_argument('--first_arg', type=str)
    args = parser.parse_args()
    main(sys.argv, args)
