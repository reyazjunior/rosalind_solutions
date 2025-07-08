def sum_of_odd_integers(a,b):
    '''
    Given: Two positive integers a and b
    Return: The sum of all odd integers from a through b
    '''
    sum=0
    for i in range(a,b+1):
        if i%2!=0:
            sum+=i
    return sum

try:
    with open('python_village/rosalind_ini4.txt', 'r') as file:
        line = file.readline().strip()
        a_str, b_str = line.split()
        a_from_file = int(a_str)
        b_from_file = int(b_str)
        file_result = sum_of_odd_integers(a_from_file, b_from_file)
        print(f"Result from file: {file_result}")
except FileNotFoundError:
    print("Error: 'rosalind_ini4' not found. Please create the file with the leg lengths.")
except ValueError:
    print("Error: Invalid data in 'rosalind_ini4'. Please ensure it contains two integers separated by a space.")