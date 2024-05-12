def reversiv(N,a):
    lst=[]
    for i in range(len(a)):
        if i<=N:
            lst.append(a[i])
    lst = a[N+1:]+lst
    return lst

a = [1,2,3,4,5,6,7]
N = int(input())
print(reversiv(N,a))
# lst = a[len(a)-N:]+a[N:]