"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        mid_idx = int(len(numbers) / 2)
        print(
            (numbers[mid_idx] + numbers[mid_idx - 1]) / 2
            if len(numbers) % 2 == 0
            else numbers[mid_idx]
        )
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
