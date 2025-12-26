import argparse
import os
import re

from colorama import init, Fore, Style

init(autoreset=True)


def highlight_text(words, search_text):
    result = []
    for word in words:
        if search_text.lower() in word.lower():
            result.append(Fore.RED + word + Style.RESET_ALL)
        else:
            result.append(word)
    return ' '.join(result)


parser = argparse.ArgumentParser()
parser.add_argument('path', help='Path to file')
parser.add_argument('-t', '--text', required=True)
parser.add_argument('--full', action='store_true')
args = parser.parse_args()

print("Path:", args.path)
print("Text:", args.text)
print("Full:", args.full)

files = [args.path] if os.path.isfile(args.path) else \
    [os.path.join(args.path, f) for f in os.listdir(args.path) if os.path.isfile(os.path.join(args.path, f))]

time_re = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})')

for file in files:
    with open(file, encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    blocks = {}
    current_time = None
    current_block = []

    for line in lines:
        match = time_re.match(line)
        if match:
            if current_time:
                blocks[current_time] = ''.join(current_block)
            current_time = match.group(1)
            current_block = [line]
        else:
            current_block.append(line)
    if current_time:
        blocks[current_time] = ''.join(current_block)

    for time, block in blocks.items():
        if args.text.lower() in block.lower():
            print(f'Файл: {file}, Время: {time}')
            if args.full:
                print(block.strip())
            else:
                words = block.split()
                for i, word in enumerate(words):
                    if args.text.lower() in word.lower():
                        start = max(0, i - 5)
                        end = min(len(words), i + 6)
                        context_word = words[start:end]
                        highlight = highlight_text(context_word, args.text)
                        print(highlight)
                        break

            print()
