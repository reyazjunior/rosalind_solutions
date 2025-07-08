from collections import defaultdict

def count_word_occurrences(s):
    """
  Counts the occurrences of each word in a string.

  Args:
    s: The input string where words are separated by spaces.

  Returns:
    A dictionary where keys are words and values are their counts.
  """
    word_counts=defaultdict(int)
    words=s.split()
    for word in words:
        word_counts[word]+=1
    return word_counts

try:
    with open('python_village/rosalind_ini6.txt','r') as file:
        input_string=file.read().strip()
        counts = count_word_occurrences(input_string)
    with open('python_village/rosalind_ini6_output.txt','w') as file:
        for key, value in counts.items():
            file.write(f"{key} {value}\n")
    print(f"Dictionary written successfully.")
except IOError as e:
    print(f"Error writing to file: {e}")