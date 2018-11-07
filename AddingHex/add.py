def Add(A,B,N):
    C = [0]* (N+1)
    carry = 0x00
    for i in range(0,N):
         digit = A[i] + B[i] + carry
         C[i] = digit%256
         carry = digit/256
    C[N] = carry
    return C

if __name__ =='__main__':
    a = [0xfe, 0xff]
    b = [0xaa, 0xbb]

    C = Add(a,b,2)
    print(C)
