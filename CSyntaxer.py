import re

def isValid(inStr: str) -> bool:
    if 0<len(re.compile("char").findall(inStr)):
        if 0<len(re.compile(r"^ *(const)? *char *[a-zA-Z_]+[0-9a-zA-Z_]*\[[0-9]+\]").findall(inStr)):
            return bool( re.match(r"^ *(const)? *char *[a-zA-Z_]+[0-9a-zA-Z_]*\[[0-9]+\] *(= *\".*\")? *;$", inStr) )
        return bool( re.match(r"^ (const)? *char *[a-zA-Z_]+[0-9a-zA-Z_] *(= *\'.\')? *;$", inStr) )
    elif 0<len(re.compile("int").findall(inStr)):
        return bool( re.match(r"^ (const)? *int *[a-zA-Z_]+[0-9a-zA-Z_] *(= *[0-9]+)? *;$", inStr) )
    elif 0<len(re.compile("float").findall(inStr)):
        return bool( re.match(r"^ (const)? *float *[a-zA-Z_]+[0-9a-zA-Z_] *(= *[0-9]+\.[0-9]+)? *;$", inStr) )
    elif 0<len(re.compile("double").findall(inStr)):
        return bool( re.match(r"^ (const)? *double *[a-zA-Z_]+[0-9a-zA-Z_] *(= *[0-9]+\.[0-9]+)? *;$", inStr) )
    return False

def main():
    inFromUsr = str(input("Input one line c code: "))
    if isValid(inFromUsr):
        print("Valid+++++++++ c code one liner: ", inFromUsr)
    else:
        print("--------INVALD c code one liner: ", inFromUsr)
    '''
     * to check
     * int a = 23, b = 45, c = 67;
     * int a[4][2] = {
     * {1,2},
     * {1,2},
     * {1,2},
     * {1,2}
     * };
     * const int a = 23;
     * char, int, float, double
    '''

if _name_ == "_main_":
    main()