from bottle import route, run, request, post , default_app

list = [0,0,0,0]
 
@route('/')
def show_first_question():
    return """
	<div style="background-color:greenyellow;height:100%">
    <div style="margin:auto;width:50%;font-family:'Verdana';padding-top:30px">
    <h1 style="text-align:left"><b>Anger and forgiveness</h1> <h3>Which of the following sentences best describes your position towards anger?</h3>
    <form name="mypage" method="post" action="/yaara/">
    <div style="padding-bottom:8px"><input type="radio" name="philosof" value="1">For each minute of anger, you lose 60 seconds of peace</div>
    <div style="padding-bottom:8px"><input type="radio" name="philosof" value="2">Always forgive your enemies - nothing annoys them as much.</div>
    <div style="padding-bottom:8px"><input type="radio" name="philosof" value="3">Anger is an acid that can do more harm to the vessel in<div style="padding-left:20px"> which it is stored, than to anything on which it is poured.</div></div>
    <div style="padding-bottom:8px"><input type="radio" name="philosof" value="4">Don't get angry, or never forgive </div>
    <input name="submit" input type="submit" value="Submit" style="margin-top: 15px;background-color: #6C1CAE;color: white;font-weight: bold;padding: 5px;border-color:gray" />
    </form>
    </div>
    <div style="margin:auto;width:70%;text-align:right">
    <img src = "http://download.installmob.com/animation/ccontennt/10712-f/angry_greg_head_explode.gif?__sid=03J2WIM&lang=en"/>
    </div>
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
    <div style="background-color:#EE537D;height:100%">
    <div style="margin:auto;width:50%;font-family:'Verdana';padding-top:30px">
        <h1 style="text-align:left"><b>Happiness</h1><h3> Which of the following sentences best describes  your position towards happiness?</h3>
        <form name="mypage" method="post" action="/yaaraq1/">
        <div style="padding-bottom:8px"><input type="radio" name="philosof" value="1">The happiest moment is the moment just before you eat honey</div>
        <div style="padding-bottom:8px"><input type="radio" name="philosof" value="2">Some cause happiness wherever they go; others whenever they go.</div>
        <div style="padding-bottom:8px"><input type="radio" name="philosof" value="3">Happiness is a Swedish sunset; it is there for all, but most of us look <div style="padding-left:20px">the other way and lose it.</div></div>
        <div style="padding-bottom:8px"><input type="radio" name="philosof" value="4">All happiness or unhappiness solely depends upon the quality of the <div style="padding-left:20px">object we love.</div></div>
        <input name="submit" input type="submit" value="Submit" style="margin-top: 15px;background-color: #6C1CAE;color: white;font-weight: bold;padding: 5px;border-color:gray" />
        </form>
     </div>
    <div style="margin:auto;width:80%;text-align:right">
    <img src= "http://d.wapday.com:8080/animation/ccontennt/16130-f/happy_face_raising_ey.gif?__sid=ggl&lang=en"  height="200" width="200"/>
    </div>
    </div>
    """
    
@post ('/yaaraq1/')
def after_sec_question():
    num  = request.forms.get("philosof")
    add_to_list(int(num)-1) 
    return """
    <div style="background-color:#43A3D1;height:100%">
    <div style="margin:auto;width:50%;font-family:'Verdana';padding-top:30px">
        <h1 style="text-align:left"><b>Wisdom:</h1><h3> Which of the following sentences best describes your position towards wisdom?</h3>
        <form name="mypage" method="post" action="/yaaraq2/">
         <div style="padding-bottom:8px"><input type="radio" name="philosof" value="1">Whoever knows so much, does not understand anything anymore</div>
         <div style="padding-bottom:8px"><input type="radio" name="philosof" value="2">I am so clever, that sometimes I don't understand a single word that <div style="padding-left:20px">I am saying.</div></div>
         <div style="padding-bottom:8px"><input type="radio" name="philosof" value="3">It is better to remain silent and be thought of as a fool, than to open <div style="padding-left:20px">one's mouth and eliminate all doubt. </div></div>
         <div style="padding-bottom:8px"><input type="radio" name="philosof" value="4">The less the mind understands and the more things it perceives, the <div style="padding-left:20px">greater its power of feigning is; and the more things it understands, the more that power is diminished.</div></div>
         <input name="submit" input type="submit" value="Submit" style="margin-top: 15px;background-color: #6C1CAE;color: white;font-weight: bold;padding: 5px;border-color:gray" />
        </form>
    </div>
    <div style="margin:auto;width:70%;text-align:right">
    <img src= "http://media.tumblr.com/add9c6d11004d574c28764bf1ced3808/tumblr_inline_mlzfj3RD3L1qz4rgp.gif"  height="200" width="300"/>
    </div>
    </div>
    """
        
