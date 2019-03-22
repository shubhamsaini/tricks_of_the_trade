#!/usr/bin/env python
"""

Author: Shubham Saini
shubhamsaini@eng.ucsd.edu

"""


import argparse
import sys
import pandas as pd

def PrintLine(text, f):
    f.write(text+"\n")
    f.flush()

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def main():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("--file1", help="File 1 Name", required=True, type=str)
    parser.add_argument("--file2", help="File 2 Name", required=True, type=str)

    parser.add_argument("--file1header", help="File 1 Header, comma separated (optional). Use None to assign int headers. Default: first line of file used as header", required=False, type=str)
    parser.add_argument("--file2header", help="File 2 Header, comma separated (optional). Use None to assign int headers. Default: first line of file used as header", required=False, type=str)

    parser.add_argument("--file1sep", help="File 1 Delimiter (optional). Default: whitespace", required=False, type=str)
    parser.add_argument("--file2sep", help="File 2 Delimiter (optional). Default: whitespace", required=False, type=str)

    parser.add_argument("--file1key", help="File 1 Key Column, either integer index or column name (optional). Used in conjunction with --file2key. Default: uses column names common to both files as index", required=False, type=str)
    parser.add_argument("--file2key", help="File 2 Key Column, either integer index or column name (optional). Used in conjunction with --file1key. Default: uses column names common to both files as index", required=False, type=str)

    parser.add_argument("--join", help="Join type (optional). Possible values: left, right, outer, inner. Default: inner", required=False, type=str, default="inner")
    #parser.add_argument("--intkey", help="Key specified as integer index, boolean value. Keys should be integer index if headers not supplied", type=str2bool, nargs='?', default=False)

    parser.add_argument("--out", help="Output file name (optional). Default: stdout", required=False, type=str)
    args = parser.parse_args()

    file1 = args.file1
    file2 = args.file2

    if args.file1header:
        if args.file1header == "None":
            if args.file1sep:
                file1sep = args.file1sep
                file1data = pd.read_csv(file1, sep=file1sep, header=None)
            else:
                file1data = pd.read_csv(file1, delim_whitespace=True, header=None)
        else:
            file1header = args.file1header.split(",")
            if args.file1sep:
                file1sep = args.file1sep
                file1data = pd.read_csv(file1, names=file1header, sep=file1sep)
            else:
                file1data = pd.read_csv(file1, names=file1header, delim_whitespace=True)
    else:
        if args.file1sep:
            file1sep = args.file1sep
            file1data = pd.read_csv(file1, sep=file1sep)
        else:
            file1data = pd.read_csv(file1, delim_whitespace=True)

    if args.file2header:
        if args.file2header == "None":
            if args.file2sep:
                file2sep = args.file2sep
                file2data = pd.read_csv(file2, sep=file2sep, header=None)
            else:
                file2data = pd.read_csv(file2, delim_whitespace=True, header=None)
        else:
            file2header = args.file2header.split(",")
            if args.file2sep:
                file2sep = args.file2sep
                file2data = pd.read_csv(file2, names=file2header, sep=file2sep)
            else:
                file2data = pd.read_csv(file2, names=file2header, delim_whitespace=True)
    else:
        if args.file2sep:
            file2sep = args.file2sep
            file2data = pd.read_csv(file2, sep=file2sep)
        else:
            file2data = pd.read_csv(file2, delim_whitespace=True)

    if args.file1key:
        if is_int(args.file1key):
            file1key = int(args.file1key) - 1
        else:
            file1key = args.file1key
        file1data = file1data.set_index(file1key)

    if args.file2key:
        if is_int(args.file2key):
            file2key = int(args.file2key) - 1
        else:
            file2key = args.file2key
        file2data = file2data.set_index(file2key)


    if args.file1key and args.file2key:
        mergeddata = file1data.merge(file2data, left_index=True, right_index=True, how=args.join).reset_index()
    else:
        mergeddata = file1data.merge(file2data, how=args.join)

    if args.out:
        mergeddata.to_csv(args.out, index=False, sep="\t")
    else:
        print mergeddata

if __name__ == "__main__":
    main()
