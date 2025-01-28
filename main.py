path_to_file="books/frankenstein.txt"

def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        print(f"--- Begin report of {path_to_file} ---")
        count_words(file_contents)
        character_dict = character_count(file_contents)
        character_list = convert_to_list(character_dict)
        sorted_list = sort_list(character_list)
        display_report(sorted_list)


def count_words(file_contents):
    words = file_contents.split()
    print(f'{len(words)} words found in the document')
    print("")


def character_count(file_contents):
    characters = {}
    for i in file_contents:
        if i.isalpha():
            c = i.lower()
            if c in characters:
                characters[c] += 1
            else:
                characters[c] = 1
    return characters


def convert_to_list(dict):
    new_list = []
    for letter in dict:
        new_dict = {}
        new_dict["letter"] = letter
        new_dict["num"] = dict[letter]
        new_list.append(new_dict)
    return new_list

def sort_on(dict):
    return dict["num"]

def sort_list(character_list):
    character_list.sort(reverse=True,key=sort_on)
    return character_list

def display_report(sorted_list):
    for i in sorted_list:
        print(f"The '{i["letter"]}' character was found {i["num"]} times")
    print("--- End report ---")


main()
