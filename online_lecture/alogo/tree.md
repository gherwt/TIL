## 트리(Tree)

- 가계도와 같은 계층적인 구조를 표현할 때 사용할 수 있는 자료 구조이다.
- 기본적으로 트리의 크기가 N 일 때, 전체 간선의 갯수는 N-1 개이다.
  
- 구조
  - 루트노드(root node) : 부모가 없는 최상위 노드
  - 단말노드(leaf node) : 자식이 없는 노드
  - 크기(size) : 트리에 포함된 모든 노드의 개수
  - 깊이(depth) : 루트 노드부터의 거리
  - 높이(height) : 깊이 중 최댓값
  - 차수(degree) : 각노드(자식 방향)의 간선 개수, 연결되어 있는 자식의 수


### 이진 탐색 트리(Binary Search Tree)

- 이진 탐색이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조의 일종
- 특징
  - 왼쪽 자식노드 < 부모노드 < 오른쪽 자식노드
  - 부모 노드보다 왼쪽 자식 노드가 작다.
  - 부모 노드보다 오른쪽 자식 노드가 크다.
  - 모든 노드에 적용되는 특징이다.

- 데이터 조회 가정
  - 현재 노드와 찾는 원소를 비교
  - 찾는 원소가 더 크면 오른쪽, 작으면 왼쪽 이를 찾을 떄까지 반복
  

### 트리의 순회(Tree Traversal)

- 트리 자료구조에 포함된 노드를 특정한 방법으로 한 번씩 방문하는 방법
  - 정보를 시각적으로 확인할 수 있다

- 순회 방법
  - 전위 순회(pre-order traverse) : 루트를 먼저 방문 -> 왼쪽 노드부터 오른쪽 노드로
  - 중위 순회(in-order traverse) : 왼쪽 자식을 방문한 뒤에 루트를 방문 -> 오른쪽 노드로
  - 후위 순회(post-order traverse) : 왼쪽 자식을 방문하고 오른쪽 자식을 방문한 뒤에 루트를 방문 

- 트리의 순회 순서, 코드 정리

`https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=sunkwang0307&logNo=221543896967`


### 트리의 순회 구현 예제(파이썬)

```
class Node:
    def __init__(self), data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회

def pre_order(node):
    print(node.data, end=' ')  # 노드부터 확인
    if node.left_node != None:  # 노드 확인 후 왼쪽 자식부터
        pre_order(tree[node.left_node])
    if node.right_ndoe !=None: # 이후 오른쪽 자식 확인
        pre_order(tree[node.right_ndoe])

# 중위 순회

def in_order(node):
    if node.left_node != None: # 오른쪽 자식을 먼저 확인
        in_order(tree[node.left_node])
    print(node.data, end=' ')  # 오른쪽 확인 후 노드 확인
    if node.right_ndoe != None:  # 노드 확인 후 왼쪽 자식 확인
        in_order(tree[node.right_ndoe])

# 후위 순회

def post_order(node):
    if node.left_node != None:  # 왼쪽 자식 확인
        pre_order(tree[node.left_node])
    if node.right_ndoe !=None: # 왼쪽 확인 후 오른쪽 자식 확인
        pre_order(tree[node.right_ndoe])
    print(node.data, end=' ')  # 마지막으로 노드를 확인

n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node =  input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] =  Node(data, left_node, right_node)

```