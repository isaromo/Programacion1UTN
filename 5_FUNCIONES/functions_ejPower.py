def sum_digits(n):
    add = 0
    while n>0:
        digit = n%10
        add +=digit
        n //=10 
    return add