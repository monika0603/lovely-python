""" 
Python program to convert a list to string

Input: ['Geeks', 'for', 'Geeks']
Output: Geeks for Geeks

Input: ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
Output: I want 4 apples and 18 bananas
"""
def list_to_string(input):
    # Only works if all the words in the list are string. 
    # Fails if any part is an integer
    str = ''
    for word in input:
        str += word 

    return str 

def list_string(input):

    output = "".join([str(word) for word in input])
    return output

if __name__ == "__main__":
    input = ['Geeks', 'for', 'Geeks']
    print(list_to_string(input))

    # Test case 01
    input = ['I', 'want', 4, 'apples', 'and', 18, 'bananas'] 
    print(list_string(input))