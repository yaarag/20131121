from bottle import route, run, request, post
@route('/multi')
def multic():
    return """
    <form name="mult" method="post" action="/multi/">
    <input name="n">
    <input type="submit" value="Enter">
    </form>
    """

 
def multi(n):
    Matrix = [[0 for x in xrange(n)] for x in xrange(n)] 
    for i in range(n):
        for j in range(n):
            Matrix[i][j] = (i+1) * (j+1)
    return Matrix
 
# print multi(3)
 
 
def html_table(m):
    """ gets a two dimensional list, returns a html table """
    s= "<table>"
    for i in range(len(m)):
        s += "<tr>"
        for j in range(len(m[0])):
            s += "<td>%d</td>" %(m[i][j])
        s +="</tr>"   
    s += "</table>"       
    return s
 
 
 
@post('/multi/')
def login_form_post():
    num = int (request.forms.get("n"))
    return html_table(multi(num))
 
assert "<table><tr><td>1</td></tr></table>" == html_table([[1]])
assert "<table><tr><td>1</td><td>2</td></tr></table>" == html_table([[1, 2]])
assert "<table><tr><td>1</td></tr><tr><td>2</td></tr></table>" == html_table([[1], [2]])

run(host='localhost', port=8080,
    debug=True, reloader=True)