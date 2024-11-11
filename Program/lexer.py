import re
from Program.helpers import KEYWORDS

def tokenize(data):
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
