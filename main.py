def main():
    bookfile = "books/frankenstein.txt"        
    book_text = get_book(bookfile)
    split_text = text_splitter(book_text) 
    print(split_text)

def get_book(path):
    with open(path) as f:
        return f.read()
    
def text_splitter(book_text_split):
    split = []
    split = book_text_split.split()
    return split




main()