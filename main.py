def main():
    bookfile = "books/frankenstein.txt"        
    book_text = get_book(bookfile)
    split_text = text_splitter(book_text) 
    word_counter = list_len(split_text)
    lower_case_dictionary = l_case_dict(book_text)
    dict_to_list = list_converter(lower_case_dictionary)
    total, percent_alphabet, not_alphabet = calculate_percent(dict_to_list)
    percent_loss = 100 - (percent_alphabet + not_alphabet)

    print(f"Review of text begins")
    print(f"The book contained in {bookfile} contains {word_counter} words.")
    print(f"There are {total} characters in the book, {percent_alphabet}% are alphabetical, {not_alphabet}% are not.")
    print(f"{percent_loss}% is lost due to rounding errors.")
    print("The letters are broken down as follows:")
    print()
    
    for l in dict_to_list:
        if not l["let"].isalpha():
            continue
        else:
            print(f"The letter '{l['let']}' appears {l['num']} times.")
    print()
    print("This ends the report")


def calculate_percent(dict_to_list): 
    alpha_only = 0
    not_alpha = 0
    for l in dict_to_list:
        if not l["let"].isalpha():
            not_alpha += l["num"]
        else:
            alpha_only += l["num"]
    print(f"{not_alpha} not alpha")
    print(f"{alpha_only} alpha")
    total = alpha_only + not_alpha
    flo = (alpha_only / total) * 100
    percent = int(flo)
    na_flo = (not_alpha / total) * 100
    na_percent = int(na_flo)
    return total, percent, na_percent

def list_converter(l_case_dict):
    list_sort = []
    for let in l_case_dict:
        list_sort.append({"let":let, "num":l_case_dict[let]})
    list_sort.sort(reverse = True, key=sort_on)
    return list_sort

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
        if let == " ":
            continue
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