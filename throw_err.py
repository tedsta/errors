#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import sys

def print_usage():
    """Print usage and exit"""
    sys.stderr.write("usage: python raise_err.py <error type>\n")
    sys.stderr.write("available errors: \n")
    sys.stderr.write("\tassertion, io, import, index\n")
    sys.stderr.write("\tkey, name, os, type, value,\n")
    sys.stderr.write("\tzerodivision\n")
    sys.exit()

# Check args
if len(sys.argv) != 2:
    print_usage()

error_type = sys.argv[1]

if error_type == "assertion":
    raise AssertionError
elif error_type == "io":
    raise IOError
elif error_type == "import":
    raise ImportError
elif error_type == "index":
    raise IndexError
elif error_type == "key":
    raise KeyError
elif error_type == "name":
    raise NameError
elif error_type == "os":
    raise OSError
elif error_type == "type":
    raise TypeError
elif error_type == "value":
    raise ValueError
elif error_type == "zerodivision":
    raise ZeroDivisionError
else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()
