
def anagram(s1, s2):
    if len(s1) != len(s2):
        return False 

    count_s1 = {}
    count_s2 = {} 
    for i in range(len(s1)):
        count_s1[s1[i]] = 1 + count_s1.get(s1[i], 0)
        count_s2[s2[i]] = 1 + count_s2.get(s2[i], 0)

    for c in count_s1:
        if count_s1[c] != count_s2.get(c, 0):
            return False 

    return True 



if __name__ == "__main__":
    s1 = 'restful'
    s2 = 'fluster'

    print(anagram(s1, s2))

    # Test case 02
    # Test case 02
    s1 = 'cats'
    s2 = 'tocs'
    print(anagram(s1, s2)) 