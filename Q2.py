# Write a program to generate the Fibonacci sequence up to 100.
def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)

    else:
        print(a)
        print(b)

        for i in range(2,100):

            c = a + b
            a = b
            b = c
            if c > 100:
                break
            print(c)
fib(100)