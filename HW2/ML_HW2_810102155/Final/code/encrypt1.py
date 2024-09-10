def encrypt(data):
        L = data>>32
        R = data & 0xffffffff
        for i in range(0,16):
                L = L^p[i]
                L1 = calculate(L)
                R = R^calculate(L1)
                L,R = R,L
        L,R = R,L
        L = L^p[17]
        R = R^p[16]
        encrypted = (L<<32) ^ R
        return encrypted
