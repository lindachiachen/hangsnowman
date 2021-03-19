#
# CS 177 - project3.py
# Jia-Lin Chen and Susan Lam
# This program display a word guess game. Besides fulfilling all the requirment from project 2,
#   our enhancements are HARD and EASY mode, a bonus game for players to get a higher score,
#   a chance to guess the whole word when nearly loosing, and a winter theme.
#
 

from graphics import *
import random
from time import sleep
import time

# welcome() function
def controlP():
    # make the welcome window
    wel = GraphWin('Welcome to', 250, 250)
    wel.setBackground('light grey')
    # the header
    head = Rectangle(Point(0,0), Point(250, 16))
    head.setFill('black')
    head.draw(wel)
    entry = Text(Point(125,9), 'GUESS MASTER 2.0')
    entry.setStyle('bold')
    entry.setTextColor('gold')
    entry.draw(wel)
    # game discription
    dis = Rectangle(Point(20,70), Point(230, 140))
    dis.setFill('white')
    dis.draw(wel)
    text1 = Text(Point(125, 90), 'This is a game where your score is ')
    text2 = Text(Point(125, 105), 'based on the number of 4-8 letter ')
    text3 = Text(Point(125, 120), 'words you can guess within 10 tries.')
    text1.setSize(9)
    text2.setSize(9)
    text3.setSize(9)
    text1.draw(wel)
    text2.draw(wel)
    text3.draw(wel)
    # new button
    new = Rectangle(Point(15, 30), Point(55, 55))
    new.setFill('gold')
    new.draw(wel)
    n = Text(Point(35, 43), 'NEW')
    n.draw(wel)
    # quit button
    quitb = Rectangle(Point(195, 30), Point(235, 55))
    quitb.setFill('black')
    quitb.draw(wel)
    q = Text(Point(216,43), 'QUIT')
    q.setTextColor('gold')
    q.draw(wel)
    # instruction
    instruction = Text(Point(125, 165), 'Click NEW to start a game...')
    instruction.draw(wel)
 
    # hint button
    hintb = Rectangle(Point(105, 30), Point(145, 55))
    hintb.setFill('red')
    hintb.draw(wel)
    h = Text(Point(125,43), 'HINT')
    h.setTextColor('white')
    h.draw(wel)
 
    #create high score button
    highscore = Rectangle(Point(65,200),Point(185,230))
    highscore.setFill('light blue')
    highscore.draw(wel)
    high_mes = Text(Point(125,215),'HIGH SCORES')
    high_mes.draw(wel)
 
    return wel
 
 
# define the hint funciton
def hint(circles, chosen_word, all_alphabet, characters, chosen_char):
    letter = set(list(chosen_word))
    alphabet = []
    for i in range(65,91):
        alphabet.append(chr(i))
    wrong_letters = []
    for f in letter:
        alphabet.remove(f)
        wrong_letters.append(f)
    chosen_char = set(chosen_char)

    for i in chosen_char:
        alphabet.remove(i)

    choose = []
    for i in range(0,3):
        choose.append(random.choice(alphabet))
 
    for h in choose:
        circles[ord(h)-65].setFill('gold')
        characters[ord(h)-65].setFill('black')

    return alphabet

 
 
 
