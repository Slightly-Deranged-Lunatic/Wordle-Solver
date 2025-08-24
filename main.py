from words_list import words

def main():
    hints = get_hints()
    get_word(hints)

def get_hints():
    green_letters = list(input("Enter all green letters you know so far, use a space to show none ").lower())
    yellow_letters = []
    for i in range(1, 6):
        yellow_letters.append(list(input(f"Enter the yellow letters for row {i}, use spaces to show no letters ").lower()))
    grey_letters = list(input("Optional: Enter all letters without a color. This is optional but doing so will significantly improve the accuracy ").lower())
    hints = {
        "green letters" : green_letters,
        "yellow letters" : yellow_letters,
        "grey letters" : grey_letters
    }
    return hints

def get_word(hints):
    possible_words = list(words)
    possible_words = filter_grey_letters(hints, possible_words)
    possible_words = filter_green_letters(hints, possible_words)
    possible_words = filter_yellow_letters(hints, possible_words)
    print(possible_words)

def filter_green_letters(hints, possible_words):
    green_letters = hints["green letters"]
    new_words = list(possible_words)
    for word in possible_words:
        for i in range(len(word)):
            if word[i] != green_letters[i] and green_letters[i] != " ":
                new_words.remove(word)
                break
    return new_words

def filter_yellow_letters(hints, possible_words):
    yellow_letters = hints["yellow letters"]
    new_words = list(possible_words)
    for word in possible_words:
        for row in yellow_letters:
            for yellow_letter in row:
                if yellow_letter not in word and yellow_letter != " ":
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