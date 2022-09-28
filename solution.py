def solution(numbers, left, right):
    
    output = []
    for i in range(len(numbers)):
        
        x = numbers[i]/(i+1)
        if x <= right and x >= left and x.is_integer():
            output.append(True)
        else:
            output.append(False)
            
    return output 

import operator 
def often_number(a):

    result = {}

    input_digits = []
    for i in range(len(a)):
        for j in str(a[i]):
            input_digits.append(j) 

            result[j] = 1 + result.get(j, 0) 

    sorted_dict = {key: value for key, value in sorted(result.items(), key=lambda x: -x[1])}
    max_value = max(sorted_dict.values())

    value = [i for i in result if result[i]==max_value]
    return sorted(value)
        

def string_solution(arr):

    min_length = float("inf")
    for word in arr:
        length = len(word)
        min_length = min(min_length, length) 
    
    output = []
    for i in range(min_length):
        output_1 = [x[i] for x in arr]
        output.append("".join(output_1))
    
    output_2 = []
    for word in arr:
        if len(word) > min_length:
            output_2.append(word[4])

    return "".join(output)

def string_solution1(s1, s2):

    if not s1 or not s2:
        return -1 

    if s2 in s1:
        return s1.index(s2) 

    else:
        return -1 
    
    

def fetch_letters(arr):

    word_length = set()
    for word in arr:
        word_length.add(len(word))

    word_length = sorted(word_length)

    output = []
    for length in word_length:
        i = 0 
        while i < length:
            for x in arr:
                if len(x) == length:
                    print(x, length, i)
                    output.append(x[i])
            i += 1 
    output.append("".join(output)) 

    return output 

    
if __name__ == "__main__":
    numbers = [8, 5, 6, 16, 5]
    left = 1
    right = 3 
    print(solution(numbers, left, right))


    a = [25, 2, 3, 57, 38, 41]
    print(often_number(a))

    arr = ["Daisy", "Rose", "Hyacinth", "Poppy"]
    print(fetch_letters(arr))

    # Test case 
    s1 = "sadbutsad"
    s2 = "sad"
    print(string_solution1(s1, s2))

    # Test case 
    s1 = "leetcode"
    s2 = "leeto"
    print(string_solution1(s1, s2))