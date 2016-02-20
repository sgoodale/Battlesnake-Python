import bottle
import os
import random


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )
    
    return {
        'color': 'orange',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json
    
    # TODO: Josh edits

    return {
        'taunt': 'MOTHAFUCKA'
    }
# https://jordanjaytester.herokuapp.com

@bottle.post('/move')
def move():
    data = bottle.request.json
   
    snakes = data.get('snakes')
    mySnake = None
    action = None
    for snake in snakes:
        if snake.get('id') == "7b6a3593-5ccf-49dc-ac1c-2108793bcac6":
            mySnake = snake
    
    if mySnake.get('age') > 2:
        action = 'north'
    else:
        action = 'west'
    
    # TODO: Do things with data
    dirs = ['east', 'north', 'west', 'south']
    
    return {  
      'move': action,
      'taunt': 'moving east'
    }


@bottle.post('/end')
def end():
    data = bottle.request.json
    
    # TODO: Do things with data

    return {
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))

snakes = data.get('snakes')
for snake in snakes 
    print snake.get('age')