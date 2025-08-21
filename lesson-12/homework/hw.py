import threading

# Function to check if a number is prime
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Worker function for each thread
def prime_checker(start: int, end: int, primes: list):
    local_primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            local_primes.append(num)
    primes.extend(local_primes)  # Add results to shared list

def threaded_prime_checker(start: int, end: int, num_threads: int):
    # Shared list for storing primes (thread-safe with proper usage)
    primes = []
    threads = []
    step = (end - start + 1) // num_threads

    for i in range(num_threads):
        sub_start = start + i * step
        # Last thread takes the remaining numbers
        sub_end = (start + (i + 1) * step - 1) if i != num_threads - 1 else end

        thread = threading.Thread(target=prime_checker, args=(sub_start, sub_end, primes))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return sorted(primes)


if __name__ == "__main__":
    start = 1
    end = 100
    num_threads = 4

    primes = threaded_prime_checker(start, end, num_threads)
    print(f"Prime numbers between {start} and {end}:")
    print(primes)






import threading
from collections import Counter

# Worker function for each thread
def count_words_in_lines(lines, counter_list, index):
    word_count = Counter()
    for line in lines:
        words = line.strip().split()
        word_count.update(words)
    counter_list[index] = word_count  # Store local result in shared list


def threaded_word_count(filename, num_threads=4):
    # Read all lines from the file
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // num_threads

    threads = []
    counter_list = [None] * num_threads  # Placeholder for each thread's results

    # Divide work among threads
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else total_lines
        thread = threading.Thread(
            target=count_words_in_lines,
            args=(lines[start:end], counter_list, i)
        )
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Merge results
    total_count = Counter()
    for c in counter_list:
        total_count.update(c)

    return total_count


if __name__ == "__main__":
    filename = "large_text.txt"  # Replace with your file path
    num_threads = 4

    word_counts = threaded_word_count(filename, num_threads)

    print("Word Occurrences:")
    for word, count in word_counts.most_common(20):  # Top 20 words
        print(f"{word}: {count}")