# def game panel:
def game_panel(score, rounds):
    # create the window
    win = GraphWin('Save the Block P',500, 500)
    win.setBackground('gold')
    # creating the circles
    circles = []
    for i in range(75, 465, 30):
        c = Circle(Point(i, 425), 15)
        c.setFill('black')
        c.draw(win)
        circles.append(c)
    for i in range(75, 465, 30):
        c = Circle(Point(i, 455), 15)
        c.setFill('black')
        c.draw(win)
        circles.append(c)
  
    # A to Z
    # drawing it in the game window
    char = ['A', 'B', 'C', 'D', 'E', 'F','G','H', 'I', 'J', 'K', 'L', 'M']
    G = 0
    characters = []
    for i in range(75, 465, 30):
        ch = Text(Point(i, 425), char[G])
        ch.setTextColor('white')
        ch.setSize(12)
        ch.draw(win)
        characters.append(ch)
        G+=1
       
    char2 = ['N', 'O', 'P', 'Q', 'R', 'S','T','U', 'V', 'W', 'X', 'Y', 'Z']
    F = 0
    for i in range(75, 465, 30):
        ch2 = Text(Point(i, 455), char2[F])
        ch2.setTextColor('white')
        ch2.setSize(12)
        ch2.draw(win)
        characters.append(ch2)
        F+=1
 
    # the middle polygon of the p
    P11 = Polygon(Point(225,220), Point(265, 220),Point(260, 260), Point(220, 260))
    P11.setFill('gold')
    P11.draw(win)
    # P outline
    Pw4 = Polygon(Point(185,220), Point(225, 220),Point(220, 260), Point(180, 260))
    Pw4.setFill('white')
    Pw4.draw(win)
    Pw8 = Polygon(Point(265,220), Point(305, 220),Point(300, 260), Point(260, 260))
    Pw8.setFill('white')
    Pw8.draw(win)
    Pw5 = Polygon(Point(190,180), Point(230, 180),Point(225, 220), Point(185, 220))
    Pw5.setFill('white')
    Pw5.draw(win)
    Pw6 = Polygon(Point(230,180), Point(270, 180),Point(265, 220), Point(225, 220))
    Pw6.setFill('white')
    Pw6.draw(win)
    Pw7 = Polygon(Point(270,180), Point(310, 180),Point(305, 220), Point(265, 220))
    Pw7.setFill('white')
    Pw7.draw(win)
    Pw3 = Polygon(Point(180,260), Point(220, 260),Point(215, 300), Point(175, 300))
    Pw3.setFill('white')
    Pw3.draw(win)
    Pw10 = Polygon(Point(220,260), Point(260, 260),Point(255, 300), Point(215, 300))
    Pw10.setFill('white')
    Pw10.draw(win)
    Pw9 = Polygon(Point(260,260), Point(300, 260),Point(295, 300), Point(255, 300))
    Pw9.setFill('white')
    Pw9.draw(win)
    Pw2 = Polygon(Point(175,300), Point(215, 300),Point(210, 340), Point(170, 340))
    Pw2.setFill('white')
    Pw2.draw(win)
    Pw1 = Polygon(Point(160,340), Point(220, 340),Point(215, 370), Point(155, 370))
    Pw1.setFill('white')
    Pw1.draw(win)
    # black polygon fill
    P4 = Polygon(Point(185,220), Point(225, 220),Point(220, 260), Point(180, 260))
    P4.setFill('black')
    P4.draw(win)
    P8 = Polygon(Point(265,220), Point(305, 220),Point(300, 260), Point(260, 260))
    P8.setFill('black')
    P8.draw(win)
    P5 = Polygon(Point(190,180), Point(230, 180),Point(225, 220), Point(185, 220))
    P5.setFill('black')
    P5.draw(win)
    P6 = Polygon(Point(230,180), Point(270, 180),Point(265, 220), Point(225, 220))
    P6.setFill('black')
    P6.draw(win)
    P7 = Polygon(Point(270,180), Point(310, 180),Point(305, 220), Point(265, 220))
    P7.setFill('black')
    P7.draw(win)
    P3 = Polygon(Point(180,260), Point(220, 260),Point(215, 300), Point(175, 300))
    P3.setFill('black')
    P3.draw(win)
    P10 = Polygon(Point(220,260), Point(260, 260),Point(255, 300), Point(215, 300))
    P10.setFill('black')
    P10.draw(win)
    P9 = Polygon(Point(260,260), Point(300, 260),Point(295, 300), Point(255, 300))
    P9.setFill('black')
    P9.draw(win)
    P2 = Polygon(Point(175,300), Point(215, 300),Point(210, 340), Point(170, 340))
    P2.setFill('black')
    P2.draw(win)
    P1 = Polygon(Point(160,340), Point(220, 340),Point(215, 370), Point(155, 370))
    P1.setFill('black')
    P1.draw(win)
 
    # store polygon in list
    polylist = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]
 
    # choose a seceret word
    # open the words.txt data file and read the words from file
    f= open('words.txt', 'r').read()
   
    # randomly choose one word
    string = ''
    for line in f:
        string += line
    word = string.split()
  
    import random
    chosen_word = random.choice(word)
 
    # create the gold block placeholder
    list_of_placeholder =[]
    if len(chosen_word)== 4:
        for g in range(150, 301, 50):
            placeholder = Rectangle(Point(g,50), Point(g+50, 100))
            placeholder.setFill('gold')
            placeholder.draw(win)
            list_of_placeholder.append(placeholder)
    if len(chosen_word)== 5:
        for g in range(125, 326, 50):
            placeholder = Rectangle(Point(g,50), Point(g+50, 100))
            placeholder.setFill('gold')
            list_of_placeholder.append(placeholder)
            placeholder.draw(win)
    if len(chosen_word)== 6:
        for g in range(100, 351, 50):
            placeholder = Rectangle(Point(g,50), Point(g+50, 100))
            placeholder.setFill('gold')
            list_of_placeholder.append(placeholder)
            placeholder.draw(win)
 
    #score display
    SCORE = Text(Point(250,25), 'SCORE: '+ str(score))
    SCORE.setSize(19)
    SCORE.draw(win)
 
    # round display
    ROUNDS = Text(Point(55,20),'ROUND: '+str(rounds))
    ROUNDS.setSize(15)
    ROUNDS.draw(win)
   
    return win, circles, polylist, chosen_word, characters,list_of_placeholder, SCORE, ROUNDS
 

 
 
 
# define the snowman function when lost the game (winter theme)
#   enhancement
def snowman(game_window):
    base = Oval(Point(140,130),Point(360,200))
    base.draw(game_window)
    base.setFill('white')
    base.setOutline('white')
    car = Polygon(Point(270,170),Point(270,180),Point(290,175))
    car.draw(game_window)
    car.setFill('orange')
    car.setOutline('orange')
    base1 = Oval(Point(110,190),Point(180,210))
    base1.draw(game_window)
    base1.setFill('white')
    base1.setOutline('white')
    base2 = Oval(Point(170,200),Point(200,210))
    base2.draw(game_window)
    base2.setOutline('white')
    base2.setFill('white')
    base3 = Oval(Point(325,163),Point(400,200))
    base3.draw(game_window)
    base3.setOutline('white')
    base3.setFill('white')
    base4 = Oval(Point(290,190),Point(340,207))
    base4.draw(game_window)
    base4.setOutline('white')
    base4.setFill('white')
    e1 = Circle(Point(200,150),5)
    e1.setFill('black')
    e1.draw(game_window)
    e2 = Circle(Point(316,160),5)
    e2.setFill('black')
    e2.draw(game_window)
    s1 = Line(Point(95,205),Point(170,195))
    s1.draw(game_window)
    s1.setFill('brown')
    s1.setWidth(3)
    s2 = Line(Point(110,205),Point(97,194))
    s2.draw(game_window)
    s2.setFill('brown')
    s2.setWidth(3)
    s3 = Line(Point(110,202),Point(99,219))
    s3.draw(game_window)
    s3.setFill('brown')
    s3.setWidth(3)
    s4 = Line(Point(360,180),Point(420,190))
    s4.draw(game_window)
    s4.setFill('brown')
    s4.setWidth(3)
    s5 = Line(Point(395,186),Point(427,210))
    s5.draw(game_window)
    s5.setFill('brown')
    s5.setWidth(3)
    s6 = Line(Point(120,190),Point(143,200))
    s6.draw(game_window)
    s6.setFill('brown')
    s6.setWidth(3)
    h1 = Oval(Point(120,95),Point(200,125))
    h1.draw(game_window)
    h1.setFill('black')
    h1.setOutline('red')
    h2 = Rectangle(Point(135,65),Point(185,110))
    h2.draw(game_window)
    h2.setFill('black')
    h3 = Rectangle(Point(135,105),Point(185,112))
    h3.draw(game_window)
    h3.setFill('green')
    h3.setOutline('green')
 
 
