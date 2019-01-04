print("hello world")

animals = ["dog", "cat", "bear", "goat"]

for i in range(len(animals)):
    print(animals[i])

for animal in animals:
    print(animal)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = []
for num in numbers:
    squared.append(num ** 2)

squared = [num ** 2 for num in numbers]
