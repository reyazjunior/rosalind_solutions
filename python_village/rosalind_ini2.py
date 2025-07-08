def calculate_hypotenuse_squared(a, b):
  """
  Calculates the square of the hypotenuse of a right triangle.

  Args:
    a: The length of the first leg.
    b: The length of the second leg.

  Returns:
    The integer corresponding to the square of the hypotenuse.
  """
  return a**2 + b**2

# Example usage with the given values:
a_val = 844
b_val = 979
result = calculate_hypotenuse_squared(a_val, b_val)
print(result)

# To read from a file named 'input.txt' (assuming it contains "844 979"):
try:
    with open('python_village/rosalind_ini2.txt', 'r') as file:
        line = file.readline().strip()
        a_str, b_str = line.split()
        a_from_file = int(a_str)
        b_from_file = int(b_str)
        file_result = calculate_hypotenuse_squared(a_from_file, b_from_file)
        print(f"Result from file: {file_result}")
except FileNotFoundError:
    print("Error: 'rosalind_ini2.txt' not found. Please create the file with the leg lengths.")
except ValueError:
    print("Error: Invalid data in 'rosalind_ini2'. Please ensure it contains two integers separated by a space.")