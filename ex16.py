#Reading and writing files
#Exercise 16

#from sys is a package, and import is saying to get the argv feature from that package
from sys import argv

#this is unpackaing argv so rather than holding all the arguments it gets assigned to variables for you to work with
script, filename = argv

#printing "we are going to erase" + filename (whatever file name you enter)
print "We are going to erase %r." %filename

#printing "if you don't want that, hit ctrl-c(^C)."
print "If you don't want that, hit CTRL-C (^C)."

#printing "if you do want that, hit return"
print "if you do want that, hit return"

#asking for users input, and printing "?"
raw_input("?")

#printing "opening the file"
print "opening the file..."

#target variable is assigned with method open, argument to open "filename", argument  "w" to write in file
target = open(filename, "w")

#printing trucating the file
print "truncating the file. Goodbye!"

#attaching function truncate to target, it empties filename 
target.truncate()

#printing "Now I am going to ask you for three lines"
print "Now I am going to ask you for three lines."

#line1 asking fo user input, and printing "line1:"
line1 = raw_input("line 1: ")
#line2 asking for user input, and printing "line2:"
line2 = raw_input("line 2: ")
#line3 asking for user input, and printing "line3:"
line3 = raw_input("line 3: ")

#printing  "now i am going to write these to the file"
print "Now I am going to write these to the file."

#writing into the file, simplified code below
target.write(line1 + "\n" + line2 + "\n" + line3)


#writing users input into file
#target.write(line1)
#target.write("\n") 
#target.write(line2)
#target.write("\n") 
#target.write(line3)
#target.write("\n") 

#target.write("%r, %r, %r") % (line1, line2, line3) wrong ! delete

#printing "and finally we close it"
print "and finally we close it"


#closing the file
target.close
