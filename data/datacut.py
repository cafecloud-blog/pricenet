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


    DEFAULT_TARGET=1
    parser.add_argument(
        '-t',
        '--target',
        help='how far ahead in the future the label is determined from',
        default=DEFAULT_TARGET
    )

    args = parser.parse_args()

    return

def create_design_matrix(input_dir, output_file, window, target):
    """ returns a design matrix built from raw data """

    ## Pseudo-code
    # define result set
    result = []

    # get the list of csv files containing the data
    files = filenames(input)

    # for each files
    for f in files:
        subset_result = process_file(f, window, target)
        result += subset_result




if __name__ == '__main__':
    main()


