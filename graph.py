f_list=[]
class f_graph_shift:
    '''
    class for get some mathmatic function graph

    this class have some mathmatic function and function 
    for shifting and scaling

    including function: x, x^2, relu, sin, cost, tangent, arctangent  

    input : func : mathmatic function                              -> function or 
                   you can get any graph about mathmatic function  -> 'all'(string)
            x_shift : x-axis parallel movement vlaue               -> int
            y_shift : y-axis parallel movement vlaue               -> int
            x_scaling : zoom-in, zoom-out about x-value            -> int
            y_scaling : zoom-in, zoom-out about y-value            -> int
            x_symmetry : x-axis symmetry                           -> int(1 or -1)
            y_symmetry : y-axis symmetry                           -> int(1 or -1)

    output : mathmatic function graph                              -> plot
             y value list of mathmatic function                    -> list(int)
    '''
    def __init__(self):
        self.x = np.linspace(-5, 5, 100)
        f_list.append(self.f_x(x))
        f_list.append(self.f_x_double(x))
        f_list.append(self.f_relu(self.x))
        f_list.append(self.f_sin(x))
        f_list.append(self.f_cos(x))
        f_list.append(self.f_tan(x))
        f_list.append(self.f_arctan(x))

    def f_x(self, x:float):
        return np.sin(x) + x + x * np.sin(x)

    def f_x_double(self, x:float):
        return x**2

    def f_relu(self, x:float):
        return np.maximum(0,x)

    def f_sin(self, x:float):
        return np.sin(x)

    def f_cos(self, x:float):
        return np.cos(x)

    def f_tan(self, x:float):
        return np.tan(x)

    def f_arctan(self, x:float):
        return np.arctan(x)

    def draw_graph(self, func, x_shift:int=0, y_shift:int=0, x_scaling:int=1, y_scaling:int=1, x_symmetry:int=1, y_symmetry:int=1):
        plt.rcParams["figure.figsize"] = [5, 3]
        plt.rcParams["figure.autolayout"] = True
        print(func)
        if func == 'all':
            for i in range(len(f_list)):
                plt.plot(self.x, x_symmetry*(y_scaling*((x_scaling*y_symmetry*(f_list[i]-x_shift))+y_shift)), color='red', label='f(x)')
                plt.title('Graph')
                plt.show()
            return

        plt.plot(self.x, x_symmetry*(y_scaling*(func(x_scaling*y_symmetry*(self.x-x_shift))+y_shift)), color='red', label='f(x)')
        plt.title('Graph')
        plt.show()

a = f_graph_shift()
a.draw_graph('all',x_shift=5, y_shift=7, x_scaling=8, y_scaling=2, x_symmetry=-1, y_symmetry=1)