# Open a file
import sys
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace
print 'a',
# sys.stdout.softspace = 0
print 'b'
