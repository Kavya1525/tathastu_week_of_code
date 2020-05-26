from itertools import permutations
str = input("Enter a string:")
print([''.join(i) for i in permutations(str)])
