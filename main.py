from lexer import tokenize
from parser import parse_expression, evaluate

def main():
    while True:
        s = input("Enter expression (or press Enter to quit): ")
        if not s.strip():
            print("Exiting parser.")
            break
        try:
            tokens = tokenize(s)
            root = parse_expression(tokens)
            print("Parsed successfully!")
            print("Evaluated result:", evaluate(root))
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
