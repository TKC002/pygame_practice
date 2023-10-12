def inner_product(vec1, vec2):
    n = len(vec1)
    if len(vec2) != n:
        print('vector1 and vector2 must be same length.')
        return False
    res = 0
    for e1, e2 in zip(vec1, vec2):
        res += e1*e2
    return res

def cross_product(vec1, vec2):
    n = len(vec1)
    if len(vec2) != n:
        print('vector1 and vector2 must be same length.')
        return False
    if n == 2:
        tmp1 = vec1
        tmp1.append(0)
        tmp2 = vec2
        tmp2.append(0)
    res = [0,0,0]
    res[0]=vec1[1]*vec2[2]-vec1[2]*vec2[1]
    res[1]=vec1[2]*vec2[0]-vec1[0]*vec2[2]
    res[2]=vec1[0]*vec2[1]-vec1[1]*vec2[0]

    return res

def on_segment(point, seg):
    tmp_seg = [seg[0], point]
    vec = [seg[1][0]-seg[0][0], seg[1][1]-seg[0][1]] # B-A
    tmp_vec = [tmp_seg[1][0]-tmp_seg[0][0], tmp_seg[1][1]-tmp_seg[0][1]] # P-A

    




