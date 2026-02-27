# Model Answer for Python Control Structures Assignment

# Task 1: Number Classifier
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Task 2: Sum of Even Numbers
sum_even = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i
print("Sum of even numbers from 1 to 100:", sum_even)

# Task 3: List Search with While Loop
numbers = [5, 12, 42, 7, 19, 42, 8]
target = 42
index = 0
found = False
while index < len(numbers):
    if numbers[index] == target:
        print(f"Found {target} at index {index}")
        found = True
        break
    index += 1
if not found:
    print(f"{target} not found in the list.")
