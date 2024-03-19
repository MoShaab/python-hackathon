def fibonacci(n):
    """
    This function generates the Fibonacci sequence up to a specified term n using iteration.

    Args:
        n: The number of terms in the Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence up to n terms.
    """
    if n<=1:
         return [0] if n == 1 else []  # Return [0] for n = 0
    elif n == 1:
        return [0]  # Return [0, 1] for n = 1
    else:
        a, b = 0, 1 
        fibonacci_sequence = [a, b] 
        for _ in range(2, n):
            c = a + b 
            fibonacci_sequence.append(c) 
            
            a, b = b, c
        return fibonacci_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the Fibonacci sequence
print(fibonacci_sequence)
