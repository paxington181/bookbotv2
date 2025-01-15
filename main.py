def main():
    bookfile = "books/frankenstein.txt"        
    book_text = get_book(bookfile)
    split_text = text_splitter(book_text) 
    word_counter = list_len(split_text)
    lower_case_dictionary = l_case_dict(book_text)
    percent_alphabet = "place holder"


    print(f"Review of text begins")
    print(f"The book contained in {bookfile} contains {word_counter} words.")
    print(f"{percent_alphabet}% of the characters in {bookfile} are letters.")
    print(lower_case_dictionary)


def get_book(path):
    with open(path) as f:
        return f.read()
    
def text_splitter(book_text_split):
    split = []
    split = book_text_split.split()
    return split

def list_len(split_text):
    return len(split_text)

def l_case_dict(book_text):
    l_case = book_text.lower()
    letter_list = list(l_case)
    dictionary = {}
    for let in letter_list:
        if let == "\n":
            continue        
        if let in dictionary:
            dictionary[let] += 1
        else:
            dictionary[let] = 1
    return dictionary

def sort_on(l_case_dict):
    return l_case_dict["num"]

main()