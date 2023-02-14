# 스택 전체 구현
# glibal  변수 
SIZE = 0
stack = []
top = -1

# 스택이 꽉 찼는지 여부 확인
def isStackFull():
    global SIZE, stack, top   # 전역변수를 그대로 함수에서 쓸래 

    if (top >= SIZE-1 ):
        return True
    else:
        return False

# 스택이 비어있는지 여부 확인
def isStackEmpty():
    global SIZE, stack, top  

    if (top == -1 ):
        return True
    else:
        return False

# 스택에서 데이터 삽입 
def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        print('Stack if Full')   
    else:
        top+=1
        stack[top] = data

# 스택에서 데이터 추출
def pop():
    global SIZE, stack, top
    if(isStackEmpty()):
        print('Stack is empty')
        return None
    else:
        data= stack[top]
        stack[top] = None
        top -=1
        return data

# top이 데이터 확인
def peek():
    global SIZE, stack, top
    if isStackEmpty():
        print('Stack is empty')
        return None
    else:
        return stack[top]


# 메인 엔트리 
'''
if __name__ == '__main__':
    top=-1
    SIZE = int(input('스택 사이즈 입력 >> ')) 
    stack = [None for _ in range(SIZE)]

    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(X) >>')
        if select.lower()=='x':    # 종료
            break
        elif select.lower()=='i':
            data= input('추가 할 데이터 >> ')
            push(data)
            print(f'스택 상태 :  {stack}')
        elif select.lower()=='e':
            data= pop()
            print(f'추출데이터 : {data}')
            print(f'스택 상태 : {stack}')
        elif select.lower()=='v':
            print(f'확인데이터 : {data}')
            print(f'스택 상태 : {stack}')
        else:
            continue
    print('스택프로그램 종료')
    '''