#exercise 16, study drill 2

from sys import argv

script, filename = argv

read_text = open(filename)
print "Here is your %s" %filename

print read_text.read()

read_text.close()

