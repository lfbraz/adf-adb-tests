import argparse
import sys

def main(args):
    print(f'My args:{args}')


if __name__ == "__main__":
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--first_arg', type=str)
    #args = parser.parse_args()
    main(sys.argv)
