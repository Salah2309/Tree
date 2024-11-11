from Program.helpers import fileReader
import Program.lexer as lexer
import Program.parser as parser

def run(file):
    for source in fileReader(file):
        tokenSet = []
        for token in lexer.tokenize(source):
            if token[0] != "NEXT": tokenSet.append(token)
            else:
                parser.parse(tokenSet)
                tokenSet = []
        parser.parse(tokenSet)