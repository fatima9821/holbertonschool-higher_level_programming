#!/usr/bin/python3
for code_ascii in range(ord('a'), ord('z') + 1):
    if chr(code_ascii) not in ['q', 'e']:
        print(chr(code_ascii), end='')
