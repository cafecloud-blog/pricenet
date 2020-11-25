#!/usr/bin/env python3
""" creates data sets for pricenet traiing """

import argparse
import glob
import os

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


    args = parser.parse_args()

    create_training_examples(args.input, args.output, args.window, args.target)

    return

def create_training_examples(input_dir, out_dir, window, target):
    """ creates the training examples from """

    def img_filename(path, index, out_dir):
        """ computes a filename given a path and an index """

        basename = os.path.basename(path).split(".")[0]
        name = f"{basename}_{i}.stonk"

        return os.path.join(out_dir, name)

    # make a list of the files in input dir
    filenames = glob.glob(f"{input_dir}/*.csv")

    # create an image set from each images
    for f in filenames:
        images = image_set(f, window, target)

        for i,img in enumerate(images):
            # generate filename for stonk file
            filename = img_filename(f, i, out_dir)
            # save content in stonkfile

            # make sure the dir for the filename exists.
            os.makedirs(os.path.dirname(filename), exist_ok=True)

    return

def image_set(f):
    """ return an image set built from raw data file f """

    # Load the file as a panda frame ?

    # partition the frame in groups of tar


if __name__ == '__main__':
    main()


