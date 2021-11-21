#Python program to build the Snake Game
#importing the libraries used in the program
import turtle 
import time
import random

#global variables - they can be acccessed throughout the program, unlike 'local varibles'

score = 0       #variable to store the gamescore
gamespeed = 0.1   #variable to store the speed of the game
bodyparts = []  #list to hold the newly created body parts
                #newparts will be added to it when the snake 'eats' the egg 

#Step 1 - Create a window
window = turtle.Screen()
window.title("Deeya's Snake Game")
window.setup(500,500)
window.bgpic('background.gif')   #insert an image as the background

#Step 2 - Create a border
border = turtle.Turtle()
border.color('midnight blue')
border.hideturtle()
border.penup()
border.goto(0,-180)
border.write("Press 'Esc' to exit.", align="center", font=("Comic Sans MS", 18, "normal"))
border.width(3)
border.goto(-150,150)
border.pendown()

#loop to create a border
for i in range(0,4):
  border.forward(300)
  border.right(90)


#Step 3 - Create a snake 
snake = turtle.Turtle()
snake.color('midnight blue')
snake.penup()
snake.direction = 'Right' #default direction
snake.speed(0)
turtle.register_shape('snake.gif') 
snake.shape('snake.gif')   #set snake as an image

#Step 6 - Create an egg
egg = turtle.Turtle()
egg.color('red')
turtle.register_shape('egg.gif') 
egg.shape('egg.gif')   #set egg as an image
egg.penup()
egg.speed(0)

#Step 7 - Create a scoreboard
scoreboard = turtle.Turtle()
scoreboard.shape('circle')
scoreboard.color('white')
scoreboard.penup()
#The turtle 'scoreboard' should not be visible, only the projected 'score' should be visible 
scoreboard.hideturtle() #hides the turtle
scoreboard.goto(0,155)
#{} is where the score variable will be printed - its a placeholder
#The rest is formatting the text
scoreboard.write("Score: {}".format(score), align="center", font=("Comic Sans MS", 24, "normal"))


#A function is a named section in a program which performs a specific task

def move_snake(): #function to move the snake
  #Get x and y coordinates of the snake
  x = snake.xcor()
  y = snake.ycor()
  
  #If direction is 'Up'
  if snake.direction == 'Up':
    #Increase y coordinate by 20 pixels
    snake.goto(x,y+20)
   
  #If direction is 'Down'
  elif snake.direction == 'Down':
    #Decrease y coordinate by 20 pixels
    snake.goto(x,y-20)
    
  #If direction is 'Right'
  elif snake.direction == 'Right':
    #increase x coordinate by 20 pixels
    snake.goto(x+20,y)
   
  #If direction is 'Left'
  elif snake.direction == 'Left':
    #Decrease x coordinate by 20 pixels
    snake.goto(x-20,y)

  time.sleep(gamespeed)


def go_up(): #function to set direction as 'Up'
  #If the snake is moving 'Down', it cannot move 'Up' and eat itself
  if snake.direction != 'Down':
    snake.direction = 'Up'


def go_down(): #function to set direction as 'Down'
  #If the snake is moving 'Up', it cannot move 'Down' and eat itself
  if snake.direction != 'Up':
    snake.direction = 'Down'
 

def go_right(): #function to set direction as 'Right'
  #If the snake is moving 'Left', it cannot move 'Right' and eat itself
  if snake.direction != 'Left':
    snake.direction = 'Right'


def go_left(): #function to set direction as 'Left'
  #If the snake is moving 'Right', it cannot move 'Left' and eat itself
  if snake.direction != 'Right':
    snake.direction = 'Left'
def go_q():
  snake.direction = 'Lqeft'
  bodyparts.clear()

def key_control(): #function to add arrow key controls
  #Start listening to the keyboard
  window.listen()
  #If the user presses the 'Esc' key, call the exit function
  window.onkey(exit , 'Escape')
  #If the key pressed is 'Up arrow key', then set the direction to 'Up'
  window.onkey(go_up,'Up')
  #If the key pressed is 'Down arrow key', then set the direction to 'Down'
  window.onkey(go_down,'Down')
  #If the key pressed is 'Right arrow key', then set the direction to 'Right'
  window.onkey(go_right,'Right')
  #If the key pressed is 'Left arrow key', then set the direction to 'Left'
  window.onkey(go_left,'Left')
  window.onkey(go_q,'q')
  #if W,A,S,D needs to be included
'''  
  #If the key pressed is 'W' key, then set the direction to 'Up'
  window.onkey(go_up,'W')
  #If the key pressed is 'S' key, then set the direction to 'Down'
  window.onkey(go_down,'S')
  #If the key pressed is 'D' key, then set the direction to 'Right'
  window.onkey(go_right,'D')
  #If the key pressed is 'A' key, then set the direction to 'Left'
  window.onkey(go_left,'A')
'''
 

