#!/usr/bin/env python

import os
import sys
import time

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("Usage: bench <pi program>")
        sys.exit()

    pi_file = os.path.join(os.getcwd(), "PI.txt");

    with open(pi_file, "r") as F:
        PI = F.readlines()[0][:31339] # Const Pi with 31337 digits after comma

    command = " ".join(sys.argv[1:])

    st = time.process_time()

    # TODO: Execute Pi program and verify output

    et = time.process_time()

    res = et - st

    print("Execution time: {} ms".format(res * 1000))


    