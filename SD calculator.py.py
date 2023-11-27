import math

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_variance(numbers, mean):
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(variance):
    return math.sqrt(variance)

def main():
    # Get input from the user
    data = input("Enter a list of numbers separated by spaces: ")
    
    # Convert input to a list of floats
    numbers = [float(x) for x in data.split()]

    # Calculate mean, variance, and standard deviation
    mean_value = calculate_mean(numbers)
    variance_value = calculate_variance(numbers, mean_value)
    standard_deviation_value = calculate_standard_deviation(variance_value)

    # Display the results
    print(f"Mean: {mean_value}")
    print(f"Variance: {variance_value}")
    print(f"Standard Deviation: {standard_deviation_value}")

if __name__ == "__main__":
    main()
