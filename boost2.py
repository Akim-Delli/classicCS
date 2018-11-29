import string
import pprint


def rotate_character(word_as_string, rotation_list):
    """
    Function to rotate by one character a consecutive number of characters of a string
    based on a sequence a character number
    eg : inputs :"abc" and [ 3, 2, 1] : "abc" -> "bcd" -> "cdd" -> "ddd"
       : output : "ddd"

    :param word_as_string: str
    :param rotation_list: List[int]
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
    word = list(word_as_string)

    # iterate over the number of characters
    for number_character in rotation_list:
        # for each #number_character first consecutive character,
        # replace the character with its direct successor in the alphabet 
        for i in range(number_character):
            word[i] = next_character[word[i]]

    # return the converted list of character into a string
    return "".join(word)


if __name__ == "__main__":
    pprint.pprint(rotate_character("abc", [3, 2, 1]))
