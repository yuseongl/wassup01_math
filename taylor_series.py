import math

# Quiz 1
def differential(polynomial:list, num:int=0):
    '''
    function for calculation derivative Differential coefficient after differential
    
    args:
        polynomial : you can get polynomial coefficient list -> lsit
        num : if you want get Differential coefficient input num -> int
        
    return:
        answer : derivative -> list
        diff_coeff : Differential coefficient -> int

    '''
    answer = []
    for i in range(1,len(polynomial)):
            answer.append(i*polynomial[i])
    return answer


def function_value(polynomial:list,x):
    '''
    function for getting polynomial function calculation value
    
    args:
        polynomial: list of polynomial function coefficient  ->  lsit
            if any degree coefficient is zero, you must contain zero in list
        x: variable of polynomial function  ->  int
    
    return:
        coeff: calculation value of polynomial function -> int
    '''
    coeff = 0
    for i in range(len(polynomial)):
        coeff += polynomial[i]*(x**i)
    return coeff


poly_list=[]
def taylor_series_module(polynomial,x,num,cnt=0,answer=0):
    '''
    function for support getting calculation value of taylor series
    this function calculate any degree derivative and make list fo derivative
    from one degree derivative to num degree derivative using Recursion function
    
    args:
        polynomial: list of polynomial function coefficient  ->  lsit
        x: variable of polynomial function  ->  int
        num: you can set degree of derivative -> int
    '''
    b=0.99
    cnt += 1
    if num < cnt:
        cnt = 0
        return answer
    
    poly = differential(polynomial)
    answer += function_value(poly,x)/math.factorial(cnt)*(b-x)**cnt
    poly_list.append(poly)
    return taylor_series_module(poly,x,num,cnt,answer)

def taylor_series(polynomial:list,x,num,cnt=0):
    '''
    function for calculation taylor series using taylor_series_module function 
    
    args:
        polynomial: list of polynomial function coefficient  ->  lsit
        x: variable of polynomial function  ->  int
        num: you can set degree of derivative -> int
    '''
    value = function_value(polynomial,x)
    poly = taylor_series_module(polynomial,x,num,cnt)
    answer = value + poly
    return answer

if __name__ == '__main__':
    print('f(0.99) 근사값:',taylor_series([30, -2023, 11, 2023],1,5))
    print('f(1):',function_value([30, -2023, 11, 2023],1))