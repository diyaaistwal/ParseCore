from parser import parser

def main():
    while True:
        s = input("Enter expression (or press Enter to quit): ")
        if not s.strip():
            print("Exiting parser.")
            break
        result = parser.parse(s)
        if result:
            print("Parsed successfully:", result)
        else:
            print("Parsing failed.")

if __name__ == "__main__":
    main()
