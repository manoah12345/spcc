import re

# Predefined grammar sets
VERBS = {"hate", "like"}  # 'chase' not included — will be treated as noun
KEYWORDS = {"if", "then"}

# Token pattern
TOKEN_PATTERN = re.compile(r"[a-z]+|[.$]")

# Symbol table
noun_counter = 1
noun_map = {}

def tokenize(input_str):
    return TOKEN_PATTERN.findall(input_str.lower())

def get_noun_index(noun):
    global noun_counter
    if noun not in noun_map:
        noun_map[noun] = noun_counter
        noun_counter += 1
    return noun_map[noun]

def process_tokens(tokens):
    output = []
    for token in tokens:
        if token in KEYWORDS:
            output.append("(k)")
        elif token in VERBS:
            output.append("(v)")
        elif token == ".":
            output.append("(op)")
        elif token == "$":
            output.append("<eof>")
        elif token == "they":
            output.append("(a)")
        else:
            output.append(f"(n,{get_noun_index(token)})")
    return output

def print_symbol_table():
    print("\nSymbol Table:")
    print("----------------")
    print(f"{'Noun':<10} | {'Index'}")
    print("----------------")
    for noun, idx in sorted(noun_map.items(), key=lambda x: x[1]):
        print(f"{noun:<10} | {idx}")
    print("----------------")

# Run the parser on the hardcoded input
if __name__ == "__main__":
    input_str = "If dogs hate cats then they chase. $"
    tokens = tokenize(input_str)
    print("\nInput:", input_str)
    print("Tokens:", tokens)
    output = process_tokens(tokens)
    print("Output:", " ".join(output))
    print_symbol_table()
