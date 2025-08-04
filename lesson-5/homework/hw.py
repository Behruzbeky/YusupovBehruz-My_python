year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")


n = int(input())

if n % 2 == 1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:  # n > 20 and even
    print("Not Weird")


def print_even_recursive(a, b):
    if a > b:
        return
    if a % 2 == 0:
        print(a)
    print_even_recursive(a + 1, b)

a=3
b=9
print_even_recursive(a, b)


a = 3
b = 12

print([x for x in range(a, b + 1) if x % 2 == 0])
