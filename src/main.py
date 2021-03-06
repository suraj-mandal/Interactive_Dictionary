import json
from difflib import get_close_matches

# loading the json file and storing it in the data variable
data = json.load(open('./data.json'))

dictionary_available_words = data.keys()


def print_pretty_output(word: str) -> None:
    """
    print the output in human readable form
    :param word:
    :return:
    """
    for (index, definition) in enumerate(data[word]):
        print(f'{index + 1}. {definition}')


# improving the performance of the application
def find_similar_word(word: str) -> list or None:
    """
    returns the word, which is most similar with the argument else returns None
    :param word:
    :return:
    """
    filtered_list = list(filter(lambda x: x.startswith(word[0]), dictionary_available_words))
    closest_match = ''.join(get_close_matches(word, filtered_list, n=1))
    return closest_match if closest_match else None


def translate(word: str) -> None:
    """
    prints the definition of the word and implements the login of the above two function
    :param word:
    :return:
    """
    if word not in dictionary_available_words:
        # checking for similar words
        similar_word = find_similar_word(word)
        if not similar_word:
            print("The word is not present in the dictionary!!")
        else:
            choice = input(f'Did you mean {similar_word}? (Y / N) : ')
            if choice.lower() == 'y':
                print_pretty_output(similar_word)
            else:
                print("The word is not present in the dictionary")

    else:
        print_pretty_output(word)


if __name__ == '__main__':
    while True:
        translate(input("Enter word : ").lower())
        print("--------------------------")
        choice = input("Want to search for more words ? (Y / N) : ")
        if choice.lower() != 'y':
            exit(0)
        else:
            continue
