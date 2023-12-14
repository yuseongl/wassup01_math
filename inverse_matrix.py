input= [[3,4,5],[6,7,2]]

# old version
def inverse_matrix(input):
    '''
    function for inverse matrix

    input : matrix -> list(int)
        you can input matrix of two-dimensional form
        ex) [[a,b,alpha],[c,d,beta]]
        
    output : x,y -> int
    '''
    D = input[0][0]*input[1][1]-input[0][1]*input[1][0]
    if D == 0:
        print('해가 존재하지 않습니다.')
        if input[0][2] / input[0][1] == input[1][2] / input[1][1]:
            print('무수히 많은 해가 존재합니다.')
        if input[0][2] / input[0][1] != input[1][2] / input[1][1]:
            print('해가 존재하지 않습니다.')
    x = (input[1][1]*input[0][2] - input[0][1]*input[1][2])/D
    y = (input[0][0]*input[1][2] - input[1][0]*input[0][2])/D
    return x,y
print(inverse_matrix(input))

# new viersion
def use_inverse_matrix(a:np.array ,b:np.array):
    '''
    fonction for answer using inverse matric

    input : a -> np.array
            b -> np.array

        det = 1/a*d - b*c 
        det variable mean a determinant
    
    output : answer -> np.array

    '''
    answer = 0
    a,b,c,d = a[0][0], a[0][1],a[1][0],a[1][1]
    alp, beta = b[0],b[1]

    det = 1/a*d - b*c
    if det == 0:
        print('해가 존재하지 않습니다.')
        if alp/b == beta /d:
            print('무수히 많은 해가 존재합니다.')
        if alp/b != beta /d:
            print('해가 존재하지 않습니다.')
        return answer

    inverse = np.linalg.inv(a)
    answer = inverse@b
    print(answer)

    return answer