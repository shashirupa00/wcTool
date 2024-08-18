#!/usr/bin/env python3

import sys
import chardet

def detect_encoding(filename):
    with open(filename, 'rb') as file:
        raw = file.read(10000)  # Read the first 10000 bytes
    return chardet.detect(raw)['encoding']

def count_words(filename):
    
    try:
        encoding = detect_encoding(filename)
        with open(filename, 'r', encoding=encoding) as file:
            content = file.read()
            word_count = len(content.split())
        return word_count

    except FileNotFoundError:
        print("Error: file not found")
        sys.exit(1)

def count_bytes(filename):
    
    try:
        with open(filename, 'rb') as file:
            content = file.read()
        return len(content)
    
    except FileNotFoundError:
        print("Error: file not found")
        sys.exit(1)

def count_lines(filename):

    encoding = detect_encoding(filename)
    try:
        with open(filename, 'r', encoding=encoding) as file:
            lines = file.readlines()
        return len(lines)
    
    except FileNotFoundError:
        print("Error: file not found")
        sys.exit(1)

def count_chars(filename):

    encoding = detect_encoding(filename)
    try:
        char_count = 0
        with open(filename, 'r', encoding=encoding) as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                char_count += len(chunk)
        return char_count
    
    except FileNotFoundError:
        print("Error: file not found")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: ccwc -[mode] <filename>")
        sys.exit(1)
    

    if len(sys.argv) == 2:
        filename = sys.argv[1]
        byte_count = count_bytes(filename)
        word_count = count_words(filename)
        line_count = count_lines(filename)

        print(f"{byte_count} {word_count} {line_count} {filename}")
        sys.exit(1)
    
    filename = sys.argv[2]
    
    if sys.argv[1] == '-c':
        byte_count = count_bytes(filename)
        print(f"{byte_count} {filename}")

    elif sys.argv[1] == '-w':
        word_count = count_words(filename)
        print(f"{word_count} {filename}")
    
    elif sys.argv[1] == '-l':
        line_count = count_lines(filename)
        print(f"{line_count} {filename}")
    
    elif sys.argv[1] == '-m':
        char_count = count_chars(filename)
        print(f"{char_count} {filename}")
    
    else:
        print("Usage: ccwc -[mode] <filename>")
        sys.exit(1)

if __name__ == "__main__":
    main()