""" 
Elections are in progress!

Given an array of the numbers of votes given to each of the candidates so far, and 
an integer k equal to the number of voters who haven't cast their vote yet, find 
the number of candidates who still have a chance to win the election.

The winner of the election must secure strictly more votes than any other candidate. 
If two or more candidates receive the same (maximum) number of votes, assume there 
is no winner at all.

Example

For votes = [2, 3, 5, 2] and k = 3, the output should be
solution(votes, k) = 2.
"""

def electionWinners(votes, k):

    winner_vote = max(votes) 
    count = 0
    check = 0 

    for vote in votes:
        if vote + k > winner_vote:
            count += 1 
        if vote == winner_vote:
            count += 1 

    if check > 1 and k == 0:
        return 0   
    elif k == 0 and count > 0:
        return count + 1 
    elif k == 0 and winner_votes:
        return count + 1
    else:
        return count 

if __name__ == "__main__":
    votes = [2, 3, 5, 2] 
    k = 3
    print(electionWinners(votes, k))

