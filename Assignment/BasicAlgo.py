import random

l = [random.randint(1,1000) for _ in range(10)]

odd_numbers = 0

for i in l:
    if i&1:
        odd_numbers+=1

print(f"Number of odd number in {l} is: {odd_numbers}")