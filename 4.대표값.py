import sys
#sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))
#avg = round(sum(a)/n) #round half even 방식 -> 짝수쪽으로 근사값 취함
avg = sum(a)/n
avg = avg+0.5
avg = int(avg)
min = 1e9
for idx, x in enumerate(a):
    tmp = abs(x-avg)
    if tmp<min:
        min = tmp
        score = x
        res = idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1

print(avg, res)