def extract_and_combine_slices(s, a, b, c, d):
  """
  Extracts two slices from a string and combines them with a space.

  Args:
    s: The input string.
    a: The starting index of the first slice (inclusive).
    b: The ending index of the first slice (inclusive).
    c: The starting index of the second slice (inclusive).
    d: The ending index of the second slice (inclusive).

  Returns:
    A string consisting of the two slices combined with a space.
  """
  slice1 = s[a : b + 1]
  slice2 = s[c : d + 1]
  return f"{slice1} {slice2}"

# Read data from a file
try:
    with open('python_village/rosalind_ini3.txt', 'r') as file:
        lines = file.readlines()
        
        # The first line is the string
        s_from_file = lines[0].strip()
        
        # The second line contains the four integers
        nums_str = lines[1].strip().split()
        a_from_file = int(nums_str[0])
        b_from_file = int(nums_str[1])
        c_from_file = int(nums_str[2])
        d_from_file = int(nums_str[3])

    result = extract_and_combine_slices(s_from_file, a_from_file, b_from_file, c_from_file, d_from_file)
    print(result)

except FileNotFoundError:
    print("Error: 'rosalind_ini3.txt' not found. Please make sure the file exists.")
except IndexError:
    print("Error: 'rosalind_ini3.txt' does not contain enough lines or data in the expected format.")
except ValueError:
    print("Error: Could not parse integers from the input file. Please check the format.")