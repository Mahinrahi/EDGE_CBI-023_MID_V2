def sum_digits(b):
    if b == 0:
        return 0
    else:
        return b % 10 + sum_digits(b // 10)

n = int(input("Enter a number: "))
print("Sum of digits:", sum_digits(n))