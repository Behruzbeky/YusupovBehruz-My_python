try:
    a = int(input("Enter a number: "))
    result = a / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")



try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Error: That was not a valid integer.")



try:
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found.")



try:
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    if not (x.replace('.', '', 1).isdigit() and y.replace('.', '', 1).isdigit()):
        raise TypeError("Inputs must be numbers.")
    result = float(x) + float(y)
    print("Sum:", result)
except TypeError as e:
    print("Error:", e)




try:
    with open("/root/secret.txt", "r") as f:  # use a restricted path
        data = f.read()
except PermissionError:
    print("Error: You do not have permission to open this file.")




try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Error: Index is out of range.")




try:
    num = input("Press Ctrl+C to interrupt or enter a number: ")
    print("You entered:", num)
except KeyboardInterrupt:
    print("\nInput cancelled by user.")



try:
    a = 10
    b = 0
    result = a / b
except ArithmeticError:
    print("Error: Arithmetic issue occurred (likely division by zero).")




try:
    with open("example.txt", "r", encoding="utf-8") as f:
        content = f.read()
except UnicodeDecodeError:
    print("Error: File encoding issue encountered.")



try:
    lst = [1, 2, 3]
    lst.upper()  # invalid: lists don't have `upper()` method
except AttributeError:
    print("Error: The object does not have that attribute.")



with open("file.txt", "r") as f:
    content = f.read()
    print(content)



n = 3
with open("file.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end='')



with open("file.txt", "a") as f:
    f.write("\nAppended line.")

with open("file.txt", "r") as f:
    print(f.read())



n = 3
with open("file.txt", "r") as f:
    lines = f.readlines()
    print(''.join(lines[-n:]))



with open("file.txt", "r") as f:
    lines = f.readlines()
print(lines)



with open("file.txt", "r") as f:
    content = ''
    for line in f:
        content += line
print(content)




with open("file.txt", "r") as f:
    array = [line.strip() for line in f]
print(array)



with open("file.txt", "r") as f:
    words = f.read().split()
    longest = max(words, key=len)
print("Longest word:", longest)



with open("file.txt", "r") as f:
    lines = f.readlines()
print("Number of lines:", len(lines))



from collections import Counter

with open("file.txt", "r") as f:
    words = f.read().replace(',', ' ').split()
    freq = Counter(words)
print(freq)



import os
size = os.path.getsize("file.txt")
print("File size:", size, "bytes")



items = ["apple", "banana", "cherry"]
with open("file.txt", "w") as f:
    for item in items:
        f.write(item + "\n")



with open("file.txt", "r") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())




with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())




import random

with open("file.txt", "r") as f:
    lines = f.readlines()
print(random.choice(lines).strip())



f = open("file.txt", "r")
print("Is closed?", f.closed)
f.close()
print("Is closed?", f.closed)



with open("file.txt", "r") as f:
    lines = [line.strip() for line in f]
print(lines)



with open("file.txt", "r") as f:
    text = f.read().replace(',', ' ')
    words = text.split()
print("Total words:", len(words))



import glob

char_list = []
for filename in glob.glob("*.txt"):
    with open(filename, "r") as f:
        char_list.extend(list(f.read()))
print(char_list)



import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}.txt")



import string

letters_per_line = 5
with open("alphabet.txt", "w") as f:
    alphabet = string.ascii_uppercase
    for i in range(0, len(alphabet), letters_per_line):
        f.write(' '.join(alphabet[i:i+letters_per_line]) + '\n')




