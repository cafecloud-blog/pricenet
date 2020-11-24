#!/usr/bin/env python3
""" creates data sets for pricenet traiing """

import argparse

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-i',
        '--input',
        help='path to the input raw data',
        required=True
    )

    parser.add_argument(
        '-o',
        '--output',
        help='name of the output file that will contain the dataset',
        required=True
    )

    DEFAULT_WINDOW=15
    parser.add_argument(
        '-w',
        '--window',
        help=f'number of trading days used to build each training examples. Defaults to {DEFAULT_WINDOW}',
        default=DEFAULT_WINDOW,
        type=int
    )

    args = parser.parse_args()
    print(args)

    return

if __name__ == '__main__':
    main()