@post ('/yaaraq2/')
def after_third_question():
    num  = request.forms.get("philosof")
    add_to_list(int(num)-1) 
    return """
    <div style="background-color:F32621;height:100%">
    <div style="margin:auto;width:50%;font-family:'Verdana';padding-top:30px">
    <h1 style="text-align:left">All you need is love </h1><h3>Which of the following sentences best describes your position towards love?</h3>
        <form name="mypage" method="post" action="/yaaraq3/">
        <div style="padding-bottom:8px ; color="red""><input type="radio" name="philosof" value="1">Some people care too much. I think it's called love</div>
        <div style="padding-bottom:8px"><input type="radio" name="philosof" value="2">One should always be in love. That is the reason one should never marry.</div>
        <div style="padding-bottom:8px"><input type="radio" name="philosof" value="3">Love is the irresistible desire to be irresistibly desired. </div>
        <div style="padding-bottom:8px"><input type="radio" name="philosof" value="4">The intellectual love of the mind towards God is part of the infinite love <div style="padding-left:20px">wherewith God loves himself. The love of God towards men, and the intellectual love of the mind towards God, are identical.</div></div>
        <input name="submit" input type="submit" value="Submit" style="margin-top: 15px;background-color: #6C1CAE;color: white;font-weight: bold;padding: 5px;border-color:gray" />
        </form>
        </div>
        <div style="margin:auto;width:70%;text-align:right">
        <img src= "http://www.picgifs.com/disney-gifs/disney-gifs/mickey-and-minnie-mouse/disney-graphics-mickey-and-minnie-mouse-405804.gif"  height="200" width="300"/>
    </div>
    </div>
    """       
        
        

        
@post ('/yaaraq3/')
def after_fourth_question():
    num  = request.forms.get("philosof")
    add_to_list(int(num)-1) 
    return """
    <div style="background-color:#C921F3;height:100%">
    <div style="margin:auto;width:50%;font-family:'Verdana';padding-top:30px">
    <h1 style="text-align:left"><b>Friendship:</h1><h3>Which of the following sentences best describes your position towards friendship?</h3>
        <form name="mypage" method="post" action="/yaaraq4/">
        <div style="padding-bottom:8px"><input type="radio" name="philosof" value="1">It is always useful to know where a friend-and-relation is, whether <div style="padding-left:20px">you want him or whether you dont.</div></div>
        <div style="padding-bottom:8px"><input type="radio" name="philosof" value="2">A true friend stabs you in the front.</div>
        <div style="padding-bottom:8px"><input type="radio" name="philosof" value="3">a true friend should side with you when you are <div style="padding-left:20px">wrong. Nearly anybody will side with you when you are right.</div></div>
        <div style="padding-bottom:8px"><input type="radio" name="philosof" value="4">Of all the things that are beyond my power, I value most <div style="padding-left:20px">the honor of friendship with people who sincerely love truth.</div></div>
        <input name="submit" input type="submit" value="Submit" style="margin-top: 15px;background-color: #6C1CAE;color: white;font-weight: bold;padding: 5px;border-color:gray" />
        </form>
    </div>
    <div style="margin:auto;width:70%;text-align:right">
    <img src= "http://www.picgifs.com/graphics/w/winnie-the-pooh/graphics-winnie-the-pooh-229897.gif"  height="200" width="300"/>
    </div>
    </div>    
    """        


