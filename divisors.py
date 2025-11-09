import sys

n = int(sys.argv[1])

result = []

for i in range(1, n + 1):
    if n % i == 0:
        result.append(str(i))

print(" ".join(result))
