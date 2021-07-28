# Copyright (c) Open Enclave SDK contributors.
# Licensed under the MIT License.

import glob
import os
import sys

def get_tests(dirs):
    tests = []
    for d in dirs:
        files = glob.glob(d + "/*.c")
        for f in files:
            t = os.path.basename(f).split('.')[0]
            tests.append((t, f))
    print(tests)
    return tests

def emit_aggregator(tests):
    f = open('test.c', 'w')
    for (t, fn) in tests:
        f.write('#define main %s\n' % t)
        f.write('#include "%s"\n' % fn)
        f.write('#undef main\n')
    f.write("\n")


if __name__ == "__main__":
    tests = get_tests(sys.argv[1:])
    emit_aggregator(tests)
