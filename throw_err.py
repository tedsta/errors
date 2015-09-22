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
    assert(0 == 1)
elif error_type == "io":
    print('\n'.join(open('asdfasdfsdfsd', 'r').lines()))
elif error_type == "import":
    import superdupercooperlooper
elif error_type == "index":
    print([1, 2, 3][3])
elif error_type == "key":
    {'cow':'moo', 'cat':'meow', 'dog':'woof'}['fox'] # What does the fox say?
elif error_type == "name":
    print(superduper)
elif error_type == "os":
    import os
    os.chdir('/bin/bin/bin/bin/bin/bin/bin/bin')
elif error_type == "type":
    print(1 + "asdf")
elif error_type == "value":
    print(int('asdf'))
elif error_type == "zerodivision":
    1 / 0
else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()
