import numpy as np
import math

# Quiz1
def cosine_similarity(a:np.array, b:np.array):
    '''
    function for calculating cosine similarity
    input : a -> np.array
            b -> np.array
        
        get cosine similarity as float type using input variable 'a,b'

    output : answer -> float

        answer is cosine similarity
    '''
    if a.shape != b.shape:
        print('입력된 벡터의 크기가 다릅니다.')
        return 

    answer = np.dot(a,b)/math.sqrt(np.dot(a,a)*np.dot(b,b)) 

    return answer