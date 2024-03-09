def main():
    with open("/Users/ross/workspace/github.com/KoalaTheProgrammer/bookbot/books/Frankenstein.txt") as f:
     file_contents = f.read()
    words_count = count_words(file_contents)
    characters_report = get_characters_dictionary(file_contents)

    
    sorted_characters_report = sorted(characters_report.items(), key=sort_by_frequency, reverse=True)

    print_report(words_count, sorted_characters_report)



def count_words(file_contents):
     words = file_contents.split()
     return len(words)


def get_characters_dictionary(file_contents):
    characters = {}
    for char in file_contents.lower():
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def sort_by_frequency(item):
    return item[1]

def print_report(words_count, sorted_characters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document\n")
    
    for char, num in sorted_characters:
        print(f"The '{char}' character was found {num} times")
    
    print("--- End report ---")
main()