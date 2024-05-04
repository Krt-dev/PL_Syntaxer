import re


def isValid(inStr: str) -> bool:
    char_regex = r"^(const)?\s*char\s+[a-zA-Z_]+\w*\[[0-9]+\]\s*(=\s*\".*\")?;$"
    int_regex = r"^(const)?\s*int\s+[a-zA-Z_]+\w*\s*(=\s*[0-9]+)?\s*;$"
    float_regex = r"^(const)?\s*float\s+[a-zA-Z_]+\w*\s*(=\s*[0-9]+\.[0-9]+)?\s*;$"
    double_regex = r"^(const)?\s*double\s+[a-zA-Z_]+\w*\s*(=\s*[0-9]+\.[0-9]+)?\s*;$"

   
    if re.match(char_regex, inStr) or re.match(int_regex, inStr) or re.match(float_regex, inStr) or re.match(double_regex, inStr):
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
