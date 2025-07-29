my_dict = {'a': 3, 'b': 1, 'c': 2}
asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", asc)
desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", desc)


sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print(sample_dict)


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
combined = {**dic1, **dic2, **dic3}
print(combined)


n = 5
squares = {x: x*x for x in range(1, n+1)}
print(squares)


squares_15 = {x: x*x for x in range(1, 16)}
print(squares_15)


my_set = {1, 2, 3}
print(my_set)


for item in my_set:
    print(item)


my_set.add(4)
my_set.update([5, 6])  
print(my_set)


my_set.discard(2)  
my_set.remove(3)   
print(my_set)


item_to_remove = 5
if item_to_remove in my_set:
    my_set.remove(item_to_remove)
print(my_set)
