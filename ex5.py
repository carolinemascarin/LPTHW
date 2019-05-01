#Exercise 5

myname = 'Caroline Mascarin'
myage = 27
myheight = 175
myeyes = 'Black'
myteeth = 'White'
myhair = 'Brown'

print "Lets talk about %s." % myname
print "She is %d centimeters tall" %myheight
print "She's got %s eyes and %s hair" % (myeyes, myhair)
print "if I add %d and %d I get %d" % (myage, myheight, myage + myheight)
print "my name is %s" % myname
print "my name is %r" % myname
print "my age is %o" % myage


""" 4. Try to write some variables that convert the inches and pounds to centimeters and kilos.
Do not just type in the measurements. Work out the math in Python. """

#converting km to pounds
x = 20 #kg
y = 2.2 # pounds
print x * y

#converting cm to inch

x = 175 #cm
y = 2.54 #inch

print x / y
