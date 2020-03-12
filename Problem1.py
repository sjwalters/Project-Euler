"""If we list all the natural numbers below 10 that 
are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum 
of these multiples is 23. Find the sum of all the 
multiples of 3 or 5 below 1000."""

#This function will sum all the mutiples of 3 or 5 that are less than 1000
def sum_multiples_of_three_or_five():
    #This variable keeps track of the sum and is intially set to zero
    sum = 0
    #loops through all natural numbers from 0 to 999
    for i in range(1000):
        #checks each number to see if it is divisible by 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            #if it is, adds it to the sum variable
            sum += i
    return sum

#prints the sum that is returned by the function
print(sum_multiples_of_three_or_five())   