# define the snowman function
#   enhancement
def nice_snowman(game_window):
    # stick arms
    e1 = Line(Point(260,150),Point(175,130))
    e1.setFill('brown')
    e1.setWidth(3)
    e1.draw(game_window)
    e2 = Line(Point(270,150),Point(315,130))
    e2.setFill('brown')
    e2.setWidth(3)
    e2.draw(game_window)
    e3 = Line(Point(180,140),Point(195,120))
    e3.setFill('brown')
    e3.setWidth(3)
    e3.draw(game_window)
    e3 = Line(Point(300,135),Point(330,140))
    e3.setFill('brown')
    e3.setWidth(3)
    e3.draw(game_window)
    # body
    c1 = Circle(Point(250,210),50)
    c1.setFill('white')
    c1.setOutline('white')
    c1.draw(game_window)
    c2= Circle(Point(250,140),36)
    c2.setFill('white')
    c2.setOutline('white')
    c2.draw(game_window)
    c3= Circle(Point(250,90),24)
    c3.setFill('white')
    c3.setOutline('white')
    c3.draw(game_window)
    d1 = Oval(Point(170,250),Point(330,270))
    d1.setFill('white')
    d1.setOutline('white')
    d1.draw(game_window)
    # black dots
    c4 = Circle(Point(240,85),3)
    c4.setFill('black')
    c4.draw(game_window)
    c5 = Circle(Point(260,85),3)
    c5.setFill('black')
    c5.draw(game_window)
    c6 = Circle(Point(250,125),3)
    c6.setFill('black')
    c6.draw(game_window)
    c7 = Circle(Point(250,140),3)
    c7.setFill('black')
    c7.draw(game_window)
    c8 = Circle(Point(250,155),3)
    c8.setFill('black')
    c8.draw(game_window)
    # carrot nose
    car1 = Polygon(Point(250,93),Point(250,98),Point(259,96))
    car1.setFill('orange')
    car1.setOutline('orange')
    car1.draw(game_window)
    # scarf
    s1 = Rectangle(Point(228,105),Point(273,112))
    s1.setFill('green')
    s1.setOutline('green')
    s1.draw(game_window)
    s2 = Line(Point(270,112),Point(275,134))
    s2.setFill('green')
    s2.setWidth(9)
    s2.draw(game_window)
    #hat
    r1= Rectangle(Point(230,65),Point(270,70))
    r1.setFill('black')
    r1.draw(game_window)
    r2 = Rectangle(Point(235,45),Point(265,65))
    r2.setFill('black')
    r2.draw(game_window)
    r3 = Rectangle(Point(235,60),Point(265,64))
    r3.setFill('red')
    r3.setOutline('red')
    r3.draw(game_window)
 
#def levels function
def levels():
    level = GraphWin('Levels',250,150)
    level.setBackground('#9c7fd6')
    # rectangles
    z1 = Rectangle(Point(15,15),Point(115,135))
    z1.setFill('green')
    z1.setOutline('green')
    z1.draw(level)
    z2 = Rectangle(Point(135,15),Point(235,135))
    z2.setFill('#ff4500')
    z2.setOutline('#ff4500')
    z2.draw(level)
    # easy and hard text
    z3 = Text(Point(65,55),'EASY')
    z3.draw(level)
    z3.setFill('white')
    z3.setSize(16)
    z4 = Text(Point(185,55),'HARD')
    z4.draw(level)
    z4.setFill('white')
    z4.setSize(16)
    easy = Text(Point(65,75),'get one hint!')
    easy.setTextColor('white')
    easy.setSize(13)
    easy.draw(level)
    hard = Text(Point(185,75),'no hints and deduct ')
    hard.setTextColor('white')
    hard.setSize(10)
    hard.draw(level)
    hard2 = Text(Point(185,85),'2 points at a time!')
    hard2.setTextColor('white')
    hard2.setSize(10)
    hard2.draw(level)
    return level
   
 
# define the sort
def sort_it(myList):
    # makes the score an integar
    for i in range(0, len(myList)):
        myList[i][2]=int(myList[i][2])
    # sort the score list
    myList.sort(key = lambda x: x[2], reverse = True)
    #print(myList)
    return myList
 
 
           
# define highscore functio
def highscore():
    # create the window
    high = GraphWin("High Scores", 250,200)
    high.setBackground("white")
    # read the score file
    hi = open("scores.txt",'r')
    hi = hi.readlines()
    # make it into a list of lists
    myList = [i.strip('\n').split(',') for i in hi]
    # call the sort_it function
    myList = sort_it(myList)
    # create the title
    title = Text(Point(125,10),'{0:<12}{1:^12}{2:>15}'.format('Player','Rounds','Score'))
    border = Text(Point(125,20),'=-'*25)
    title.draw(high)
    border.draw(high)
 
    k = 0
    high_list = []
    # draw the names, rounds, scores
    for i in range(35,160,20):
        nice = Text(Point(50,i),'{0:<14}'.format(myList[k][0]))
        nice2 = Text(Point(120,i),'{0:^15}'.format(myList[k][1]))
        nice2.draw(high)
        nice3 = Text(Point(200,i),'{0:>13}'.format(myList[k][2]))
        nice3.draw(high)
        nice.draw(high)
        high_list.append(nice)
        high_list.append(nice2)
        high_list.append(nice3)
        k+=1
        #print(k)
       
    # moving the text up, scrolling
    M = True
    while M!=False:
        title.move(0, -3)
        border.move(0, -3)
        sleep(0.23) 
        if title.getAnchor().getY()<0:
            title.move(0,220)
 
        if border.getAnchor().getY()<0:
            border.move(0, 220)
 
        for i in high_list:
            i.move(0,-3)
            if i.getAnchor().getY()<0:
                i.move(0,220)
               
        # clicking the window to close it
        scoreclose = high.checkMouse()
        if scoreclose!=None:
            M = False
            high.close()
 
from random import randint, choice
 
