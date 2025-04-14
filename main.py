from stats import get_num_words, get_letter_array, sort_letter_dict
import sys

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    booktext = get_book_text(sys.argv[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    get_num_words(booktext)
    print(sort_letter_dict(get_letter_array(booktext)))
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read() 

   

main()