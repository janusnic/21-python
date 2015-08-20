# -*- coding:utf-8 -*-

import os

filename = 'file.txt'
try:
    f = open (filename, 'r')
    try:
        print f.read()
    finally:
        f.close()
# except OSError as ex:
except (os.error, OSError) as ex:
    print "Cannot process file", filename, ": Error is", ex