# bonus round
def bonus(game_window, circles, polylist, chosen_word, characters, list_of_placeHolder, SCORE, ROUNDS, score,failed_times,succeeded_times,hints,rounds):
    mini = GraphWin('BONUS ROUND',400,400)
    mini.setBackground('white')
    colors = ['light blue','orange','yellow','light green','#bdacd1','pink']
    rec = Rectangle(Point(0,0),Point(400,75))
    rec.setFill('black')
    rec.draw(mini)
    T1 = Text(Point(200,20),'FIND THE GRAY CIRCLE TO WIN THIS')
    T2 = Text(Point(200,50),'MINI GAME AND EARN 5 BONUS POINTS!')
    T1.setSize(14)
    T2.setSize(14)
    T1.setFill('white')
    T2.setFill('white')
    T1.draw(mini)
    T2.draw(mini)
    
    # make the circles
    circles_list = []
    for i in range(0,600):
        cir = Circle(Point(randint(10,390),randint(75,390)), randint(10,20))
        cir.setFill(choice(colors))
        cir.setOutline(choice(colors))
        cir.draw(mini)
        circles_list.append(cir)

    # make the grey circle
    gray = Circle(Point(randint(5,190),randint(115,340)),7)
    gray.setFill('light gray')
    gray.setOutline('light gray')
    gray.draw(mini)
    center = gray.getCenter()
    #print(center)
    rec1 = Rectangle(Point(40,350),Point(365,380))
    rec1.setFill('red')
    rec1.draw(mini)
    T3 = Text(Point(200,365),"CAN'T FIND IT... SKIP TO NEXT ROUND")
    T3.draw(mini)
    T3.setSize(13)

    # play the game
    ope = True
    while ope ==True:
        circle_click = mini.checkMouse()
        if circle_click != None:
            center = gray.getCenter()
            X4 = circle_click.getX()
            Y4 = circle_click.getY()
            dx = X4 - center.getX()
            dy = Y4 - center.getY()
            dist = (dx*dx + dy*dy)**0.5

            # if found the grey circle
            if dist <= gray.getRadius():
               
                mini.close()
                ope = False
                return 1

            # if want to skip bonus
            if 40<X4<365 and 350<Y4<380:
               
                mini.close()
                ope = False
                return 2

 
# drop function
def drop(polygon):
    polygon.setFill('red')
    d_total = 0
    while d_total<=500:
        polygon.move(0, 10)
        sleep(0.01)
        d_total+=10
 
 