def egg_eaten(): #function to execute when the egg is eaten

  global score #denotes that a variable 'score' has already been declared globally
	       #this makes sure that another variable 'score' is not re-created	
  #If distance between snake and egg is <= 15 (ie, If the egg is eaten)
  if snake.distance(egg) <= 15:
    #randomly move egg to a different point
    xcoregg = random.randint(-150,150) #randint gives a random-integer between the specifed range
    ycoregg = random.randint(-150,150)
    egg.goto(xcoregg,ycoregg)
  
    #Create and add a newpart to the list 'bodyparts[]' 
    #The new parts will be created one on top of the other, hence only one bodypart will be visible initiall
    newpart = turtle.Turtle()
    newpart.shape("circle")
    newpart.color("white")
    newpart.speed(0)
    newpart.penup()
    bodyparts.append(newpart) #join newpart to the list 'bodyparts[]'

    #Increase the score
    
    scoreboard.clear()
    score = score+10
    scoreboard.write("Score: {}".format(score), align="center", font=("Comic Sans MS", 24, "normal"))
  
def move_body(): #function to move the snake's bodyparts
  #There are 2 steps to move the body of the snake: 
  	#Step A - Move each bodypart to the position of the previous one,
 	  	  #so part 5 moves to position 4, 4 moves to 3, 3 to 2, 2 to 1 and 1 moves to 0th position 
 	#Step B - Move the 0th bodypart to the snake's position.

  #length of (bodyparts list)-1 is the last index of the list
  #so iterate down the list from the last index of the list to 0,
  last_index =  len(bodyparts)-1
  first_index =  0
  interval =  -1
  for position in range( last_index, first_index ,interval):
    #move the bodypart at 'position' to 'position -1' 
    x = bodyparts[position-1].xcor()
    y = bodyparts[position-1].ycor()
    bodyparts[position].goto(x, y)
    
  #If the Length of the list is > 0 (ie, if the list is not empty)
  if len(bodyparts) > 0 :
    #get the x and y coordinates of the snake
    xcorsnake = snake.xcor()
    ycorsnake = snake.ycor()
    #move the 0th element of the list to the snake's position
    bodyparts[0].goto(xcorsnake,ycorsnake)



def snake_is_dead(): #function to run if the snake is dead
  global score
  #Give it a random direction to stop 
  snake.direction = "stop"

  #for each element in the list	
  for i in bodyparts: 
    i.color('red') #change the color of body to red
    
  time.sleep(2) #pause the game for 2 seconds 
  
  #Move each body part out of screen
  for j in bodyparts:
    j.goto(1000,1000)

  #Move the snake to the middle of the screen
  snake.goto(0,0)
    
  #Clear the list 'bodyparts[]'
  #So next time the game starts, the body does not appear    
  bodyparts.clear()

  #prompt a 'Game Over' message
  snake.write('  GAME OVER!!!',align ='center', font = ('Comic Sans MS',24,'bold'))

  time.sleep(2) #pause the game for 2 seconds 
  snake.clear() 

  #Reset the score and display
  score = 0
  scoreboard.clear()
  scoreboard.write("Score: {}".format(score), align="center", font=("Comic Sans MS", 24, "normal"))

  #make the screen blink
  window.bgcolor('white')
  time.sleep(0.5)
  window.bgcolor('coral')
  
def check_border_collision(): #function to check for border collisions
  #If the snake hits the borders on any side  
  if snake.xcor() > 150 or snake.xcor() < -150 or snake.ycor() > 150 or snake.ycor() < -150:
    snake_is_dead() #call the snake is dead function

def check_body_collision(): #function to check for body collisions 
  #for each bodypart
  for i in bodyparts:

    #if it is touching the snake
    if i.distance(snake) < 20 :
      snake_is_dead() #call the snake is dead function
    
def exit(): #function to exit the game
  #If this function has been called, it means that the user wants to exit the game
  #Hence we set the global variable 'flag' as 'True'
  global game_running
  
  game_running = False

game_running = True

#Keep running the program till the user stops it 
#A loop that executes forever (infinite loop)
while game_running: #game loop

  window.update() #refresh the window
    
  #Step 10.A - Check for border collisions
  check_border_collision()

  #Step 4 - Make the snake move
  move_snake()
  
  #Step 5 - Add arrow key controls
  key_control()

  #Step 10.B - Check for body collisions
  #check_body_collision()
  
  #Step 8 - When the egg is eaten
  egg_eaten()
  
  #Step 9 - Move bodyparts
  move_body()


turtle.bye()   #close the turtle window

