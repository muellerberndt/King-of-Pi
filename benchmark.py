#!/usr/bin/env python

import os
import sys
import time
import subprocess

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("Usage: bench <pi program>")
        sys.exit()

    pi_file = os.path.join(os.getcwd(), "PI.txt");

    with open(pi_file, "r") as F:
        PI = F.readlines()[0][:10002] # Const Pi with 10000 digits after comma. 2 extra chars for "3."

    command = sys.argv[1:]

    st = time.time()

    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    process.wait()

    et = time.time()

    result = process.stdout.read().decode("utf-8").rstrip()
    res = et - st

    if (result == PI):
      print("Result is correct.")
      print("Execution time: {} ms".format(res * 1000))
    else:
      print ("Result is incorrect.\nReturned value: {}\n\nExpected value: {}".format(result, PI));


    