#exercise 15

#from sys is a package, and import is saying to get the argv feature from that package
from sys import argv

#this is unpackaing argv so rather than holding all the arguments it gets  assigned to variables for you to work with
script, filename = argv

#ousing comand opening to open file filename 
txt = open(filename)
#printing filename, just the file 'name' rather than it's content
print "Here is your file %r" %filename
#printing the content of a file 
#print txt.read(3)
print(txt.readline())
print(txt.readlines())
#print(txt.readline(8))
txt.close()


#printing the text on screen 
print "Type the filename again:"
#prompting the user to type file name again
file_again = raw_input("> ")

#opening the file again
txt_again = open(file_again)

#reading the file again
print txt_again.read()

txt_again.close()