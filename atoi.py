
def atoi(s):

    a = set('0123456789-')
    if s in a:
        return s 

    
if __name__ == "__main__":
    s = "   -42"
    print(atoi(s))