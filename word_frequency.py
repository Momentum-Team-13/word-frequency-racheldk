from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import re


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # ALL OF MY CODE GOES INSIDE THIS FUNCTION
    # in terminal I'll type: python word_frequency.py [file name]
    
    # print(f'your file is {file}')
    with open(file) as open_file:
        text = open_file.read()
        print(text)

        words_without_breaks = []
        words_to_keep = []
        words_to_count = []
        
        no_punctuation = text.replace("?", "").replace(",", "").replace(".", "").replace("!", "").replace('"', '').replace(':', '').replace(';', '')
        # print(f'no punctuation: {no_punctuation}')       
  
        lower_case = no_punctuation.lower()
        # print(f'lower_case: {lower_case}')

        text_list = lower_case.split(" ")
        # print(f'text_list: {text_list}')


        def remove_breaks(input):
            for word in input:
                word = re.sub("\\n", "", word)
                words_without_breaks.append(word)
                
        remove_breaks(text_list)
        # print(f'words without breaks: {words_without_breaks}')



        def check_words(text_list):
            for word in text_list:
                if word in STOP_WORDS:
                    word = f'stop: {word}'
                    # print(word)
                else:
                    # print(word)
                    words_to_keep.append(word)
                    # print(f'words to keep: {words_to_keep}')
        check_words(words_without_breaks)
        # print(words_to_keep)   

        def do_not_add_repeat_words(input):
            for word in input:
                # if the word does not already appear in our final tally list, add it to the list. if not, don't do anything
                if word in words_to_count:
                    word = f'{word} already in list'
                    # print(word)
                else: 
                    words_to_count.append(word)
                    # print(f'number of {word}: {words_to_keep.count(word)}')
    
        do_not_add_repeat_words(words_to_keep)
        # print(f'words to count: {words_to_count}')

        word_totals = {}
    
        def compile_word_counts(input):
            for word in input:
                word_totals[word] = words_to_keep.count(word)
            # print(word_totals)  
        
        compile_word_counts(words_to_count)
        # word_totals['star_test'] = '*' * 3
        # word_totals['star_test'] = 3
        # print(f'word total dictionary: {word_totals}')
        # print(word_totals['star_test'])
        # print('*' * int(word_totals['hello']))

        ordered_words = {k: v for k, v in sorted(word_totals.items(), key=lambda item: item[1], reverse=True)}
        # print(ordered_words)

        def add_stars_and_format(input):
            for word in input:
                name = word
                bar = "|"
                number = word_totals[word]
                star = '*' * int(word_totals[word])
                print("{:<20} {:<1} {:<2} {:<40}".format(name.rjust(20), bar, number, star))
                
        add_stars_and_format(ordered_words)

        
    # opened the file and made it a long string with new lines in it 
    # using open_file.readlines() will make it a list I think 
    # print(type(read_file))
    


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

