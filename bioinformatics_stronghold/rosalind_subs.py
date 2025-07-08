def motif(s,t):
    """
    Finds all starting indices of substring 't' within string 's'.

    This version uses a more concise approach by iterating through possible
    start indices and checking if the substring matches.

    Args:
        s (str): The main string to search within.
        t (str): The substring to search for.

    Returns:
        list: A list of integers, where each integer is the starting index
              of an occurrence of 't' in 's'. Returns an empty list if 't'
              is not found or if 't' is an empty string.
    """
    if not t: # If t is an empty string, return empty list
        return []

    # Use a list comprehension to build the list of indices
    # We iterate from 0 up to (len(s) - len(t)) inclusive.
    # For each 'i', we check if the slice s[i:i+len(t)] is equal to t.
    locations = [i+1 for i in range(len(s) - len(t) + 1) if s[i:i+len(t)] == t]
    return locations

try:
    with open('bioinformatics_stronghold/rosalind_subs.txt', 'r') as file:
        lines = file.read().strip().splitlines()
        if len(lines) < 2:
            raise ValueError("File must contain exactly two lines with DNA strings.")
        s, t = lines[0].strip(), lines[1].strip()
        result = motif(s, t)
        print(*result)
except FileNotFoundError:
    print("Error: File not found. Please make sure the file exists.")
except IndexError:
    print("Error: File does not contain enough lines or data in the expected format.")
except ValueError:
    print("Error: Could not parse data from the input file. Please check the format.")