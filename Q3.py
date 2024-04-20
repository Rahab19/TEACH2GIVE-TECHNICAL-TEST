# Write a program that takes an integer as input and returns true if the input is a power of two.
def is_power_of_two(number):
    if number <= 0:
        return False
    return number & (number - 1) == 0


number = int(input("Enter an integer: "))

if is_power_of_two(number):
    print(f"{number} true.")
else:
    print(f"{number} false.")
