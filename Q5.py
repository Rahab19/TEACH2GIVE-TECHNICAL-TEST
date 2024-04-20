# Write a program that takes an integer as input and returns an integer with reversed digit ordering.
num = int(input("Enter the number :- "))
reverse_num = 0


def reverse_fuc(num):
    global reverse_num
    while num > 0:
        r = num % 10
        reverse_num = (reverse_num * 10) + r
        num = num // 10


reverse_fuc(num)
print("Reverse of enter number is =", reverse_num)
