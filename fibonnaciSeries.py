# Example 1

def fibonnaci(n):
  a, b = 0, 1
  while a <= n:
    print(a, end=" ")
    a, b = b, a + b

# This function prints all Fibonacci numbers up to n.
# I start with two variables a and b initialized to 0 and 1.
# In each iteration, I print a, then update a and b such that a becomes the current b, and b becomes the sum of the previous a & b.
# The loop continues until a exceeds n. This approach uses constant space and linear time O(n)

# Return Fibonacci Sequence as a List
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence
