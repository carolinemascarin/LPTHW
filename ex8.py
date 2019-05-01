#Exercise 8


#%r will give you the raw text and it would be used only for debugging
#formatter variable is assigned with "%r"
formatter = "%r %r %r %r"

#formatter variable is assigned with "%s"
othertest = "%s %s %s %s"

#this will print 1,2,3,4
print formatter % (1,2,3,4)

#this will print one, two, three, four
print formatter % ("one", "two", "three", "four")

#this will print %r 4 times

print formatter % (True, False, True, False)

print formatter % (formatter, formatter, formatter, formatter)

#this will print the text below, the \n can be used to create a new line
print othertest % ("I had this thing.\n","That you could type up right.",
"But it didn't sing.","so I said goodnight.")
