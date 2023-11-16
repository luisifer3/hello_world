def main():
    book_path = "/home/lqreyes/workspace/github.com/luisifer3/hello_world/books/frankenstein.txt"
    text = get_book_text(book_path) 
    word_count = get_word_count(text)
    letterdict = get_letter_count(text)
    letterlist = chars_dict_to_sorted_list(letterdict)
    print(f"{word_count} words found in the document")
    print()

    for items in letterlist:
        if not items["char"].isalpha():
            continue
        print(f"The '{items['char']}' character was found {items['num']} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    textlist = []
    textlist = text.split()
    return len(textlist)

def get_letter_count(text):
    textlist = []
    letterdict = {}
    textlist = text.split()
    for word in textlist:
        for letter in word:
            if letter.lower() in letterdict:
                letterdict[letter.lower()] += 1
            else:
                letterdict[letter.lower()] = 1
    return letterdict

def chars_dict_to_sorted_list(dictionary):
    sortedlist = []
    for dictitem in dictionary:
        sortedlist.append({"char": dictitem, "num":dictionary[dictitem]})
    sortedlist.sort(reverse=True, key=sort_on)
    return sortedlist

def sort_on(d):
    return d["num"]

main()