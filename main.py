words_list = []
with open("words.txt") as file:
    file_contents = file.readlines()
    for word in file_contents:
        if "\n" in word:
            word = word.replace("\n", "")
        words_list.append(word)

with open("words.py", "w") as output:
    output.write("words = [\n")

with open("words.py", "a") as output:
    for i in words_list:
        output.write(f'\t"{i}",\n')
    output.write("]")