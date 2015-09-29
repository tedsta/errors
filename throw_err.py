#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import sys
import argparse

class TeddyError(Exception):
        def __init__(self, message, some_param):
            super(TeddyError, self).__init__(message)
            self.some_param = some_param

available_errors = ["assertion", "io", "import", 
                    "index", "key", "name", "os", "type",
                    "value", "zerodivision", "teddy"]
parser = argparse.ArgumentParser()
parser.add_argument("error_type",
                choices=available_errors)
args = parser.parse_args()
error_type = args.error_type

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
elif error_type == "teddy":
    raise TeddyError("something horrible happened", 125)
else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()
