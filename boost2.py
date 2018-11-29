import string
import pprint


def rollTheStringOld(s, roll):
    """
    Function to rotate by one character a consecutive number of characters of a string
    based on a sequence a character number
    eg : inputs :"abc" and [ 3, 2, 1] : "abc" -> "bcd" -> "cdd" -> "ddd"
       : output : "ddd"

    :param s: str
    :param roll: List[int]
    :return: word transformed: str
    """

    # convert alphabet into a List [a, b, c, ..., z]
    alphabet = list(string.ascii_lowercase)
    # rotate to the left the alphabet List: [b, c, ...., z, a]
    alphabet_shifted = alphabet[1:] + alphabet[:1]

    # Dictionary where keys are alphabet letters and values are their corresponding next letter in the alphabet
    # next_charater = {"a": "b", "b": "c", ... , "z": "a"}
    next_character = {character_pair[0]: character_pair[1] for character_pair in zip(alphabet, alphabet_shifted)}

    # convert input string into a list
    word = list(s)

    # iterate over the number of characters
    for number_character in roll:
        # for each #number_character first consecutive character,
        # replace the character with its direct successor in the alphabet 
        for i in range(number_character):
            word[i] = next_character[word[i]]

    # return the converted list of character into a string
    return "".join(word)


def rollTheString(s, roll):
    """
        Function to rotate by one character a consecutive number of characters of a string
        based on a sequence a character number
        eg : inputs :"abc" and [ 3, 2, 1] : "abc" -> "bcd" -> "cdd" -> "ddd"
           : output : "ddd"

        :param s: str
        :param roll: List[int]
        :return: word transformed: str
    """

    # number of rotation to perform per character
    character_shift = []
    roll_without_zero = roll

    # TODO this loop can be improved
    while roll_without_zero:
        character_shift.append(len(roll_without_zero))
        A = list(map(lambda x: x - 1, roll_without_zero))
        roll_without_zero = [x for x in A if x]

    word = []
    for i, c in enumerate(s):

        if i < len(character_shift):
            # apply the x number of rotation only once per character in the string
            word.append(string.ascii_lowercase[(string.ascii_lowercase.index(c) + character_shift[i]) % 26])
        else:
            word += s[i:]
            break

    return "".join(word)


if __name__ == "__main__":
    # pprint.pprint(rollTheString("abc", [3, 2, 1]))

    pprint.pprint(rollTheString2("abc", [3, 2, 1]))
    # pprint.pprint(rollTheString2("abc", [1, 1, 1]))


