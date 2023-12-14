import math

def quadratic_polynomial(a,b,c,x):
    '''
    이차식의 해와 꼭짓점을 구하는 함수
    
    input : a,b,c 이차함수의 상수 -> int
    return : solution = x절편, -> int
             vertex = 꼭짓점(x,y) -> int
    '''
    D = b**2 - (4*a*c)
    x_vertex = -b/(2*a)
    y_vertex = a*(x_vertex**2)+(b*x_vertex)+c
    if D<0:
        print('solution does not exist!')
        return 
    elif D==0:
        value = -b/2*a 
        print('solution exist only one!\nsolution : {},vertex : {}'.format(value,[x_vertex,y_vertex]))
        return
    else:
        value = [(-b + math.sqrt(D))/(2*a),(-b - math.sqrt(D))/(2*a)]
        print('solution exist!\nsolution : {},vertex : {}'.format(value,[x_vertex,y_vertex]))
    graph = a*(x**2) + b*x + c
    return