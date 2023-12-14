# 두 점을 지나는 직선
def two_point_linear(p,q):
    '''
    두 점을 지나는 직선을 구하는 함수
    input : 튜플 형태의 두 점 p,q
    return : 기울기(m), y절편(b), x절편(a)
    '''
    m = ((p[1]-q[1])/(p[0]-q[0]))
    b = p[1]-(m*p[0])
    linear = m*x + b
    a = -b/m

    return print('기울기:{} y절편:{} x절편:{}'.format(m,b,a))