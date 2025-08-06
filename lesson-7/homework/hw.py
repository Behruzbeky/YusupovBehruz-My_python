def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
print(is_prime(4))   # False
print(is_prime(7))   # True



def digit_sum(k):
    total = 0
    while k > 0:
        total += k % 10
        k //= 10
    return total
print(digit_sum(24)) 


def print_powers_of_two(N):
    power = 1
    while True:
        power *= 2
        if power > N:
            break
        print(power, end=' ')
print_powers_of_two(10)
