# numbers = []
# for _ in range(9):
#     x = int(input())
#     numbers.append(x)

numbers = [int(input()) for _ in range(9)]

max_val = max(numbers)
location = numbers.index(max_val) + 1

print(max_val)
print(location)