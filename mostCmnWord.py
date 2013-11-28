def findMostCmnWord(stri):
    words = stri.split()
    top_word = ""
    n = 0
    d = {}
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    n = max(d.values())
    for key in d:
        if d[key] == n:
            return key
            
            
def test(s, word):
    rv = findMostCmnWord(s) 
    assert rv == word, '"%s" != "%s"' % (rv, word)

test("Hello Joe how are you today Joe  ", "Joe")
test("Hello Hi Hi Hello Hello  ", "Hello")
test("x y y z z z", "z")
test("x y y y z z", "y")
test("xy xyxyxy xyxyxy", "xyxyxy")

print "ok"
