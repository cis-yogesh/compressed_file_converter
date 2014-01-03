#!/usr/bin/env python2.7
# ­*­ coding: utf­8 ­*­
import sys
import time
from optparse import OptionParser

from models.handler import Handler

def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-f", "--file", 
            dest="filename",
            type=str,
            help="provid original file Name with path",
            metavar="FILE"
        )
    parser.add_option("-o", "--output", 
            dest="out_file",
            type=str,
            help="provid target file Name",
            metavar="FILE"
        )
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    options, args = parser.parse_args()
    handler = Handler()
    handler.set_filename=options.filename
    handler.output = options.out_file
    handler.execute()
    
if __name__ == "__main__":
    main()
