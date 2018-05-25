#!/usr/bin/env python
"""

Author: Shubham Saini
shubhamsaini@eng.ucsd.edu

"""


import argparse
import sys

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
    parser.add_argument("--arg1", help="Argument 1 description", required=True, type=str)
    parser.add_argument("--boolean-arg", type=str2bool, nargs='?', default=True)
    parser.add_argument("--out", help="Output file name. Default: stdout", required=False, type=str)
    args = parser.parse_args()

    # Prepare output
    if args.out: outf = open(args.out,"w")
    else: outf = sys.stdout
    
    PrintLine("Run Successful! Exiting Now...", outf)
        
if __name__ == "__main__":
    main()