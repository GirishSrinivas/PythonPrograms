#Author: Girish Srinivas
#Date: February 8, 2016

#program to illustrate usage of 'variables'...
#various variable's are declred and initialized....
#here all the variables are dynamically typed to the datatype at runtime based on the declared data...
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
variable = 0
_variable123 = 9

print "the content of '_variable123' is: ", _variable123
print "The content of variable is: ", variable
variable = 'a'
print "the content of variable is: ", variable
variable = "Girish"
print "the value of variable is: ", variable
print "There are ", cars, "cars availlable."
print "There are only ", drivers, "drivers availlable"
print "There will be ", cars_not_driven, "empty cars today"
print "We can transport ", carpool_capacity, "people today"
print "We have ", passengers, "to carpool today"
print "We need to put about ", average_passengers_per_car, "in each car."