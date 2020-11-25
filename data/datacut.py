#!/usr/bin/env python3
""" creates data sets for pricenet traiing """

import argparse
import glob

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
        help='name of the directory where training examples will be saved',
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


    DEFAULT_TARGET=1
    parser.add_argument(
        '-t',
        '--target',
        help='how far ahead in the future the label is determined from',
        default=DEFAULT_TARGET
    )

    parser.add_argument(
        '-k',
        '--keep-shorter',
        action='store_true',
        default=True
    )

    args = parser.parse_args()

    return

def create_training_examples(input_dir, out_dir, window, target):
    """ creates the training examples from """


if __name__ == '__main__':
    main()


