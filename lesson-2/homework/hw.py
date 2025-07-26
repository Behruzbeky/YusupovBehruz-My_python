name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
age = 2025 - birth_year
print(f"{name}, you are {age} years old.")


txt = 'LMaasleitbtui'
car1 = txt[1] + txt[3] + txt[5] + txt[7] + txt[9]+ txt[11]
car2= txt[0] + txt[2] + txt[4] + txt[6] + txt[8]+ txt[12]
print("Extracted car:", car1)
print("Extracted car:", car2)


txt = 'MsaatmiazD'
car1 = txt[0] + txt[2] + txt[8] + txt[9] + txt[3]
car2 = txt[5] + txt[7] + txt[4] + txt[6] + txt[8]
print("Extracted car:", car1)
print("Extracted car:", car2)


txt = "I'm John. I am from London"
words = txt.split()
if "from" in words:
    index = words.index("from")
    print("Residence area:", words[index + 1])


user_input = input("Enter a string: ")
reversed_str = user_input[::-1]
print("Reversed string:", reversed_str)


text = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)


nums = input("Enter numbers separated by spaces: ")
num_list = list(map(int, nums.split()))
print("Maximum value:", max(num_list))


word = input("Enter a word: ")
if word == word[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")


email = input("Enter your email address: ")
domain = email.split('@')[-1]
print("Email domain:", domain)


import random
import string
length = 12
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated password:", password)
