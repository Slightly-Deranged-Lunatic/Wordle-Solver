from words_list import words

def main():
    hints = get_hints()
    possible_answers = get_word(hints)
    print("Possible words are:", end=" ")
    for word in possible_answers:
        print(word, end=", ")

def get_hints():
    while True:
        green_letters = list(input("Enter all green letters you know so far, use a space to show none ").lower().strip())
        green_letters = add_dummy_input(green_letters)
        if is_valid_input(green_letters):
            break

    yellow_letters = []
    row_counter = 1
    while True:
        new_yellow_letters = list(input(f"Enter the yellow letters for row {row_counter}, use spaces to show no letters, and press enter if none ").lower().strip())
        new_yellow_letters = add_dummy_input(new_yellow_letters)
        if is_valid_input(new_yellow_letters):
            yellow_letters.append(new_yellow_letters)
            row_counter += 1
        if len(yellow_letters) == 5:
            break

    while True:
        grey_letters = list(input("Enter all letters without a color. ").lower().strip())
        grey_letters = add_dummy_input(grey_letters)
        if is_valid_input(grey_letters, length_check = False):
            break

    hints = {
        "green letters" : green_letters,
        "yellow letters" : yellow_letters,
        "grey letters" : grey_letters
    }
    return hints

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

def get_word(hints):
    possible_words = list(words)
    possible_words = filter_grey_letters(hints, possible_words)
    possible_words = filter_green_letters(hints, possible_words)
    possible_words = filter_yellow_letters(hints, possible_words)
    return possible_words

def filter_green_letters(hints, possible_words):
    green_letters = hints["green letters"]
    new_words = list(possible_words)
    for word in possible_words:
        for i in range(len(word)):
            if word[i] != green_letters[i] and green_letters[i] != "_":
                new_words.remove(word)
                break
    return new_words

def filter_yellow_letters(hints, possible_words):
    yellow_letters = hints["yellow letters"]
    new_words = list(possible_words)
    for word in possible_words:
        for row in yellow_letters:
            for yellow_letter in row:
                if yellow_letter not in word and yellow_letter != "_":
                    new_words.remove(word)
                    break
            if word not in new_words:
                break
        if word not in new_words:
            continue
        for i in range(len(word)):
            for row in yellow_letters:
                if word[i] == row[i]:
                    new_words.remove(word)
                    break
            if word not in new_words:
                break
        if word not in new_words:
            continue
    return new_words

def filter_grey_letters(hints, possible_words):
    grey_letters = hints["grey letters"]
    for word in words:
        for letter in word:
            if letter in grey_letters:
                possible_words.remove(word)
                break
    return possible_words

if __name__ == "__main__":
    main()