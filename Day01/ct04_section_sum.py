# 입력 속도를 개선 (주피터는 x )
import sys
input= sys.stdin.readline      # 이부분이 없으면 백준은 시간 초과

N, M= tuple(map(int, input().split()))
numbers =list(map(int, input().split()))
sums= [0]     
temp= 0

for i in numbers:
    temp = temp + i            
    sums.append(temp)
   

for i in range(M): 
    x, y = tuple(map(int, input().split()))
    print(sums[y]-sums[x-1])     