# Quiz 1,3
def differential(polynomial:list, num:int):
    '''
    function for calculation derivative Differential coefficient after differential
    
    args:
        polynomial : you can get polynomial coefficient list -> lsit
        num : if you want get Differential coefficient input num -> int
        
    return:
        answer : derivative -> list
        diff_coeff : Differential coefficient -> int

    '''
    diff_coeff = 0
    answer = []
    for i in range(len(polynomial)):
        if polynomial[i] != 0:
            coefficient = int(i)*polynomial[i]
            diff_coeff += coefficient * num ** i
            answer.append(str(coefficient)+'x^'+str(i))
    print('Differential coefficient : ',diff_coeff)
    print('derivative : ',answer)
    return answer, diff_coeff

#Quiz 2
def e_differential(n:int, num:int=0):
    '''
    function for calculation natural exponential function differential using recursive function
    this function hasn't result value. 
    
    function for differential : x*e^x
    
    args:
        n: derivative number -> int
        num: number for recursive function size(default=0) -< int
        
    return: print n stage derivative 

    '''
    num += 1
    if n == num:
        return  print('{}계 도함수 : {}e^x + xe^x'.format(num,num))
    e_differential(n,num)
    return 