#exercise 4

#this is assigning the value of 100 to car
cars = 100

#this is assigning the value of 4.0 to space_in_a_car, float point is used here but not necessary
space_in_a_car = 4.0

#this is assigning the value of 30 to drivers
drivers = 30

#this is assigning the value of 90 to passengers
passengers = 90

"""
this varible is calculating the amount of cars not driving by taking the value
assigned to car and - the value assigned to drivers
"""
cars_not_driven = cars -drivers

#this is a varible taking the value from the varible drivers
cars_driven = drivers

"""
this varible is calculating the carpool capacity by taking the value giving to cars drive
and * the space in the car
"""
carpool_capacity = cars_driven * space_in_a_car

"""
this varible is calculating the avarage average_passengers_per_car by taking the value giving to passengersand divding
the amount from cars_driven
"""
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


#Study Drill calculator

#assiging the value 20 to x
x = 20

#assiging the value 4 to y
y = 4

#print the modulos of 4 % 20
print y % x
