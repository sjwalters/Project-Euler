# Problem #1:  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# My solution allows a user to input an integer
# then calculates the sum of the multiples of 3 or 5 below that user input

total = 0
upper_bound = int(input('Enter number: '))

for number in range(1, upper_bound):
    if number % 3 == 0 or number % 5 == 0:
        total += number
print ("The sum of all multiples of 3 or 5 below " + str(upper_bound) + ": " + str(total))