@post ('/yaaraq4/')
def after_fourth_question():
    num  = request.forms.get("philosof")
    add_to_list(int(num)-1) 
    return """
    <div style="background-color:#EC7B28;height:100%">
    <div style="margin:auto;width:50%;font-family:'Verdana';padding-top:30px">
    <h1 style="text-align:left">And a last sentence to make this world a better place:</h1><h3> Which of the following sentences best describes your attitude?</h3>
        <form name="mypage" method="post" action="/yaarasol/">
        <div style="padding-bottom:8px"><input type="radio" name="philosof" value="1">Don't underestimate the value of doing nothing, of just going along,<div style="padding-left:20px"> listening to all the things you can't hear,and not bothering.</div></div>
        <div style="padding-bottom:8px"><input type="radio" name="philosof" value="2">It is better to be beautiful than to be good. But, it is better to be good <div style="padding-left:20px">than to be ugly.</div></div>
        <div style="padding-bottom:8px"><input type="radio" name="philosof" value="3">Good friends, good books and a sleepy conscience -this is the ideal life. <div style="padding-left:20px">The notion of the rich that the poor are happier is no more foolish than the notion of the poor that the rich are.</div></div>
        <div style="padding-bottom:8px"><input type="radio" name="philosof" value="4">The world would be a happier place, if men had the same capacity to be <div style="padding-left:20px">silent as their ability to speak.</div></div>
         <input name="submit" input type="submit" value="Submit" style="margin-top: 15px;background-color: #6C1CAE;color: white;font-weight: bold;padding: 5px;border-color:gray" />
        </form>
    </div>
    <div style="margin:auto;width:70%;text-align:right">
    <img src= "http://www.picgifs.com/glitter-gifs/u/unicorn/picgifs-unicorn-5109450.gif"  height="100" width="200"/>
    </div>
    </div>    
    """            

        

@post ('/yaarasol/')
def after_sec_question():
    num  = request.forms.get("philosof")
    add_to_list(int(num)-1)
    image_num = get_max_index()
    if image_num == 0 :
            return """
            <div style="background-image:url(https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT3wTqVgubKjrE51oZ1thDN_iSsNtbWPMgKEI2TdxikjShqqjcS);height:100%">
            <div style="margin:auto;width:50%;font-family:'Verdana';padding-top:30px">
            <h3 style="text-align:left">Your opinions are similiar to the spirit of....</h3><h1>Winnie the Pooh</h1> 
            <img src= "http://t0.gstatic.com/images?q=tbn:ANd9GcQp75TdxYb_H9MtI_pZqrdwVT0OYjFfeJAuDHXbBhAmWQMhO3jm1g" alt="Winnie the Pooh" />
            <p> <b>Pooh</b> 's tip for you: <br> You can't stay in your corner of the Forest waiting for others to come to you. You have to go to them sometimes...</p>
            </div>
            </div> 
            """
    elif image_num == 1:
            return """
            <div style="background-image:url(https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT3wTqVgubKjrE51oZ1thDN_iSsNtbWPMgKEI2TdxikjShqqjcS);height:100%">
            <div style="margin:auto;width:50%;font-family:'Verdana';padding-top:30px">
            <h3 style="text-align:left">Your opinions are similiar to the spirit of....</h3><h1>Oscar Wilde</b> <br> </h1>
            <img src= "http://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Oscar_Wilde_portrait.jpg/150px-Oscar_Wilde_portrait.jpg" alt="Oscar Wilde" />
            <p> <b>Oscar Wilde</b> 's tip for you: <br> Education is an admirable thing, but it is well to remember from time to time that nothing that is worth knowing can be taught.
            </div>
            </div> 
            """
    elif image_num == 2:
            return """
            <div style="background-image:url(https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT3wTqVgubKjrE51oZ1thDN_iSsNtbWPMgKEI2TdxikjShqqjcS);height:100%">
            <div style="margin:auto;width:50%;font-family:'Verdana';padding-top:30px">
            <h3 style="text-align:left"> Your opinions are similiar to the spirit of....</h3><h1>Mark Twain </h1>
            <img src= "http://southernmemoriesandupdates.com/wp-content/uploads/2011/05/2011-01-23-Mark-Twain-300x222.jpg" alt="Mark Twain" />
            <p> <b>Mark Twain</b> 's tip for you : <br> Don't go around saying the world owes you a living. <br>The world owes you nothing. It was here first.</br>
            </div>
            </div> 
            """
    elif image_num == 3:
            return """
            <div style="background-image:url(https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT3wTqVgubKjrE51oZ1thDN_iSsNtbWPMgKEI2TdxikjShqqjcS);height:100%">
            <div style="margin:auto;width:50%;font-family:'Verdana';padding-top:30px">
            <h3 style="text-align:left"> Your opinions are similiar to the spirit of....</h3><h1>Baruch Spinoza</h1>
            <img src= "http://capone.mtsu.edu/rbombard/RB/Images/spinoza1.jpg" alt="Baruch Spinoza" />
            <p> <b>Baruch Spinoza</b> 's tip for you : <br> The highest activity a human being can attain is learning for understanding, because to understand is to be free.
            </div>
            </div> 
            """
    else:
        return """
            <img src= "http://i.stack.imgur.com/3mwxc.png" alt="Smiley face" />
            """

application = default_app()
