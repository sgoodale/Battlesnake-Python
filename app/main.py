import bottle
import os
import random
import math


def ID = 0

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')

@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.png' % (
	#head_url = 'http://placecage/com/c/100/100' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )
    
    return {
        'color': 'gold',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json
    ID = data['game_id']
    return {
        'color': 'gold',
        'name': 'Dream_Team_Swag_Snake_Team_Of_Dreams'
        'taunt': 'Existence is pain',
        'head_type': 'sand-worm',
        'tail_type': 'skinny-tail',
        'game_id': ID
    }
    

def closestFood(): 
    data = bottle.request.json
    
    snakes = data.get('snakes')
    food = [None]*2
    mySnake = None
    mySnakeHead = None
    mySnakeTail = None
    action = None
    for snake in snakes:
        if snake.get('id') == "7b6a3593-5ccf-49dc-ac1c-2108793bcac6":
            mySnake = snake
            
    myCoords = mySnake.get('coords')
    mySnakeHead = myCoords[0]
    snakex = mySnakeHead[0]
    snakey = mySnakeHead[1]
    
    foodCoords = data.get('food')
    minim = data.get('height') + data.get('width')
    for i in range(0,len(foodCoords)-1):
        currFood = foodCoords[i]
        x = currFood[0]
        y = currFood[1]
        coldif = abs(x - snakex)
        rowdif = abs(y - snakey)
        distance = coldif + rowdif
        if distance <= minim:
            minim = distance
            food = [x,y]
    return food

    
def moveToFood():
    data = bottle.request.json   
    moveToDo = None
    
    snakes = data.get('snakes')
    mySnake = None
    dangerZone = []
    for snake in snakes:
        if snake.get('id') == "7b6a3593-5ccf-49dc-ac1c-2108793bcac6":
            mySnake = snake
        dangerZone = dangerZone + snake.get('coords')
            
        
    
    foodToGetCoords = closestFood()
    snakeHeadCoords = getInitSnakeCoords()
    foodX = foodToGetCoords[0]
    foodY = foodToGetCoords[1]
    snakeX = snakeHeadCoords[0]
    snakeY = snakeHeadCoords[1]
    difX = abs(foodX-snakeX)
    difY = abs(foodY-snakeY)
    difX = int(difX)
    difY = int(difY)
    distance = difX + difY
    print foodToGetCoords
    print snakeHeadCoords
    futurePosition = None
    if snakeX <= foodX and mySnake.get('message') != 'Moved west':
        futurePosition = [snakeX+1,snakeY]
        if futurePosition not in dangerZone:
            moveToDo = 'east'
            return moveToDo
    if snakeX > foodX and mySnake.get('message') != 'Moved east':
        futurePosition = [snakeX-1,snakeY]
        if futurePosition not in dangerZone:
            moveToDo = 'west'
            return moveToDo            
    if snakeY <= foodY and mySnake.get('message') != 'Moved north':
        futurePosition = [snakeX,snakeY+1]
        if futurePosition not in dangerZone:
            moveToDo = 'south'
            return moveToDo            
    if snakeY > foodY and mySnake.get('message') != 'Moved south':
        futurePosition = [snakeX,snakeY-1]
        if futurePosition not in dangerZone:        
            moveToDo = 'north'
            return moveToDo                
    if moveToDo == None:
        futurePosition = [snakeX+1,snakeY]
        if futurePosition not in dangerZone:
            return 'east'        
        futurePosition = [snakeX-1,snakeY]
        if futurePosition not in dangerZone:
            return 'west'
        futurePosition = [snakeX,snakeY+1]
        if futurePosition not in dangerZone:
            return 'south'
        futurePosition = [snakeX,snakeY-1]
        if futurePosition not in dangerZone:        
            return 'north'
    if snakeX == 0:
        return 'north'
    if snakeX == 17:
        return 'south'
    if snakeY == 0:
        return 'east'
    if snakeY == 17:
        return 'west'
    else:
        return None
    
def getInitSnakeCoords():
    data = bottle.request.json    
    mySnake = None
    mySnakeHead = None
    mySnakeTail = None    
    snakes = data.get('snakes')
    for snake in snakes:
        if snake.get('id') == "7b6a3593-5ccf-49dc-ac1c-2108793bcac6":
            mySnake = snake
            
    myCoords = mySnake.get('coords')
    mySnakeHead = myCoords[0]    
    mySnakeTail = myCoords[len(myCoords)-1]
    return mySnakeHead

@bottle.post('/move')
def move():
    data = bottle.request.json
    action = None
    action = moveToFood()
    
    return {  
      'move': action,
      'taunt': "OH YEAHHHH"
    }


@bottle.post('/end')
def end():
    data = bottle.request.json
    
    # TODO: Do things with data

    return {
        'taunt': 'GOOD GAME!!!! '
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
