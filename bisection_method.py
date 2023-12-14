class Bisection_Method:
    def __init__(self):
        print('뉴턴 방정식을 시작합니다!')
        
    def function_value(self, polynomial:list, x:int) -> int:
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
        
    def differential(self, polynomial:list, num:int=0) -> list:
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
        
    def solution_check(self,poly:list, section:list) -> bool:
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
            print('구간을 다시 설정하세요!\n현 구간:',section)
            return False
        return True
    
    def bisection_method(self,poly:list, a:int, b:int) -> int:
        '''function for calculation bisection method to getting solution
        
        args:
            poly: polynomial function for checking -> list
            a: first value of section for checking Existence of solution -> int
            b: second value of section for checking Existence of solution -> int
        
        return:
            c : solution of bisection method -> int
        '''
        section = [a,b]
        if self.solution_check(poly,section):
            c = (a+b)/2
            section2 = [a,c]
            if self.function_value(poly,c) == 0:
                print('해를 찾았습니다!\nsolution:',c) 
                print('section:',section)
                return c
            elif self.solution_check(poly,section2):
                return self.bisection_method(poly,a,c)
            else:
                return self.bisection_method(poly,c,b)
        return

if __name__ == '__main__':
    
    netwon = Bisection_Method()
    netwon.bisection_method([-4, 0, 1],0, 100)