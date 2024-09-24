import multiprocessing
import math

def is_prime(n):
    if n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i) == 0:
                return False
        return True
    else:
        return False

def check_prime_chunk(chunk):
  lst = []
  for n in chunk:
      if is_prime(n):
          lst.append(n)
  return lst

def find_primes_in_range(numbers):
  primes = []
  num_chunks = multiprocessing.cpu_count()
  num_chunks = 4
  chunks = [numbers[i * len(numbers) // num_chunks:(i + 1) * len(numbers) // num_chunks] for i in range(num_chunks)]
  with multiprocessing.Pool(processes=num_chunks) as pool:
        chunk_prime = pool.map(check_prime_chunk, chunks)
  for i in chunk_prime:
      primes.extend(i)
  return primes
