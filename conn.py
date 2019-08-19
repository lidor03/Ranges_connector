#ranges connect

def conn(A,B):
    c = []
    start = None
    i = j =0
    while i<len(A) and j<len(B):
        if start == None:
            start = min(A[i][0], B[j][0])
        if A[i][0] <= B[j][1] <= A[i][1]:
            j += 1
        elif B[j][0] <= A[i][1] <= B[j][1]:
            i += 1
        else:
            if A[i][1]<B[j][1]:
                c.append((start,A[i][1]))
                i += 1
            elif A[i][1]>B[j][1]:
                c.append((start, B[j][1]))
                j += 1
            else:
                c.append((start, B[j][1]))
                j += 1
                i += 1
            start = None
    if j<len(B):
        return c+B[j:]
    if i<len(A):
        return c+A[i:]
    return c

def main():
  a=[(1,6),(10,20),(38,42),(45,80)]
  b = [(8,15),(18,43),(82,98)]
  print(conn(a,b))

if __name__ == '__main__':
    main()
