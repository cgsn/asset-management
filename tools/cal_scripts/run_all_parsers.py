#!/usr/bin/env python
import os
import glob
import subprocess
import time

def main():
    for parser in glob.glob('*_cal_parser.py'):
        command = ['python2.7', parser]
        p = subprocess.Popen(command)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
