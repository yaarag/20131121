from bottle import route, run, request, post

list = [0,0,0,0]

@route('/yaara/')
def multic():
    return """
	<p><b>Anger and forgiveness:</b> <br> What sentence from the sentences below describes your attitude for anger?.</p>
	<form name="mypage" method="post" action="/yaara/">
	<input type="radio" name="philosof" value="1">Each minute of anger, you loose 60 seconds of peace(pooh)<br>
	<input type="radio" name="philosof" value="2">Always forgive your enemies - nothing annoys them so much.(oscar wilde)<br>
	<input type="radio" name="philosof" value="3">Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured.(mark twain) <br>
	<input type="radio" name="philosof" value="4">Don't get angry, or never forgive (shpinoze)<br>
	<input name="submit" input type="submit" value="Submit">
	</form>
    """

 
def add_to_list (index):
	list[index] += 1
	print list[index]

def get_max_index():
    max_index = list.index(max(list))
    return max_index
     	 
 
 
@post('/yaara/')
def login_form_post():
	num  = request.forms.get("philosof")
	add_to_list(int(num)-1)
	return """
	<p><b>Happiness:</b> <br> What sentence from the sentences below describes your attitude for happines?.</p>
	<form name="mypage" method="post" action="/yaaraq1/">
	<input type="radio" name="philosof" value="1">The happiest moment is the moment just before you eat honey(pooh)<br>
	<input type="radio" name="philosof" value="2">Some cause happiness wherever they go; others whenever they go.(oscar wilde)<br>
	<input type="radio" name="philosof" value="3">Happiness is a Swedish sunset; it is there for all, but most of us look the other way and lose it.(mark twain) <br>
	<input type="radio" name="philosof" value="4">All happiness or unhappiness solely depends upon the quality of the object to which we are attached by love.(shpinoze)<br>
	<input name="submit" input type="submit" value="Submit">
	</form>
    """
    
@post ('/yaaraq1/')
def after_sec_question():
    num  = request.forms.get("philosof")
    add_to_list(int(num)-1) 
    return """
	<p><b>Wisdom:</b> <br> What sentence from the sentences below describes your attitude for wisdom?.</p>
	<form name="mypage" method="post" action="/yaaraq2/">
	<input type="radio" name="philosof" value="1">Whoever knows so much, does not understand anything anymore(pooh)<br>
	<input type="radio" name="philosof" value="2">I am so clever that sometimes I don't understand a single word of what I am saying.(oscar wilde)<br>
	<input type="radio" name="philosof" value="3">It is better to remain silent and be thought a fool than to open one's mouth and remove all doubt.(mark twain) <br>
	<input type="radio" name="philosof" value="4">The less the mind understands and the more things it perceives, the greater its power of feigning is; and the more things it understands, the more that power is diminished.(shpinoze)<br>
	<input name="submit" input type="submit" value="Submit">
	</form>
    """
	
@post ('/yaaraq2/')
def after_third_question():
    num  = request.forms.get("philosof")
    add_to_list(int(num)-1) 
    return """
	<p>All you need is <b>love:</b> <br> What sentence from the sentences below describes your attitude for wisdom?.</p>
	<form name="mypage" method="post" action="/yaaraq3/">
	<input type="radio" name="philosof" value="1">Some people care too much. I think it's called love(pooh)<br>
	<input type="radio" name="philosof" value="2">One should always be in love. That is the reason one should never marry.(oscar wilde)<br>
	<input type="radio" name="philosof" value="3">Love is the irresistible desire to be irresistibly desired.(mark twain) <br>
	<input type="radio" name="philosof" value="4">The intellectual love of the mind towards God is part of the infinite love wherewith God loves himself. The love of God towards men, and the intellectual love of the mind towards God, are identical.(shpinoze)<br>
	<input name="submit" input type="submit" value="Submit">
	</form>
    """	
	
	

	
