class Netwon_Method:
    def __init__(self):
        print('뉴턴 방정식을 시작합니다!')
        
    def function_value(self, polynomial:list, x:int):
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
        
    def differential(self, polynomial:list, num:int=0):
        '''
        function for calculation derivative Differential coefficient after differential
        
        args:
            polynomial : you can get polynomial coefficient list -> lsit
            num : if you want get Differential coefficient input num -> int
            
        return:
            answer : derivative -> list
            diff_coeff : Differential coefficient -> int
        '''
        #diff_coeff = 0
        answer = []
        for i in range(1,len(polynomial)):
            #if polynomial[i] != 0:
                answer.append(i*polynomial[i])
                #diff_coeff += coefficient * num ** i
                #answer.append(str(coefficient)+'x^'+str(i))
        #print('Differential coefficient : ',diff_coeff)
        #print('derivative : ',answer)
        return answer    
        
    def solution_check(self,poly:list, section:list):
        '''
        function for checking solution of polynomial function exists or not
        
        input: 
            poly: polynomial function for checking -> list
            section: section for checking Existence of solution -> list
        '''
        if self.function_value(poly,section[0])*self.function_value(poly,section[1])==0:
            if self.function_value(poly,section[0]) == 0:
                print('p(x)의 해는:',section[0])
                return False
            else:
                print('p(x)의 해는:',section[1])
                return False
        elif self.function_value(poly,section[0])*self.function_value(poly,section[1])>0:
            print('구간을 다시 설정하세요!')
            return False
        return True
    
    def netwon_method(self,poly:list, x:int, cnt:int):
        '''
        function for calculation netwon method using recursive function
        
        input:
            pol: polynomial function for getting solution -> list 
            x: x1 value for predictions x2 -> int
            cnt: this function will run until cnt value -> int
        
        return: 
            solution: solution of polynomial function -> int
            value: calculation value of solution -> int 
        '''
        if self.function_value(poly,x)==0 or cnt==0:
            return x, self.function_value(poly,x)
        
        answer = x-(self.function_value(poly,x)/self.function_value(self.differential(poly),x))
        return self.netwon_method(poly, answer, cnt-1)

if __name__ == "__main__":
    netwon = Netwon_Method() 
    check = netwon.solution_check([-4, 0, 1],[0, 12])
    
    if check:
        x = netwon.function_value([-4, 0, 1],0)
        solution, value = netwon.netwon_method([-4, 0, 1],x,100)
        print('해:{}\n근사 값:{}'.format(solution,value))