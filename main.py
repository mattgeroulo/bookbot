
from stats import get_num_words, char_count, sort_char_count
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents=f.read()
    return file_contents

def print_report(bookname,word_count,character_count,sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookname}...")
    print(f"----------- Word Count ----------\nFound {word_count} total words\n--------- Character Count -------")
    for i in sorted_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv)==2:
        book_path = sys.argv[1]
        num_words= get_num_words(get_book_text(book_path))
    
        char_counts= char_count(get_book_text(book_path))
    
        sorted_char_count = sort_char_count(char_counts)
        
        print_report(book_path,num_words,char_counts,sorted_char_count)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
main()
