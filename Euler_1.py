total = 0
upper_bound = int(input('Enter number: '))

for number in range(1, upper_bound):
    if number % 3 == 0 or number % 5 == 0:
        total += number
print ("The sum of all multiples of 3 or 5 below " + str(upper_bound) + ": " + str(total))
