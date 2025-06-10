def sum_and_average(numbers):
    """Calculates the sum and average of a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        A tuple containing the sum and average of the numbers.
        Returns (0, 0) if the list is empty.
    """
    if not numbers:
        return 0, 0
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

# Example usage
numbers = [1, 2, 3, 4, 5]
total, average = sum_and_average(numbers)
print(f"Sum: {total}")
print(f"Average: {average}")

numbers = []
total, average = sum_and_average(numbers)
print(f"Sum: {total}")
print(f"Average: {average}")
