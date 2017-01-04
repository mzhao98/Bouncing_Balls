'''
This module simulates balls bouncing around a canvas.
'''

import math, random, time
from Tkinter import *

def random_color():
    '''random_color which will generate random color values in hexadecimal 
    digits'''
    output = '#'
    for i in range (0, 6):
        output += str(random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 
                                     'c', 'd', 'e', 'f']))
    return output

class BouncingBall:
    '''Objects of this class represent balls which bounce on a canvas.'''

    def __init__(self, canvas, center, radius, color, direction, speed):
        '''
        Create a new ball with a given location, direction, color, and speed.

        Arguments:
          canvas:    the canvas the ball moves on
          center:    the center of the ball in (x, y) pixel coordinates
          radius:    the radius of the ball in pixels
          color:     the color of the ball
          direction: the initial direction the ball is moving
          speed:     the initial speed of the ball
        '''

        x, y = center
        x1 = x - radius
        y1 = y - radius
        x2 = x + radius
        y2 = y + radius
        self.handle = canvas.create_oval(x1, y1, x2, y2,
                        fill=color, outline=color)
        self.canvas = canvas
        self.xmax   = int(canvas.cget('width')) - 1
        self.ymax   = int(canvas.cget('height')) - 1
        self.center = center
        self.radius = radius
        self.color  = color
        self.direction = direction

        # The direction is represented as an angle in degrees
        # (range 0-360), which we convert to radians here.
        # The angle is with respect to the positive x axis,
        # going clockwise around the origin.
        if direction < 0.0 or direction > 360.0:
            raise ValueError('Invalid direction; must be in range [0.0, 360.0]')
        dir_radians = direction * math.pi / 180.0

        # Separate the direction into its x and y coordinates.
        # Flip the sign of the y coordinate because the y coordinate
        # grows downward, not upward.
        self.dirx = math.cos(dir_radians)
        self.diry = -math.sin(dir_radians)

        # Speed is represented as a single non-negative float.
        # Note that non-float speeds will behave poorly.
        if speed < 0.0: 
            raise ValueError('Invalid speed; must be positive')
        self.speed = speed

    
    
    def step(self):
        '''
        Move this ball in its current direction with its current speed.  
        Change direction if the edge of the canvas is reached.

        Arguments: none
        Return value: none
        '''
        
        vx = self.speed * self.dirx
        vy = self.speed * self.diry 
        (a,b) = self.center
        
        
        dx = ball.displacement(a, vx, self.xmax)
        dy = ball.displacement(b, vy, self.ymax)
        
        
            
        if dx != vx:
            self.dirx *= -1
            
        if dy != vy:
            self.diry *= -1       
              
              
        self.canvas.move(self.handle, dx, dy)
        self.center = (a+dx, b+dy)
        
       
        # TODO: Add your code here. 

    def displacement(self, c, d, cmax):
        '''
        Compute the actual displacement along the x or y dimension,
        taking reflections off the edge into account.  
        
        Arguments:
          c:    the center of the ball (x or y coordinate)
          cmax: the largest value in that direction
          d:    the desired displacement in that direction

        Return value: the computed displacement
        '''
        r = self.radius
        
        if c + r + d <= cmax and c - r + d >= 0:
            return d
        
        if c -r + d < 0:
            return (c-r)-d
        
        if c + r+ d > cmax:
            return 2*cmax - 2*c - 2*r - d
      
        # TODO: Add your code here. 

    def scale_speed(self, scale):
        '''
        Scale the speed of this object.
        
        Arguments: 
          scale: the speed scaling factor

        Return value: none
        '''
        self.speed *= scale
        # TODO: Add your code here. 

    def delete(self):
        '''
        Remove this object from the canvas.

        Arguments: none
        Return value: none
        '''

        self.canvas.delete(self.handle)
       


def random_ball(canvas, rmin, rmax, smin, smax, xmax, ymax):
    '''
    Create and return a ball with a random color, starting position,
    size, direction, and velocity.
    rmin: minimum radius (pixels)
    rmax: maximum radius (pixels)
    smin: minimum speed
    smax: maximum speed
    xmax: maximum x dimension of canvas
    ymax: maximum y dimension of canvas
    '''
    radius = random.choice(range(rmin, rmax))
    speed = random.uniform(smin, smax)
    xpos = random.choice(range(radius, xmax-radius))
    ypos = random.choice(range(radius, ymax-radius))
    x1 = xpos - radius
    y1 = ypos - radius
    x2 = xpos + radius
    y2 = ypos + radius    
    direction = random.uniform(1.0, 360.0)
    color = random_color()
    #ball = BouncingBall(canvas, (xpos, ypos), radius, color, direction, speed)
    # TODO: Add your code here.
    
    return BouncingBall(canvas, (xpos, ypos), radius, color, direction, speed)

def key_handler(event):
    '''Handle key presses.'''
    global bouncing_balls
    global done
    global color
    key = event.keysym
    if key == 'q': 
        done = True
    elif key == 'plus':  # add a ball at a random location
        bouncing_balls.append(random_ball(canvas, 10, 60, 1.0, 5.0, 800, 600))
        # TODO: Add your code here.   Use the random_ball function.
    elif key == 'minus':  # remove a ball from the canvas if there are any
        if len(bouncing_balls) > 0:
            bouncing_balls[0].delete()
            bouncing_balls = bouncing_balls[1:]
        # TODO: Add your code here.  Use the delete() method on balls.
    elif key == 'u':  # speed (u)p all bouncing_balls by factor of 1.2
        for i in bouncing_balls:
            i.scale_speed(1.2)
        # TODO: Add your code here.   Use the scale_speed() method on balls.
    elif key == 'd':  # slow (d)own all bouncing_balls by factor of 1.2
        for i in bouncing_balls:
            i.scale_speed(1.0/1.2)
        # TODO: Add your code here.   Use the scale_speed() method on balls.
    elif key == 'x':  # delete all bouncing_balls
        canvas.delete('all')
        bouncing_balls=[]
        # TODO: Add your code here.   Use the delete() method on balls.
        # Adjust the global list of balls accordingly.

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x600')
    canvas = Canvas(root, width=800, height=600)
    canvas.pack()
    done = False

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    
    # Set up some bouncing balls.
    bouncing_balls = []
    for i in range(5):
        bouncing_balls.append(random_ball(canvas, 10, 60, 1.0, 5.0, 800, 600))

    # Start the event loop.
    while not done:
        time.sleep(0.001)  # add a slight delay to smooth out the simulation
        for ball in bouncing_balls:
            ball.step()
        root.update()

