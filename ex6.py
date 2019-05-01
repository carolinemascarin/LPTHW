#Exercise 6

#assigning value 10 to %d
x = "There are %d types of people." % 10

#assiging value of string "binary" to binary
binary = "binary"

#assigngin value "dont" to do_not
do_not = "don't"

#assiging value "those.." and value binary and do_not to y
y = "Those who know %s and those who %s." % (binary, do_not)

#printing these values
print x
print y

#print
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
