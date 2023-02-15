# 이진 탐색 트리 구현
# 전역변수 선언
memory = []
root = None
nameArr = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

class TreeNode:
    def __init__(self) -> None:
        self.left = None
        self.data = None
        self.right =None

if __name__=='__main__':
    node= TreeNode()
    node.data = nameArr[0]
    root= node
    memory.append(node)

    for name in nameArr[1:]:
        node =TreeNode()
        node.data = name

        current = root

        while True:
            if name < current.data :      # 부모노드의 왼쪽으로 
                if  current.left == None:
                    current.left =node
                    break
                current = current.left
            else:                        # 부모노드의 오른쪽으로
                if current.right == None:
                    current.right= node
                    break
                current = current.right
        memory.append(node)

    print('이진 탐색 트리 구성 완료')
    print(root.data)
    print('｜         ＼')
    print(root.left.data,'   ',root.right.data)
    print('｜   ＼       ｜    ＼')
    print(root.left.left.data, '', root.left.right.data, ' ', root.right.right.data )
    
    search = input('찾을 걸그룹 입력 > ')

    current = root
    while True:
        if search ==current.data :
            print(search, '찾음 끝')
            break
        elif search <current.data :
            if current.left == None:
                print('못찾음')
                break
            else:
                current =current.left
        else:
            if current.right == None:
                print('못찾음')
                break
            else:
                current =current.right
    