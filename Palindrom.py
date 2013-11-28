def isPalindrom(stri):
    if (len(stri) == 0) | (len(stri) == 1) :
        return True
    if stri[0] != stri[len(stri)-1]:
        return False
    stri = stri[1:len(stri)-1]
    return isPalindrom(stri)

assert isPalindrom("aba") == True  
assert isPalindrom("abba") == True
assert isPalindrom("ttytt") == True
assert isPalindrom("abab") == False   