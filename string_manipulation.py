""" 
Various string manipulations
"""

def convert(s):

    output = s.split() 
    return output 

def convert_1(s):
    output = list(s)
    return output 

import re 
def use_findall(s): 
    output = re.findall('[a-zA-Z]', s)
    return output 

import ast 
def using_ast(input_list):
    result = ast.literal_eval(input_list)
    return result 

if __name__ == "__main__":
    s = "Geeks for geeks"
    print(convert(s))

    # Test case 01
    s = 'ABCD'
    print(convert_1(s))

    # Test case 02
    s = 'ABCD123'
    print(use_findall(s))

    # Test case 03 
    s = "Testing is always important. unit test, regression test, acceptance test. Always test!"
    print(use_findall(s))

    # Test case 04 
    input_list = '["geeks", 2,"for", 4, "geeks",3]'
    print(using_ast(input_list))