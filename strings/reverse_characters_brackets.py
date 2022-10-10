""" 
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
"""

def reverse_characters(s):

    stack = [] 

    for char in s:
        if char == ')':
            segment = ''
            while not stack[-1] == '(':
                popped = stack.pop() 
                segment += popped 
            stack.pop() # Remove the closing bracket
            for i in segment:
                stack.append(i)
        else:
            stack.append(char) 

    stack = "".join(stack)
    return  stack 



if __name__ == "__main__":
    s = '(bar)'
    print(reverse_characters(s)) # rab

    # Test case 01
    s = "foo(bar)baz"
    print(reverse_characters(s)) # foorabbaz

    # Test case 02
    s = "foo(bar(baz))blim" 
    print(reverse_characters(s)) # foobazrabblim"