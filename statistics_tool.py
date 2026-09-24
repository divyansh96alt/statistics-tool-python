import statistics


def main():
    print("=== Python Statistics Tool ===")

    user_input = input("Enter numbers separated by spaces: ")

    try:
        numbers = [float(x) for x in user_input.split()]
    except ValueError:
        print("Please enter numbers only.")
        return

    if not numbers:
        print("Please enter at least one number.")
        return

    print("\n--- Results ---")
    print(f"Count: {len(numbers)}")
    print(f"Mean: {statistics.mean(numbers):.2f}")
    print(f"Median: {statistics.median(numbers):.2f}")
    print(f"Minimum: {min(numbers):.2f}")
    print(f"Maximum: {max(numbers):.2f}")
    print(f"Range: {max(numbers) - min(numbers):.2f}")

    if len(numbers) >= 2:
        print(f"Sample Variance: {statistics.variance(numbers):.2f}")
        print(f"Sample Standard Deviation: {statistics.stdev(numbers):.2f}")

    try:
        print(f"Mode: {statistics.mode(numbers):.2f}")
    except statistics.StatisticsError:
        print("Mode: No unique mode")


if __name__ == "__main__":
    main()