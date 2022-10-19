""" 
An email address such as "John.Smith@example.com" is made up of a local part 
("John.Smith"), an "@" symbol, then a domain part ("example.com").

The domain name part of an email address may only consist of letters, digits, 
hyphens and dots. The local part, however, also allows a lot of different 
special characters. Here you can look at several examples of correct and 
incorrect email addresses.

Given a valid email address, find its domain part.

Example

For address = "prettyandsimple@example.com", the output should be
solution(address) = "example.com";
For address = "fully-qualified-domain@codesignal.com", the output should 
be
solution(address) = "codesignal.com".
"""

def findEmailDomain(address):

    count = {}
    for char in address:
        if char == '@':
            count[char] = 1 + count.get(char, 0)

    illegal = '\"(),:;<>[ '

    if address.find('@') == -1:
        return 'Not found'
    if count['@'] > 1:
        return 'Not allowed'

    for char in address:
        if char in illegal:
            return 'Not allowed'
    
    else:
        output = address.split('@')
        if output[1].find('_') != -1:
            return 'Not allowed'
        if len(output[0] > 64):
            return 'Not allowed'
        return output[1] 

    

if __name__ == "__main__":
    address = "prettyandsimple@example.com"
    print(findEmailDomain(address)) 

    # Test case 01
    address = "Abc.example.com"
    print(findEmailDomain(address)) 

    # Test case 02
    address = "Abc@example@com"
    print(findEmailDomain(address)) 

    # Test case 03
    address = "a\"b(c)d,e:f;g<h>i[j\k]l@example.com"
    print(findEmailDomain(address)) 

    # Test case 04
    address = "just\"not\"right@example.com"
    print(findEmailDomain(address)) 

    # Test case 05
    address = "this isnot\allowed@example.com"
    print(findEmailDomain(address)) 

    # Test case 06
    address = "i_like_underscore@but_its_not_allowed_in_this_part.example.com"
    print(findEmailDomain(address)) 

    # Test case 06
    address = "1234567890123456789012345678901234567890123456789012345678901234+x@example.com"
    print(findEmailDomain(address)) 

    

