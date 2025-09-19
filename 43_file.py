import prime_number as p

def is_perfect(n):
    if n < 2:
        return False
    return sum([i for i in range(1, n) if n % i == 0]) == n

read_file = "numbers.txt"
prime_file = "prime.txt"
perfect_file = "perfect.txt"

try:
    with open(read_file, 'r') as numbers, \
        open(prime_file, 'w') as prime_writer, \
        open(perfect_file, 'w') as perfect_writer:

        for line in numbers:
            try:
                num = int(line.strip())

                # Check and write prime numbers
                if p.isPrime(num):
                    prime_writer.write(str(num) + "\n")

                # Check and write perfect numbers
                if is_perfect(num):
                    perfect_writer.write(str(num) + "\n")

            except ValueError:
                print(f"Skipping invalid line (not a number): {line.strip()}")

except FileNotFoundError:
    print(f"Error: File {read_file} not found.")
except IOError as e:
    print(f"I/O error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Task complete.")
