#Exercise 11

#raw_input read a line from input and returns a string by stripping a trailing new line

#it basically prints a blank space in the terminal which allow you to enter data

#Test 1 from book
print "How old are you?"
age = raw_input()

print "How tall are you in cm?"
height = raw_input()

print "How much do you weigh in stone?"
weight = raw_input()

print "So, you're %r years old, %r cm tall, and weight %r stone" % (age, height, weight)


#Test 2 mine

print "do you like apples or bananas"
answer = raw_input()

print "cool, %s is also my favourite fruit" % answer

#test 3 mine

#assigned the list value of sad and happy to emotions

emotions = ["Sad", "Happy"]

#  telling emotions string to join emotions, using .join with the emotions variables to get them together, 
emotions_string = " ".join(emotions)

# assinging a raw_input (which allow you to enter date) to the variable feelings
# this will print "how are you feeling today", the \n is used to add a new line, the {} is used to return string, the .format is used to collect the data from emotions_strings
feelings = raw_input("How are you feeling today?\n{}?".format(emotions_string))
    
#if statements allows you to perform actions based on if the statement is true / not true
#in this case it is saying "if feelings is not happy" print "hope you will feel better" and if they type Sad or other it will return "glad that you are ok"
if feelings != "Happy":
    print "hope you will feel better"
else:
    print "glad that you are ok, have a nice evening"
