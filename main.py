import sys
from collections import Counter


def count_total_words(text: str) -> int:
    return len(text.split())

def count_chars(text: str) -> Counter:
    chars = list(text.lower())
    return Counter(chars)

def get_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def print_report(path: str, n_words: int, counts: Counter) -> None:
    print(f'--- Begin report of {path} ---')
    print(f'{n_words:,} words found in the document\n')
    for c, n in counts.most_common():
        if c.isalpha():
            print(f"The '{c}' character was found {n:,} times")
    print('--- End report ---')

def main(path: str) -> None:
    text = get_text(path)
    n_words = count_total_words(text)
    counts = count_chars(text)
    print_report(path, n_words, counts)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Path to the document')
    args = parser.parse_args()

    sys.exit(main(args.path))
