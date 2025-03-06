import sys

from stats import count_characters
from stats import count_words
from stats import count_characters2

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

def sysinput(input):
    return(input[1])

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_contents = get_book_text(sysinput(sys.argv))
    
        print("============ BOOKBOT ===========")
        print(f"Analyzing book found at {sysinput(sys.argv)}...")
        print("----------- Word Count ----------")
        print(f"Found {count_words(book_contents)} total words")
        print("--------- Character Count -------")
        print(f"{count_characters2(book_contents)}")
        print("============= END ===============")

main()