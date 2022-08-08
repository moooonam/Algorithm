a, b, c= map(int, input().split())


if b>=c:
    print(-1)
else:
    print(a//(c-b)+1)
    
#처음엔 1씩 더해가면서 하는 반복문을 생각했지만 시간 초과가 떠서
#수학적으로 풀이를 훨씬 줄였따

    
    

