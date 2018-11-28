import string
import pprint


def rotate_character(word, rotation_list):
    alphabet = list(string.ascii_lowercase)
    alphabet_shifted = alphabet[1:] + alphabet[:1]

    next_character = {character_pair[0]: character_pair[1] for character_pair in zip(alphabet, alphabet_shifted)}

    word_sequence = list(word)

    for shift_count in rotation_list:
        for i in range(shift_count):
            word_sequence[i] = next_character[word_sequence[i]]

    return "".join(word_sequence)


if __name__ == "__main__":
    pprint.pprint(rotate_character("abc", [3, 2, 1]))
