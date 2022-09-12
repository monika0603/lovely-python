""" 
# Implement a word count engine. Given a string of words, sort words by count in descending order. If two words have same count 
# then they should be displayed in the lexicographical order. Note that non-alphabetical chars can be discarded for this question.
# Eg: "Testing is always important. unit test, regression test, acceptance test. Always test!"
# Out: [test, 4], [always, 2], [acceptance, 1], [important, 1], [is, 1], [regression, 1], [testing, 1], [unit, 1]

Algorithm:

A. First ask clarifying questions. 
1. Can I get other non-alphabetical words, other than the ones shown in this example?
2. Do I have to take case into account? 
3. Explain lexical ordering concept to the interviewer and confirm if that is correct. 
4. Before proceeding to implementing the code,  
"""

import re 
def word_count(s):

    input_list = clean_input_string(s) 

    word_dict = create_word_dict(input_list) 

    # sorts dictionary by values in the descending order 
    #sorted_dict = {key: value for key, value in sorted(word_dict.items(), key=lambda item: -item[1])}
    sorted_dict = {key: value for key, value in sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))}
    
    return sorted_dict

def create_word_dict(input_list):
    count_word = {} 
    for word in input_list:
        count_word[word] = 1 + count_word.get(word, 0)

    return count_word 


def clean_input_string(s):
    str = re.sub('[^a-zA-Z0-9]+', ' ', s) 
    str = str.lower() 
    input_list = str.split() 

    return input_list 


if __name__ == "__main__":
    s = "Testing is always important. unit test, regression test, acceptance test. Always test!"
    print(word_count(s))