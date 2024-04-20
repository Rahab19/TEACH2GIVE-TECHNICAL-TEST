# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for
# multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print
# "FizzBuzz".

def fizz_Buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'

    return input


print(fizz_Buzz(25))
