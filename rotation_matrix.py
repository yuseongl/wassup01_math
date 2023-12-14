import math

def vector_rotation(x, y, theta):
    '''
    function for vector rotation
    input : x -> int
            y -> int
            theta -> int

        theta is value for rotation vector

    output : x, y -> int
    '''
    radians = math.radians(theta)

    x = x*math.cos(radians)-y*math.sin(radians)
    y = x*math.sin(radians)+y*math.cos(radians)
    print('x:',x,'y:',y)
    return x,y

vector_rotate(3,5,80)