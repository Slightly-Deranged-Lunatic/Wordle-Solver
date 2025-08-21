from words_list import words as possible_words

def main():
    hints = get_hints()
    get_word(hints)
def get_hints():
    green_letters = list(input("Enter all green letters you know so far, use a space to show none ").lower())
    yellow_letters = list(input("Enter all yellow letters you know so far, use a space to show none ").lower())
    bad_letters = list(input("Optional: Enter all letters without a color. This is optional but doing so will significantly improve the accuracy ").lower())
    hints = {
        "green letters" : green_letters,
        "yellow letters" : yellow_letters,
        "bad letters" : bad_letters
    }
    return hints

def get_word(hints):
    green_letters = hints["green letters"]
    for word in possible_words:
        for i in range(len(word)):
            if word[i] == green_letters[i] or green_letters[i] == " ":
                correct_pos = True
if __name__ == "__main__":
    main()