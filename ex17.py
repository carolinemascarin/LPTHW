#More files
#Exercise 17

from sys import argv
from os.path import exists

script, to_file = argv

out_file = open(to_file, "w")

print "Does the output file exist? %r \n Ready, hit RETURN to continue, CTRL- C to abort." % exists(to_file)
raw_input()

print "Alright, all done."

out_file.close()


#print "Ready, hit RETURN to continue, CTRL- C to abort."
#indata = in_file.read()
#print "The input file is %d bytes long" % len(from_file)
#out_file.write(from_file)
#out_file.write(from_file)
#in_file = open(from_file, "r")



