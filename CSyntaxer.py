import re

TOKEN_TYPES = {
    'STORAGE_CLASS_SPECIFIER': r'(auto|register|static|extern)?',
    'TYPE_QUALIFIER': r'(const|volatile)?',
    'SIGN_SPECIFIER': r'(signed|unsigned)?',
    'SIZE_SPECIFIER': r'(short|long(\s+long)?)?',
    'BASE_TYPE': r'(int|float|double|boolean|char)',
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'ASSIGNMENT_OP': r'=',
    'INTEGER': r'-?\d+',
    'FLOAT': r'-?\d+\.\d+',
    'BOOLEAN': r'(true|false)',
    'STRING': r'"(?:\\"|[^"])*"',
    'CHAR': r"'.'",
    'SEMICOLON': r';',
    'OPERATOR': r'[\+\-\*\/\%\&\|\^\>\<]',
    'COMMA': r',',
    'BRACKET': r'[\[\]\(\)\{\}]',
    'FUNCTION': r'(printf|scanf)',
    'BITWISE_OP': r'[\&\|\^\>\<\<\>\>]',
    'FORMAT_SPECIFIER': r'%[\-\+]?(\d+|\*)?(\.\d+)?[cdieEfgGllopuXxs%]'
}

def isValid(inStr: str) -> bool:
    type_regex = r"^(?:" + TOKEN_TYPES['STORAGE_CLASS_SPECIFIER'] + r"\s+)?" + \
                 TOKEN_TYPES['BASE_TYPE'] + \
                 r"\s+" + TOKEN_TYPES['IDENTIFIER'] + \
                 r"\s*(?:" + TOKEN_TYPES['ASSIGNMENT_OP'] + \
                 r"\s*(?:" + TOKEN_TYPES['INTEGER'] + \
                 r"|" + TOKEN_TYPES['FLOAT'] + \
                 r"|" + TOKEN_TYPES['STRING'] + \
                 r"|" + TOKEN_TYPES['CHAR'] + r"))?" + \
                 TOKEN_TYPES['SEMICOLON'] + r"$"

    if re.match(type_regex, inStr):
        return True
    else:
        return False

def main():
    while True:
        print("Menu:")
        print("1. Input one-line C code")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            inFromUsr = input("Input one line C code: ")
            if isValid(inFromUsr):
                print("Valid+++++++++ C code one-liner:", inFromUsr)
            else:
                print("--------INVALID C code one-liner:", inFromUsr)
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
