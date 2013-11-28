def isPalindrom(stri):
    if (len(stri) == 0) | (len(stri) == 1) :
        return True
    if stri[0] != stri[len(stri)-1]:
        return False
    stri = stri[1:len(stri)-1]
    return isPalindrom(stri)


def findPalindromsInTxt():
    myOutput = ""
    file = open("newfile.txt", 'r')
    for line in file:
        line = line[:len(line)-1]
        if (isPalindrom(line)):
            myOutput += line +" " 
    return myOutput


print findPalindromsInTxt()

assert isPalindrom("abbca") == False
assert isPalindrom("aba") == True
assert isPalindrom("rt") == False
assert isPalindrom("ttytt") == True