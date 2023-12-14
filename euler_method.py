import numpy as np
import matplotlib as plt
from .taylor_series import function_value, differential

y_label = []
x_label = []
def euler_method(poly,h,x,y):
    '''
    function for calculation euler method 
    
    for using this function you must have other function
    required function list : function_value()
    
    args:
        poly: list of polynomial function coefficient  ->  lsit
        h: variable for setting step size -> int
        x: Initial value of x ->int
        y: Initial value of y ->int
        
    return: x_label: x label value list stepping as much as you set  -> list
            y_label: y label value list  -> list

    '''
    if x > 4:
        return x_label, y_label
    
    x_label.append(x)
    y_label.append(y)
    y = y+function_value(poly,x)*h
    
    return euler_method(poly,h,x+h,y)

def graph():
    '''
    function for getting graph of value predicted as euler method
    you can get a different graph depending on list you set
    if you want getting other graph plz put specific float on step_list
    
    for using this function you must have other function
    required function list : differential(), euler_method(), function_value()
    
    args:
        None
    return:
        None
    '''
    x = np.linspace(0,4,100)
    y = function_value([1, 8.5, -10, 4, -0.5],x)
    step_list = [0.1,0.25,0.5,0.75]
    plt.plot(x, y, "g", label='real')
    
    for i in step_list:   
        poly = differential([1, 8.5, -10, 4, -0.5])
        x_pred, y_pred = euler_method(poly,i,0,1)
        
        plt.plot(x_pred, y_pred , "r", label=f'pred{i}')
    plt.legend()
    plt.show()
    
    return


graph()