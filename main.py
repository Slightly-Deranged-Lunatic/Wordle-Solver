from words_list import words

def main():
    hints = get_hints()
    possible_answers = get_word(hints)
    if len(possible_answers) == 0:
        print("You messed up somewhere or the word just isn't in the dictionary at all.", end = " ")
        close_program()
    print("Possible words are:", end =" ")
    for word in possible_answers:
        print(word, end=", ")
    close_program()

def get_hints():
    # User input to get all the hints for the word
    while True:
        green_letters = list(input("Enter all green letters you know so far, use underscores to show none and press enter if none: ").lower().strip())
        green_letters = add_dummy_input(green_letters)
        if is_valid_input(green_letters):
            break

    yellow_letters = []
    row_counter = 1
    while True:
        new_yellow_letters = list(input(f"Enter the yellow letters for row {row_counter}, use underscores to show no letters, and press enter if none: ").lower().strip())
        new_yellow_letters = add_dummy_input(new_yellow_letters)
        if is_valid_input(new_yellow_letters):
            yellow_letters.append(new_yellow_letters)
            row_counter += 1
        if len(yellow_letters) == 5:
            break

    while True:
        grey_letters = list(input("Enter all grey letters: ").lower().strip())
        grey_letters = add_dummy_input(grey_letters)
        if is_valid_input(grey_letters, length_check = False):
            break

    hints = {
        "green letters" : green_letters,
        "yellow letters" : yellow_letters,
        "grey letters" : grey_letters
    }
    return hints

def get_word(hints):
    # Returns all possible words
    possible_words = list(words)
    possible_words = filter_grey_letters(hints, possible_words)
    possible_words = filter_green_letters(hints, possible_words)
    possible_words = filter_yellow_letters(hints, possible_words)
    return possible_words

def add_dummy_input(letter_list):
    if letter_list == []:
        for i in range(5):
            letter_list.append("_") # 5 underscores to represent no information
    return letter_list

def is_valid_input(user_input, length_check = True):
    WHITELISTED_LETTERS = "abcdefghijklmnopqrstuvwxyz_"
    if length_check:
        if len(user_input) != 5:
            print("Not enough characters, please try again.")
            return False

    for i in user_input:
        if i not in WHITELISTED_LETTERS:
            print(f"Unaccepted input {i}, please try again.")
            return False
    return True

def filter_green_letters(hints, possible_words):
    # Filters out possible words using green letters
    green_letters = hints["green letters"]
    new_words = list(possible_words)
    for word in possible_words:
        to_remove = remove_green_letters(green_letters, word)
        if to_remove:
            new_words.remove(word)
    return new_words

def remove_green_letters(green_letters, word):
    # Checks to see if the word has green letters in the right position
    for i in range(len(word)):
        if word[i] != green_letters[i] and green_letters[i] != "_":
            return True

def filter_grey_letters(hints, possible_words):
    # Filters out possible words using green letters
    grey_letters = hints["grey letters"]
    new_words = list(possible_words)
    for word in possible_words:
        to_remove = remove_grey_letters(grey_letters, word)
        if to_remove:
            new_words.remove(word)
    return new_words

def remove_grey_letters(grey_letters, word):
    # Checks to see if the word contains a grey letter
    for letter in word:
        if letter in grey_letters:
            return True

def filter_yellow_letters(hints, possible_words):
    # Filters out possible words using green letters
    yellow_letters = hints["yellow letters"]
    new_words = list(possible_words)
    for word in possible_words:
        to_remove = remove_yellow_letter(yellow_letters, word)
        if not to_remove:
            to_remove = check_yellow_letter_position(yellow_letters, word)
        if to_remove:
            new_words.remove(word)
    return new_words

def remove_yellow_letter(yellow_letters, word):
    # Checks to see if the word doesn't have a yellow letter in it at all
    for row in yellow_letters:
        for yellow_letter in row:
            if yellow_letter not in word and yellow_letter != "_":
                return True
    return False

def check_yellow_letter_position(yellow_letters, word):
    # Checks to see if the positions of the yellow letter input and yellow letters in word are the same 
    for i in range(len(word)):
        for row in yellow_letters:
            if word[i] == row[i]:
                return True
    return False

def close_program():
    termination = input("\nPress enter when you are ready to close the program.")
    raise SystemExit

if __name__ == "__main__":
    main()