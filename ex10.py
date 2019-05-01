#Exercise 10

tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line"
backlash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t * Cat food
\t * Fishies
\t * Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat

#testing escape sequences

print "hello world"
print "hello\\world"
print "hello\'world"
print "hello\"world"
print "hello\aworld"
print "hello\bworld"
print "hello\fworld"
print "hello\rworld"
print "hello\nworld"
print "test\nwhy\rbecause\'"
print "caroline \'%s" % "is my name",
print "and my surname is \"%r" % "mascarin"

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i
