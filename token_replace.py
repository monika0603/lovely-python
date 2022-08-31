""" 
Write a function, token_replace, that takes in a dictionary of tokens and a string. The function 
should return a new string where tokens are replaced.

Tokens are enclosed in a pair of '$'. You can assume that the input string is properly formatted. 
Tokens should be replaced from left to right in the 
string (see test_05).
"""

def token_replace(s, tokens):

    for word, token in tokens.items():
        s = s.replace(word, token)

    return s 

if __name__ == "__main__":
    tokens = {
    '$LOCATION$': 'park',
    '$ANIMAL$': 'dog',
    }
    print(token_replace('Walk the $ANIMAL$ in the $LOCATION$!', tokens)) 
    # -> 'Walk the dog in the park!'

    # Test case 01
    tokens = {
    '$ADJECTIVE$': 'quick',
    '$VERB$': 'hopped',
    '$DIRECTION$': 'North'
    }
    print(token_replace('the $ADJECTIVE$ fox $VERB$ $ADJECTIVE$ly $DIRECTION$ward', tokens))
    # -> 'the quick fox hopped quickly Northward'

    # Test case 02
    tokens = {
    '$greeting$': 'hey programmer',
    }
    print(token_replace('his greeting is always $greeting$.', tokens)) 
    # -> 'his greeting is always hey programmer.'

    # Test case 03
    tokens = {
    '$A$': 'lions',
    '$B$': 'tigers',
    '$C$': 'bears',
    }
    print(token_replace('$A$$B$$C$, oh my.', tokens))
    # -> 'lionstigersbears, oh my.'

    # Test case 04
    tokens = {
    '$A$': 'lions',
    '$B$': 'tigers',
    '$C$': 'bears',
    }
    print(token_replace('$B$', tokens)) 
    # -> 'tigers'

    # Test case 05
    tokens = {
    '$second$': 'beta',
    '$first$': 'alpha',
    '$third$': 'gamma',
    }
    print(token_replace('$first$second$third$', tokens)) 
    # -> 'alphasecondgamma'