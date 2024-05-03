import re

def isValid(inStr: str) -> bool:
    if 0 < len(re.compile("char").findall(inStr)):
        if 0 < len(re.compile(r"^ *(const)? *char *[a-zA-Z_]+[0-9a-zA-Z_]*\[[0-9]+\]").findall(inStr)):
            return bool(re.match(r"^ *(const)? *char *[a-zA-Z_]+[0-9a-zA-Z_]*\[[0-9]+\] *(= *\".*\")? *;$", inStr))
        return bool(re.match(r"^ (const)? *char *[a-zA-Z_]+[0-9a-zA-Z_] *(= *\'.\')? *;$", inStr))
    elif 0 < len(re.compile("int").findall(inStr)):
        return bool(re.match(r"^ (const)? *int *[a-zA-Z_]+[0-9a-zA-Z_] *(= *[0-9]+)? *;$", inStr))
    elif 0 < len(re.compile("float").findall(inStr)):
        return bool(re.match(r"^ (const)? *float *[a-zA-Z_]+[0-9a-zA-Z_] *(= *[0-9]+\.[0-9]+)? *;$", inStr))
    elif 0 < len(re.compile("double").findall(inStr)):
        return bool(re.match(r"^ (const)? *double *[a-zA-Z_]+[0-9a-zA-Z_] *(= *[0-9]+\.[0-9]+)? *;$", inStr))
    return False

def main():
    while True:
        print("1. Enter one-line C code")
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
