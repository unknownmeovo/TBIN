#!/usr/bin/env python3
import sys

def text_to_binary(text):
    binary_result = ' '.join(format(ord(char), '08b') for char in text)
    return binary_result

def main():
    if len(sys.argv) < 2:
        print("Usage: tbin <text>")
        sys.exit(1)
    
    text = ' '.join(sys.argv[1:])
    binary_text = text_to_binary(text)
    print("Binary Output:", binary_text)

if __name__ == "__main__":
    main()