@post ('/yaaraq3/')
def after_fourth_question():
    num  = request.forms.get("philosof")
    add_to_list(int(num)-1) 
    return """
	<p><b>Friendship:</b> <br> What sentence from the sentences below describes your attitude for friendship?</p>
	<form name="mypage" method="post" action="/yaaraq4/">
	<input type="radio" name="philosof" value="1">It is always useful to know where a friend-and-relation is, whether you want him or whether you dont.<br>
	<input type="radio" name="philosof" value="2">True friends stab you in the front..(oscar wilde)<br>
	<input type="radio" name="philosof" value="3">The proper office of a friend is to side with you when you are in the wrong. Nearly anybody will side with you when you are in the right.<br>
	<input type="radio" name="philosof" value="4">Of all the things that are beyond my power, I value nothing more highly than to be allowed the honor of entering into bonds of friendship with people who sincerely love truth.<br>
	<input name="submit" input type="submit" value="Submit">
	</form>
    """	


@post ('/yaaraq4/')
def after_fourth_question():
    num  = request.forms.get("philosof")
    add_to_list(int(num)-1) 
    return """
	<p><b>And a last sentence to make this world a better place:</b> <br> What sentence from the sentences below describes your attitude for wisdom?</p>
	<form name="mypage" method="post" action="/yaarasol/">
	<input type="radio" name="philosof" value="1">Dont underestimate the value of doing nothing, of just going along, listening to all the things you cant hear,and not bothering.(pooh)<br>
	<input type="radio" name="philosof" value="2">It is better to be beautiful than to be good. But, it is better to be good than to be ugly.(oscar wilde)<br>
	<input type="radio" name="philosof" value="3">Good friends, good books and a sleepy consciencethis is the ideal life. The conviction of the rich that the poor are happier is no more foolish than the conviction of the poor that the rich are.(mark twain)<br>
	<input type="radio" name="philosof" value="4">The world would be happier if men had the same capacity to be silent that they have to speak.(shpinoza)<br>
	<input name="submit" input type="submit" value="Submit">
	</form>
    """	

	

@post ('/yaarasol/')
def after_sec_question():
    num  = request.forms.get("philosof")
    add_to_list(int(num)-1)
    image_num = get_max_index()
    if image_num == 0 :
	    return """
        <p> Your opinions are similiar to the spirit of....<br><b>Winnie the Pooh</b> <br> </p>
	    <img src= "http://t0.gstatic.com/images?q=tbn:ANd9GcQp75TdxYb_H9MtI_pZqrdwVT0OYjFfeJAuDHXbBhAmWQMhO3jm1g" alt="Winnie the Pooh" />
        <p> <b>Pooh</b> 's tip for you: <br> You cant stay in your corner of the Forest waiting for others to come to you. You have to go to them sometimes</p>
		"""
    elif image_num == 1:
	    return """
        <p> Your opinions are similiar to the spirit of....<br><b>Oscar Wilde</b> <br> </p>
	    <img src= "http://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Oscar_Wilde_portrait.jpg/150px-Oscar_Wilde_portrait.jpg" alt="Oscar Wilde" />
		<p> <b>Oscar Wilde</b> 's tip for you: <br> Education is an admirable thing, but it is well to remember from time to time that nothing that is worth knowing can be taught.
        """
    elif image_num == 2:
	    return """
        <p> Your opinions are similiar to the spirit of....<br><b>Mark Twain</b> <br> </p>
	    <img src= "http://southernmemoriesandupdates.com/wp-content/uploads/2011/05/2011-01-23-Mark-Twain-300x222.jpg" alt="Mark Twain" />
		<p> <b>Mark Twain</b> 's tip for you : <br> Don't go around saying the world owes you a living. The world owes you nothing. It was here first.
        """
    elif image_num == 3:
	    return """
        <p> Your opinions are similiar to the spirit of....<br><b>Baruch Spinoza</b> <br> </p>
	    <img src= "http://capone.mtsu.edu/rbombard/RB/Images/spinoza1.jpg" alt="Baruch Spinoza" />
		<p> <b>Baruch Spinoza</b> 's tip for you : <br> The highest activity a human being can attain is learning for understanding, because to understand is to be free.
        """
    else:
        return """
	    <img src= "http://i.stack.imgur.com/3mwxc.png" alt="Smiley face" />
	    """

run(host='localhost', port=8080,
    debug=True, reloader=True)