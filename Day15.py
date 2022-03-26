lst = [1,5,2,7,3,4]


def max(n):
    a=0
    for i in range(len(n)):
        if n[i] > n[a]:
            a = i
    return a+1

print(max(lst)) 