# main function
def main():
    # intialize the variables
    score = 10
    rounds=1
    control_window  = controlP()
    failed_times = 0
   
    #succeeded_times = 0
    indicator1 = True
    indicator2 = True
    #indicator3 = True
    all_alphabet = []
    for i in range(65,91):
        all_alphabet.append(chr(i))
 
    while indicator1 ==True:
        all_alphabet = []
        for i in range(65,91):
            all_alphabet.append(chr(i))
        start_click  = control_window.checkMouse()
        indicator2 = True
        failed_times = 0
        succeeded_times = 0
       
        # detect clicks
        if start_click != None:
            x0 = start_click.getX()
            y0 = start_click.getY()

            # click high score
            if 65<x0<185 and 200<y0<230:
                highscore()
 
            # click new button
            if 15<=x0<=55 and 30<=y0<=55:

                # call level function
                level = levels()

                level_click= level.getMouse()
                # detect clicks
                if level_click != None:
                    x8 = level_click.getX()
                    y8 = level_click.getY()
                    
                    # click easy button
                    if 15<x8<115 and 15<y8<135:

                        # start the program
                        level.close()
                        hints = 1
                        score = 10
                        game_window, circles, polylist, chosen_word, characters, list_of_placeHolder, SCORE, ROUNDS = game_panel(score, rounds)
                        HINT = Text(Point(450,20), 'HINTS: '+str(hints))
                        HINT.setSize(15)
                        HINT.draw(game_window)
                        print(chosen_word)
                        chosen_char = []

                        # game while loop
                        while indicator2==True:
 
                            control_click = control_window.checkMouse()
                            input_click = game_window.checkMouse()
                            
   
                            
                            # check clicks
                            if input_click!= None:
                                x1 = input_click.getX()
                                y1 = input_click.getY()

                                # click circles
                                for i in range(0,26):
                                    xc = circles[i].getCenter().getX()
                                    yc = circles[i].getCenter().getY()
                                    d = ((x1-xc)**2 + (y1-yc)**2)**0.5
                                   
                                    if d<15:
                                        # changing the color of the circles when clicked
                                        circles[i].setFill('gold')
                                        characters[i].setFill('black')
                                        guessed_character = all_alphabet[i]
                                        
                                        # if presssed right character
                                        if guessed_character in chosen_word:
                                            for i in range(len(chosen_word)):

                                                # changing the placeholder to the correct letter
                                                if guessed_character==chosen_word[i]:
                                                    display = Text(list_of_placeHolder[i].getCenter(),guessed_character)
                                                    display.setFill('black')
                                                    display.setSize(20)
                                                    display.setStyle('bold')
                                                    display.draw(game_window)
                                                    succeeded_times+=1
                                                   
                                            # the word is guessed completely
                                            if succeeded_times==len(chosen_word):
                                                # snowman appears and Congrats
                                                t = Rectangle(Point(100,40),Point(400,370))
                                                t.setFill('light blue')
                                                t.setOutline('light blue')
                                                t.draw(game_window)
                                                nice_snowman(game_window)
                                                m = Text(Point(250,290),'You Win, Boiler up!')
                                                m.setSize(24)
                                                m.setFill('gray')
                                                m.setStyle('bold')
                                                m3 = Text(Point(250,325),'The Word was '+chosen_word.title()+'!')
                                                m3.setSize(18)
                                                m3.draw(game_window)
                                                m3.setFill('gray')
                                                m3.setStyle('bold')
                                                m2 = Text(Point(250,355),'Click to Continue')
                                                m2.setFill('gray')
                                                m2.setStyle('bold')
                                                m2.setStyle('italic')
                                                m2.draw(game_window)
                                                score +=10
                                                failed_times =0
                                                succeeded_times=0
                                                rounds+=1
                                                hints = 1
                                                m.draw(game_window)
                                                # change the background to indicate that
                                                #   the round is coming next (celebration)
                                                game_window.setBackground('red')
                                                sleep(.1)
                                                game_window.setBackground('green')
                                                sleep(.1)
                                                game_window.setBackground('magenta')
                                                sleep(.1)
                                                game_window.setBackground('cyan')
                                                sleep(.1)
                                                game_window.setBackground('orange')
                                                sleep(.1)
                                                game_window.setBackground('purple')
                                                sleep(.1)
                                                game_window.setBackground('gold')
                                                sleep(.1)
                                                # get the mouse to go to the next round
                                                game_window.getMouse()
                                                game_window.close()
                                               
                                                # call the game_panel function
                                                game_window, circles, polylist, chosen_word, characters, list_of_placeHolder, SCORE, ROUNDS = game_panel(score, rounds)
                                                HINT = Text(Point(450,20), 'HINTS: '+str(hints))
                                                HINT.setSize(15)
                                                HINT.draw(game_window)
                                                chosen_char = []
                                                
                                                print(chosen_word)

                                                
                                                # pop up bonus game 
                                                for i in range(3, 101, 2):
                                                    
                                                    if rounds == i:
                                                        
                                                        game_window.close()
                                                        bonusgame = bonus(game_window, circles, polylist, chosen_word, characters, list_of_placeHolder, SCORE, ROUNDS, score,failed_times,succeeded_times,hints,rounds)

                                                        # if won the game
                                                        if bonusgame == 1:
                                                            score +=5
                                                            #print(rounds)
                                                            game_window, circles, polylist, chosen_word, characters, list_of_placeHolder, SCORE, ROUNDS = game_panel(score, rounds)
                                                            HINT = Text(Point(450,20), 'HINTS: '+str(hints))
                                                            HINT.setSize(15)
                                                            HINT.draw(game_window)
                                                            failed_times =0
                                                            succeeded_times=0
                                                            hints = 1
                                                            chosen_char = []
                                                            
                                                            print(chosen_word)

                                                        # if skip the game
                                                        elif bonusgame == 2:
                                                            game_window, circles, polylist, chosen_word, characters, list_of_placeHolder, SCORE, ROUNDS = game_panel(score, rounds)
                                                            HINT = Text(Point(450,20), 'HINTS: '+str(hints))
                                                            HINT.setSize(15)
                                                            HINT.draw(game_window)
                                                            failed_times =0
                                                            succeeded_times=0
                                                            hints = 1
                                                            chosen_char = []
                                                        
                                                            print(chosen_word)
               
                                           
                                    
                                        # pressed wrong charater
                                        elif guessed_character not in chosen_word:
                                            drop(polylist[failed_times])
                                            guessed_char = guessed_character
                                            chosen_char.append(guessed_char)

                                            #print(failed_times)
                                            score-=1
                                            SCORE.setText('SCORE: '+str(score))
                                            # pop up two chance to guess the whole word when failed 7 times
                                            if 7<=failed_times<9:
                                                
                                                enhance = Oval(Point(100,150), Point(400,300))
                                                enhance.setFill('light blue')
                                                enhance.setOutline('light blue')
                                                enhance.draw(game_window)
                                                H = Text(Point(250, 185), 'FEELING LUCKY?')
                                                H.setSize(24)
                                                H.setStyle('bold')
                                                H.setTextColor('red')
                                                H.setFace('courier')
                                                H.draw(game_window)
                                                M = Text(Point(250, 210), 'Guess a word to win ')
                                                M.setTextColor('white')
                                                M.setFace('courier')
                                                M.setSize(20)
                                                M.draw(game_window)
                                                M2 = Text(Point(250, 235), 'this round immediately!')
                                                M2.setTextColor('white')
                                                M2.setFace('courier')
                                                M2.setSize(20)
                                                M2.draw(game_window)
                                                guess = Entry(Point(250, 270), 7)
                                                guess.setFill('white')
                                                guess.draw(game_window)
                                                B = Circle(Point(300,270), 15)
                                                B.setFill('red')
                                                B.setOutline('red')
                                                B.draw(game_window)
                                                B2 = Text(Point(300,271), 'GO!')
                                                B2.setSize(11)
                                                B2.draw(game_window)
                                                R1 = Rectangle(Point(145,310),Point(355,340))
                                                R1.setFill('purple')
                                                R1.setOutline('purple')
                                                R1.draw(game_window)
                                                R2 = Text(Point(250,325),"NO, I'M NOT FEELING IT!")
                                                R2.setFill('white')
                                                R2.setStyle('bold')
                                                R2.draw(game_window)
                                                
                                                
                                                go_click = game_window.getMouse()
                                                if go_click != None:
                                                    X3 = go_click.getX()
                                                    Y3 = go_click.getY()

                                                    # dont want to guess word
                                                    if 145<X3<355 and 310<Y3<340:
                                                        H.undraw()
                                                        enhance.undraw()
                                                        M.undraw()
                                                        M2.undraw()
                                                        guess.undraw()
                                                        B.undraw()
                                                        B2.undraw()
                                                        R1.undraw()
                                                        R2.undraw()
                                   
                                                    # pressed GO to guess word
                                                    x= B.getCenter()
                                                    dx = X3 - x.getX()
                                                    dy = Y3 - x.getY()
                                                    dist = (dx*dx + dy*dy)**0.5
                                                    if dist <= B.getRadius():
                                                        guessword = guess.getText()

                                                        # if guessed right
                                                        if guessword.upper() == chosen_word:
                                                            guess.undraw()
                                                            t = Rectangle(Point(100,40),Point(400,345))
                                                            t.setFill('light blue')
                                                            t.setOutline('light blue')
                                                            t.draw(game_window)
                                                            nice_snowman(game_window)
                                                            m = Text(Point(250,290),'You Win, Boiler up!')
                                                            m.setSize(24)
                                                            m.setFill('gray')
                                                            m.setStyle('bold')
                                                            m2 = Text(Point(250,325),'Click to Continue')
                                                            m2.setFill('gray')
                                                            m2.setStyle('bold')
                                                            m2.setStyle('italic')
                                                            m2.draw(game_window)
                                                            score +=10
                                                           
                                                            succeeded_times=0
                                                            rounds+=1
                                                            hints = 1
                                                            m.draw(game_window)
                                                            # change the background to indicate that
                                                            #   the round is coming next (celebration)
                                                            game_window.setBackground('red')
                                                            sleep(.1)
                                                            game_window.setBackground('green')
                                                            sleep(.1)
                                                            game_window.setBackground('magenta')
                                                            sleep(.1)
                                                            game_window.setBackground('cyan')
                                                            sleep(.1)
                                                            game_window.setBackground('orange')
                                                            sleep(.1)
                                                            game_window.setBackground('purple')
                                                            sleep(.1)
                                                            game_window.setBackground('gold')
                                                            sleep(.1)
                                                            game_window.getMouse()
                                                            game_window.close()
                                                            game_window, circles, polylist, chosen_word, characters, list_of_placeHolder, SCORE, ROUNDS = game_panel(score, rounds)
                                                            HINT = Text(Point(450,20), 'HINTS: '+str(hints))
                                                            HINT.setSize(15)
                                                            HINT.draw(game_window)
                                                            failed_times = -1
                                                            chosen_char = []
                                                           
                                                            print(chosen_word)
                                                            
                                                           
                                                        # when guess wrong 
                                                        else:
                                                            enhance.undraw()
                                                            H.undraw()
                                                            B.undraw()
                                                            B2.undraw()
                                                            M.undraw()
                                                            M2.undraw()
                                                            R1.undraw()
                                                            R2.undraw()
                                                            guess.undraw()
                                                            for i in range(2):
                                                                failed_times+=1
                                                                drop(polylist[failed_times])
                                                                score-=1
                                                                SCORE.setText('SCORE: '+str(score))
                                                            
 
                                            # losing the game completely
                                            if failed_times == 9:
                                                
                                                w = Rectangle(Point(85,55),Point(440,230))
                                                w.draw(game_window)
                                                w.setFill('light blue')
                                                w.setOutline('light blue')
                                                # call the snowman function
                                                #   enhancement
                                                snowman(game_window)
                                                lose_infor = Text(Point(250,250),'You lose, better luck next time')
                                                lose_infor.setSize(20)
                                                lose_infor.setFill('red')
                                                lose_infor.setStyle('bold')
                                                lose_infor.draw(game_window)
                                                m5 = Text(Point(250,310),'The Word was '+chosen_word.title()+'...')
                                                m5.setSize(18)
                                                m5.draw(game_window)
                                                m5.setFill('red')
                                                m5.setStyle('bold')
                                                # prompt user for name
                                                myEntry= Entry(Point(340,280),8)
                                                myEntry.setFill('white')
                                                myEntry.draw(game_window)
                                                mes = Text(Point(210,280),'Enter your name:')
                                                mes.setTextColor('red')
                                                mes.setStyle('bold')
                                                mes.setSize(14)
                                                mes.draw(game_window)
                                                # create save button
                                                save = Rectangle(Point(380,270),Point(430,290))
                                                save.setFill('red')
                                                save.draw(game_window)
                                                save_mes = Text(Point(405,280),"SAVE")
                                                save_mes.draw(game_window)
                                                # store the in score file
 
                                                # get mouse click for save button
                                                save_click = game_window.getMouse()
                                                x4 = save_click.getX()
                                                y4 = save_click.getY()
                                                if 380<x4<430 and 270<y4<290:
                                                    # open file and write the name and scores
                                                    f = open('scores.txt','a')
                                                    name = myEntry.getText()
                                                    f.write('\n'+name+','+str(rounds)+','+str(score-1))
                                                    # close file
                                                    f.close()
                                                    game_window.close()
                                                    indicator2=False
                                            failed_times+=1

                            
                            # detect click
                            if control_click != None:
                                x3 = control_click.getX()
                                y3 = control_click.getY()

                                # clicking the hint 
                                if 105<=x3<=145 and 30<=y3<=55:
                                    
                                    while hints ==1 and failed_times<=7:
                                        
                                        alphabet = hint(circles, chosen_word, all_alphabet, characters, chosen_char)
                                        #print(alphabet)
                                        for i in range(0,2):
                                            drop(polylist[failed_times])
                                            failed_times +=1
                                        hints -=1  
                                        HINT.setText('HINTS: '+ str(hints))
                            
                                   
 
                                # high score is clicked
                                if 65<x3<185 and 200<y3<230:
                                    highscore()
                                   
                                    
                            
                                # exit during the game
                                if 195<=x3<=235 and 30<= y3<=55:
                                    control_window.close()
                                    game_window.close()
                                    indicator1 = False
                                    indicator2 = False
               

 
                    # if click the HARD button
                    if 135<x8<235 and 15<y8<135:

                        level.close()
                        # no hints for hard mode
                        hints = 0                                   
                        succeeded_times=0
                        score = 10
                        rounds=1                                  
                    
                        # start the game
                        game_window, circles, polylist, chosen_word, characters, list_of_placeHolder, SCORE, ROUNDS = game_panel(score, rounds)
                       
                        print(chosen_word)

                        chosen_char = []
                        while indicator2==True:
                           
                            
                            input_click = game_window.checkMouse()
                            control_click= control_window.checkMouse()
                   
                            # detect the clicks in game
                            if input_click!= None:
                                x1 = input_click.getX()
                                y1 = input_click.getY()

                                # click the circles
                                for i in range(0,26):
                                    xc = circles[i].getCenter().getX()
                                    yc = circles[i].getCenter().getY()
                                    d = ((x1-xc)**2 + (y1-yc)**2)**0.5
                                    
                                    # changing the color of the circles when clicked
                                    if d<15:
                                        circles[i].setFill('gold')
                                        characters[i].setFill('black')
                                        guessed_character = all_alphabet[i]
                                        
 
                                       
                                        # if presssed right character
                                        if guessed_character in chosen_word:
                                            for i in range(len(chosen_word)):
                                                
                                                # changing the placeholder to the correct letter
                                                if guessed_character==chosen_word[i]:
                                                    display = Text(list_of_placeHolder[i].getCenter(),guessed_character)
                                                    display.setFill('black')
                                                    display.setSize(20)
                                                    display.setStyle('bold')
                                                    display.draw(game_window)
                                                    succeeded_times+=1
                                                   
                                            # the word is guessed completely
                                            if succeeded_times==len(chosen_word):
                                                # snowman appears and Congrats
                                                t = Rectangle(Point(100,40),Point(400,370))
                                                t.setFill('light blue')
                                                t.setOutline('light blue')
                                                t.draw(game_window)
                                                nice_snowman(game_window)
                                                m = Text(Point(250,290),'You Win, Boiler up!')
                                                m.setSize(24)
                                                m.setFill('gray')
                                                m.setStyle('bold')
                                                m3 = Text(Point(250,325),'The Word was '+chosen_word.title()+'!')
                                                m3.setSize(18)
                                                m3.draw(game_window)
                                                m3.setFill('gray')
                                                m3.setStyle('bold')
                                                m2 = Text(Point(250,355),'Click to Continue')
                                                m2.setFill('gray')
                                                m2.setStyle('bold')
                                                m2.setStyle('italic')
                                                m2.draw(game_window)
                                                score +=10
                                                failed_times =0
                                                succeeded_times=0
                                                rounds+=1
                                                hints =0
                                                m.draw(game_window)
                                                # change the background to indicate that
                                                #   the round is coming next (celebration)
                                                game_window.setBackground('red')
                                                sleep(.1)
                                                game_window.setBackground('green')
                                                sleep(.1)
                                                game_window.setBackground('magenta')
                                                sleep(.1)
                                                game_window.setBackground('cyan')
                                                sleep(.1)
                                                game_window.setBackground('orange')
                                                sleep(.1)
                                                game_window.setBackground('purple')
                                                sleep(.1)
                                                game_window.setBackground('gold')
                                                sleep(.1)
                                                # get the mouse to go to the next round
                                                game_window.getMouse()
                                                game_window.close()
                                                # call the game_panel function
                                                hints = 0
                                                game_window, circles, polylist, chosen_word, characters, list_of_placeHolder, SCORE, ROUNDS = game_panel(score, rounds)
                                                chosen_char = []
                                                failed_times = 0
                                                #print(chosen_word)

                                                # have bonus game
                                                for i in range(3, 101, 2):
                                                    if rounds == i:
                                                        
                                                        game_window.close()
                                                        bonusgame = bonus(game_window, circles, polylist, chosen_word, characters, list_of_placeHolder, SCORE, ROUNDS, score,failed_times,succeeded_times,hints,rounds)
                                                        # if won the game
                                                        if bonusgame == 1:
                                                            score +=5
                                                            game_window, circles, polylist, chosen_word, characters, list_of_placeHolder, SCORE, ROUNDS = game_panel(score, rounds)
                                                            failed_times =0
                                                            succeeded_times=0
                                                            rounds+=1
                                                            hints = 1
                                                            chosen_char = []
                                                            
                                                            print(chosen_word)

                                                        # if skip the bonus
                                                        elif bonusgame == 2:
                                                            
                                                            game_window, circles, polylist, chosen_word, characters, list_of_placeHolder, SCORE, ROUNDS = game_panel(score, rounds)
                                                            failed_times =0
                                                            succeeded_times=0
                                                            rounds+=1
                                                            hints = 1
                                                            chosen_char = []
                                                        
                                                            print(chosen_word)
                                                
                                       
                                        # pressed wrong charater
                                        elif guessed_character not in chosen_word:

                                            drop(polylist[failed_times])
                                            failed_times+=1
                                            drop(polylist[failed_times])
                                            score-=1
                                            guessed_char = guessed_character
                                            chosen_char.append(guessed_char)
                                            
 
                                            # pop up a chance to guess the word when failed 7 times
                                            if 7<=failed_times<9:
                                                
                                                SCORE.setText('SCORE: '+str(score-1))
                                                enhance = Oval(Point(100,150), Point(400,300))
                                                enhance.setFill('light blue')
                                                enhance.setOutline('light blue')
                                                enhance.draw(game_window)
                                                H = Text(Point(250, 185), 'FEELING LUCKY?')
                                                H.setSize(24)
                                                H.setStyle('bold')
                                                H.setTextColor('red')
                                                H.setFace('courier')
                                                H.draw(game_window)
                                                M = Text(Point(250, 210), 'Guess a word to win ')
                                                M.setTextColor('white')
                                                M.setFace('courier')
                                                M.setSize(20)
                                                M.draw(game_window)
                                                M2 = Text(Point(250, 235), 'this round immediately!')
                                                M2.setTextColor('white')
                                                M2.setFace('courier')
                                                M2.setSize(20)
                                                M2.draw(game_window)
                                                guess = Entry(Point(250, 270), 7)
                                                guess.setFill('white')
                                                guess.draw(game_window)
                                                B = Circle(Point(300,270), 15)
                                                B.setFill('red')
                                                B.setOutline('red')
                                                B.draw(game_window)
                                                B2 = Text(Point(300,271), 'GO!')
                                                B2.setSize(11)
                                                B2.draw(game_window)
                                                R1 = Rectangle(Point(145,310),Point(355,340))
                                                R1.setFill('purple')
                                                R1.setOutline('purple')
                                                R1.draw(game_window)
                                                R2 = Text(Point(250,325),"NO, I'M NOT FEELING IT!")
                                                R2.setFill('white')
                                                R2.setStyle('bold')
                                                R2.draw(game_window)

                                                # detect clicks 
                                                no_click = game_window.getMouse()
                                                if no_click != None:
                                                    X3 = no_click.getX()
                                                    Y3 = no_click.getY()

                                                    # does not want to guess word
                                                    if 145<X3<355 and 310<Y3<340:
                                                        H.undraw()
                                                        enhance.undraw()
                                                        M.undraw()
                                                        M2.undraw()
                                                        guess.undraw()
                                                        R1.undraw()
                                                        R2.undraw()
                                                        B.undraw()
                                                        B2.undraw()
                                                        
                                                    # clicked GO to guess word
                                                    x= B.getCenter()
                                                    dx = X3 - x.getX()
                                                    dy = Y3 - x.getY()
                                                    dist = (dx*dx + dy*dy)**0.5
                                                    if dist <= B.getRadius():
                                                        guessword = guess.getText()

                                                        # guessed right 
                                                        if guessword.upper() == chosen_word:
                                                            guess.undraw()
                                                            t = Rectangle(Point(100,40),Point(400,345))
                                                            t.setFill('light blue')
                                                            t.setOutline('light blue')
                                                            t.draw(game_window)
                                                            nice_snowman(game_window)
                                                            m = Text(Point(250,290),'You Win, Boiler up!')
                                                            m.setSize(24)
                                                            m.setFill('gray')
                                                            m.setStyle('bold')
                                                            m2 = Text(Point(250,325),'Click to Continue')
                                                            m2.setFill('gray')
                                                            m2.setStyle('bold')
                                                            m2.setStyle('italic')
                                                            m2.draw(game_window)
                                                            score +=10
                                                            failed_times =0
                                                            succeeded_times=0
                                                            rounds+=1
                                                            hints =1
                                                            m.draw(game_window)
                                                            # change the background to indicate that
                                                            #   the round is coming next (celebration)
                                                            game_window.setBackground('red')
                                                            sleep(.1)
                                                            game_window.setBackground('green')
                                                            sleep(.1)
                                                            game_window.setBackground('magenta')
                                                            sleep(.1)
                                                            game_window.setBackground('cyan')
                                                            sleep(.1)
                                                            game_window.setBackground('orange')
                                                            sleep(.1)
                                                            game_window.setBackground('purple')
                                                            sleep(.1)
                                                            game_window.setBackground('gold')
                                                            sleep(.1)
                                                            game_window.getMouse()
                                                            game_window.close()
                                                            game_window, circles, polylist, chosen_word, characters, list_of_placeHolder, SCORE, ROUNDS = game_panel(score, rounds)
                                                            print(chosen_word)
                                                            failed_times = -1


                                                        # guessed the word wrong   
                                                        else:
                                                            enhance.undraw()
                                                            H.undraw()
                                                            B.undraw()
                                                            B2.undraw()
                                                            M.undraw()
                                                            M2.undraw()
                                                            R1.undraw()
                                                            R2.undraw()
                                                            guess.undraw()
                                                            for i in range(2):
                                                                failed_times+=1
                                                                drop(polylist[failed_times])
                                                                score-=1
                                                                SCORE.setText('SCORE: '+str(score))
                                                        
                                                            
                                            # losing the game completely
                                            if failed_times == 9:
                                                score-=1
                                                SCORE.setText('SCORE: '+str(score-1))
                                                
                                                w = Rectangle(Point(85,55),Point(440,230))
                                                w.draw(game_window)
                                                w.setFill('light blue')
                                                w.setOutline('light blue')
                                                # call the snowman function
                                                #   enhancement
                                                snowman(game_window)
                                                lose_infor = Text(Point(250,250),'You lose, better luck next time')
                                                lose_infor.setSize(20)
                                                lose_infor.setFill('red')
                                                lose_infor.setStyle('bold')
                                                lose_infor.draw(game_window)
                                                m5 = Text(Point(250,310),'The Word was '+chosen_word.title()+'...')
                                                m5.setSize(18)
                                                m5.draw(game_window)
                                                m5.setFill('red')
                                                m5.setStyle('bold')
                                                # prompt user for name
                                                myEntry= Entry(Point(340,280),8)
                                                myEntry.setFill('white')
                                                myEntry.draw(game_window)
                                                mes = Text(Point(210,280),'Enter your name:')
                                                mes.setTextColor('red')
                                                mes.setStyle('bold')
                                                mes.setSize(14)
                                                mes.draw(game_window)
                                                # create save button
                                                save = Rectangle(Point(380,270),Point(430,290))
                                                save.setFill('red')
                                                save.draw(game_window)
                                                save_mes = Text(Point(405,280),"SAVE")
                                                save_mes.draw(game_window)
                                                # store the in score file
 
                                                # get mouse click for save button
                                                save_click = game_window.getMouse()
                                                x4 = save_click.getX()
                                                y4 = save_click.getY()
                                                if 380<x4<430 and 270<y4<290:
                                                    # open file and write the name and scores
                                                    f = open('scores.txt','a')
                                                    name = myEntry.getText()
                                                    f.write('\n'+name+','+str(rounds)+','+str(score-1))
                                                    # close file
                                                    f.close()
                                                    game_window.close()
                                                    indicator2=False
                                                    
                                            failed_times+=1
                                            score-=1
                                            SCORE.setText('SCORE: '+str(score))
                                    
 
                            # detect clicks in control panel
                            if control_click != None:
                                x3 = control_click.getX()
                                y3 = control_click.getY()


                                # high score is clicked
                                if 65<x3<185 and 200<y3<230:
                                    highscore()
                                   
                                    
                            
                                # exit during the game
                                if 195<=x3<=235 and 30<= y3<=55:
                                    control_window.close()
                                    game_window.close()
                                    indicator1 = False
                                    indicator2 = False
                                    

                        
                   
                    # exit button
                    elif 195<=x0<=235 and 30<=y0<=55:
                        # close the window and end the loop
                        level.close()
                        control_window.close()
                        indicator1=False

            elif 195<=x0<=235 and 30<=y0<=55:
                # close the window and end the loop
                control_window.close()
                indicator1=False
     
 
 

     
 
 
main()
 
