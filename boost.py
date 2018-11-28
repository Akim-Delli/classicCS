from collections import Counter


def electionsWinners(votes):
    # Function to find winner of an election where votes
    # are represented as candidate names

    # convert list of candidates into dictionary
    # output will be likes candidates = {'A':2, 'B':4}
    votes = Counter(votes)

    # create another dictionary and it's key will
    # be count of votes values will be name of
    # candidates
    dict = {}

    for value in votes.values():
        # initialize empty list to each key to
        # insert candidate names having same
        # number of votes
        dict[value] = []

    for (key, value) in votes.items():
        dict[value].append(key)

    # sort keys in descending order to get maximum
    # value of votes
    maxVote = sorted(dict.keys(), reverse=True)[0]

    # check if more than 1 candidates have same
    # number of votes. If yes, then sort the list
    # first and print first element
    if len(dict[maxVote]) > 1:

        return sorted(dict[maxVote])[0]
    else:

        return dict[maxVote][0]


if __name__ == "__main__":
    votes = ['Alex', 'Michael', 'Harry', 'Dave', 'Michael', 'Victor', 'Harry', 'Alex', 'Mary', 'Mary']
    print(electionsWinners(votes))