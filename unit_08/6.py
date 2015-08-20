# -*- coding:utf-8 -*-
import os
import traceback

filename = 'file.txt'
try:
    f = open (filename, 'r')
    try:
        print f.read()
    finally:
        f.close()
except (os.error, IOError) as ex:
    traceback.print_exc(ex)
