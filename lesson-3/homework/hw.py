fruits = ["apple", "banana", "cherry", "orange", "grape"]
print("1. Third fruit:", fruits[2])


list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("2. Concatenated list:", combined_list)


numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
new_list = [first, middle, last]
print("3. Extracted elements:", new_list)


favorite_movies = ["Inception", "Matrix", "Interstellar", "Titanic", "Avengers"]
movie_tuple = tuple(favorite_movies)
print("4. Tuple of movies:", movie_tuple)


cities = ["London", "New York", "Paris", "Tokyo"]
is_paris_in_list = "Paris" in cities
print("5. Is Paris in list?", is_paris_in_list)


original_list = [1, 2, 3]
duplicated_list = original_list * 2
print("6. Duplicated list:", duplicated_list)


swap_list = [10, 20, 30, 40, 50]
swap_list[0], swap_list[-1] = swap_list[-1], swap_list[0]
print("7. Swapped list:", swap_list)


numbers_tuple = tuple(range(1, 11))  
sliced = numbers_tuple[3:8]  
print("8. Sliced tuple (index 3-7):", sliced)


colors = ["blue", "red", "blue", "green", "blue"]
blue_count = colors.count("blue")
print("9. Count of 'blue':", blue_count)


animals = ("cat", "dog", "lion", "tiger")
lion_index = animals.index("lion")
print("10. Index of 'lion':", lion_index)


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print("11. Merged tuple:", merged_tuple)


sample_list = [1, 2, 3, 4]
sample_tuple = (10, 20, 30)
print("12. Length of list:", len(sample_list))
print("   Length of tuple:", len(sample_tuple))


num_tuple = (5, 10, 15, 20, 25)
converted_list = list(num_tuple)
print("13. Converted list:", converted_list)


num_tuple2 = (10, 3, 25, 1, 7)
print("14. Max:", max(num_tuple2))
print("   Min:", min(num_tuple2))


words = ("hello", "world", "python", "tuple")
reversed_tuple = words[::-1]
print("15. Reversed tuple:", reversed_tuple)
