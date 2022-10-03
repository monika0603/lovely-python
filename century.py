""" 
Given a year, return the century it is in. The first century spans from the year 1 up to and including 
the year 100, the second - from the year 101 up to and including the year 200, etc.
"""

def solution(year):

    output = ''
    i = 0
    year = str(year) 
    if int(year[-1]) == 0 & int(year[-2]) == 0:
        output += year[0]
        output += year[1] 
        return int(output)
    

    if int(year) - (int(year)+1) != 0:
        for y in year:
            i += 1 
            output += y 
            if i == 2:
                break 
        return int(output)+1 
    
        

if __name__ == "__main__":
    print(solution(1905))

    # Test case 01
    print(solution(1700))