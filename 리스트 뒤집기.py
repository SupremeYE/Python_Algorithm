numbers = [2, 4, 6, 8, 10, 12, 14]
j = list(numbers)

for i in range(len(numbers)):
    numbers[i] = j[len(numbers) - i - 1]

print("뒤집어진 리스트: " + str(numbers))

print(len(numbers))

# numbers.reverse()
# print(numbers)