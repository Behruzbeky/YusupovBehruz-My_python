def insert_shifted_underscores(txt):
    vowels = 'aeiouAEIOU'
    i = 3
    while i < len(txt):
        while i < len(txt) and (txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] == '_')):
            i += 1
        if i < len(txt):
            txt = txt[:i] + '_' + txt[i:]
            i += 4
    return txt.rstrip('_')
print(insert_shifted_underscores("hello"))             
print(insert_shifted_underscores("assalom"))           
print(insert_shifted_underscores("abcabcabcdeabcdefabcdefg"))  


n = int(input())

for i in range(n):
    print(i** 2)


i = 1
while i <= 10:
    print(i)
    i += 1


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()



num = int(input("Enter number: "))
total = 0
for i in range(1, num + 1):
    total += i
print("Sum is:", total)



num = int(input("Enter number: "))
for i in range(1, 11):
    print(num * i)



numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num > 100 and num % 5 == 0:
        print(num)



num = int(input("Enter number: "))
count = 0
while num != 0:
    num //= 10
    count += 1
print("Total digits:", count)


for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()


list1 = [10, 20, 30, 40, 50]
for i in range(len(list1) - 1, -1, -1):
    print(list1[i])


for i in range(-10, 0):
    print(i)



for i in range(5):
    print(i)
else:
    print("Done!")



start = 25
end = 50
print("Prime numbers between", start, "and", end, ":")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)



n = 10
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b



num = int(input("Enter number: "))
factorial = 1
for i in range(2, num + 1):
    factorial *= i
print(f"{num}! = {factorial}")



from collections import Counter

def uncommon_elements(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)
    
    result = []

    # Elements in list1 but not in list2
    for elem in count1:
        if elem not in count2:
            result.extend([elem] * count1[elem])
        else:
            diff = count1[elem] - count2[elem]
            if diff > 0:
                result.extend([elem] * diff)
    
    # Elements in list2 but not in list1
    for elem in count2:
        if elem not in count1:
            result.extend([elem] * count2[elem])
        else:
            diff = count2[elem] - count1[elem]
            if diff > 0:
                result.extend([elem] * diff)

    return result


print(uncommon_elements([1, 1, 2], [2, 3, 4]))     
# Output: [1, 1, 3, 4]

print(uncommon_elements([1, 2, 3], [4, 5, 6]))     
# Output: [1, 2, 3, 4, 5, 6]

print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  
# Output: [1, 2, 2, 5]
