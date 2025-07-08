def extract_even_numbered_lines(input_filepath, output_filepath):
  """
  Reads an input file and writes all even-numbered lines to an output file.

  Args:
    input_filepath: The path to the input text file.
    output_filepath: The path to the output text file where even-numbered lines will be written.
  """
  try:
    with open(input_filepath, 'r') as infile:
      with open(output_filepath, 'w') as outfile:
        line_number = 0
        for line in infile:
          line_number += 1
          if line_number % 2 == 0:  # Check if the line number is even
            outfile.write(line)
    print(f"Even-numbered lines successfully written to '{output_filepath}'")
  except FileNotFoundError:
    print(f"Error: The input file '{input_filepath}' was not found.")
  except IOError as e:
    print(f"Error: An I/O error occurred while processing files: {e}")

input_file = 'python_village/rosalind_ini5.txt'
output_file = 'python_village/rosalind_ini5_output.txt'
extract_even_numbered_lines(input_file, output_file)