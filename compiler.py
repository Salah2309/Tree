import re
import sys
import time

class Tree:
    def __init__(self, name):
        self.name = name
        self.children = []
    def addChild(self, node):
        self.children.append(node)
        
    def __repr__(self):
        return f"Tree({self.name}, {self.children})"

KEYWORDS = ["root",  "in", "and", "swap", "line"]

def compiler(file):
    for line in  fileReader(file):
        tokens = lexer(line)
        for token in tokens:
            print(token)
    return

    while True:
        try:
            token = next(tokens)
            print(token)        
        except:
            break
    
def fileReader(file):
    dataState = ""
    data = ""
    try:
        with open(file, "r") as f:
            while True:
                data += f.read()
                time.sleep(1)
                print(f.read())
                if not data:
                    time.sleep(0.1)
                    continue
                if "\n" in data:
                    dataState += data
                    yield data
                    data = ""
    except Exception as e:
        raise Exception(f"Error parsing file: {e}")



try:
    with open('test.txt', "r") as f:
        while True:
            data = f.readlines()        
            print(data)
            time.sleep(1)
except Exception as e:
    raise Exception(f"Error parsing file: {e}")



def lexer(data):
    types = [
        ("KEY", r'\b(?:' + '|'.join(KEYWORDS) + r')\b'),
        ("NEXT",   r'\n'),
    ]
    regex = '|'.join(f'(?P<{t[0]}>{t[1]})' for t in types)
    position = 0
    curr = ""
    while position < len(data):
        match = re.match(regex, data[position:], re.IGNORECASE)
        if match:
            kind = match.lastgroup
            value = match.group()
            position += len(value)
            if kind == "KEY" or kind == "NEXT":
                if curr:
                    yield "STRING", curr.strip()
                    curr = ""
                yield kind, value.lower()
        else:
            curr += data[position]
            position += 1 
    if curr:
        yield "STRING", curr.strip()

compiler('test.txt')