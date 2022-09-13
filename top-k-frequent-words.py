""" 
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their 
lexicographical order.

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
"""

def topKFrequent(words, k):

    word_count = {}
    for word in words:
        word_count[word] = 1 + word_count.get(word, 0) 

    sorted_dict = {key:value for key, value in sorted(word_count.items(), key=lambda x: (-x[1], x[0]))}

    output = [] 
    for key, value in sorted_dict.items():
        output.append(key)
        k -= 1 
        if k == 0: break 

    return output 


if __name__ == "__main__":
    words = ["i","love","leetcode","i","love","coding"]
    k = 2
    print(topKFrequent(words, k))

    # Test case 01
    words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
    k = 4 
    print(topKFrequent(words, k))