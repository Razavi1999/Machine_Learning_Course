def decrypt(data):
    L = data >> 32
    R = data & 0xffffffff
    for i in range(17, 1, -1):
        L = p[i]^L
        L1 = calculate(L)
        R = R^calculate(L1)
        L,R = R,L

    L,R = R,L
    L = L^p[0]
    R = R^p[1]
    data_decrypted1 = (L<<32) ^ R
    return data_decrypted
