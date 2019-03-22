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

def main():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("--file1", help="File 1 Name", required=True, type=str)
    parser.add_argument("--file2", help="File 2 Name", required=True, type=str)
    
    parser.add_argument("--file1header", help="File 1 Header, comma separated (optional)", required=False, type=str)
    parser.add_argument("--file2header", help="File 2 Header, comma separated (optional)", required=False, type=str)
    
    parser.add_argument("--file1sep", help="File 1 Delimiter. Default: whitespace", required=False, type=str)
    parser.add_argument("--file2sep", help="File 2 Delimiter. Default: whitespace", required=False, type=str)
    
    parser.add_argument("--file1key", help="File 1 Key Column, either integer index or column name", required=False, type=str)
    parser.add_argument("--file2key", help="File 2 Key Column, either integer index or column name", required=False, type=str)
    
    parser.add_argument("--intkey", help="Key specified as integer index, boolean value. Keys should be integer index if headers not supplied", type=str2bool, nargs='?', default=False)
    
    parser.add_argument("--out", help="Output file name", required=True, type=str)
    args = parser.parse_args()
    
    file1 = args.file1
    file2 = args.file2
    
    if args.file1header:
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
            
    if args.intkey:
        file1data = file1data.set_index(list(file1data.columns.values)[int(args.file1key)-1])
        file2data = file2data.set_index(list(file2data.columns.values)[int(args.file2key)-1])
    else:
        file1data = file1data.set_index(args.file1key)
        file2data = file2data.set_index(args.file2key)
        
    mergeddata = file1data.merge(file2data, left_index=True, right_index=True).reset_index()
    
    mergeddata.to_csv(args.out, index=False, sep="\t")

        
if __name__ == "__main__":
    main()
