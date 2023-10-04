## 우선순위에 따라 데이터를 꺼내는 자료구조

### 우선 순위 큐

- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조.
- 데이터를 우선순위에 따라 처리하고 싶을 때 사용한다.
    물건 데이터를 자료구조에 넣었다가 가치가 높은 물건부터 꺼내서 확인하는 경우

|자료구조|추출되는 데이터|
|---|---|
|스택(stack)|가장 나중에 삽입된 데이터|
|큐(Queue)|가장 먼저 삽입된 데이터|
|우선순위 큐(Priority Queue)|가장 우선 순위가 높은 데이터|

- 리스트를 이용하여 구현할 수 있다.
- 힙(heap)을 이용하여 구현할 수 있다.
  데이터가 n개일 때, 구현방식에 따라 시간 복잡도가 다르다.
    - 리스트 : 최대 n, 선형적인 방식
    - 힙 : 데이터를 삽입하고 삭제하는 정렬은 모두 동일하게 작동

### 힙(heap)의 특징

- 완전 이진 트리 자료구조의 일종입니다.
  - 완전 이진 트리란? 
    - 루트(root) 노드부터 시작하여 왼쪽 자식노드, 오른쪽 자식 노드 순서대로 데이터가 차례대로 삽입되는 트리(tree)를 의미한다. 

![이진트리](%EC%9D%B4%EC%A7%84%ED%8A%B8%EB%A6%AC.jpg)

- 힙에서는 항상 루트 노드(root node)를 제거한다.

- 최소 힙
  - 루트 노드가 가장 작은 값을 가집니다.
  - 따라서 값이 작은 데이터가 우선적으로 제거됩니다.

- 최대 힙
  - 루트 노드가 가장 큰 값을 가집니다.
  - 따라서 값이 큰 데이터가 우선적으로 제거됩니다.
 
- 최소 힙 구성함수(Min-Heapify())
    (상향식) 부모 노드로 거슬로 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치를 교체합니다.

- 힙에 새로운 원소가 삽입될 때 o(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있다.

- 힙에서 원소를 제거할 때 O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있다.
    원소를 제거할 떄는 가장 마지막 노드가 루트 노드의 위치에 오도록 한다.
    이후에 루트노드에서부터 하향식으로(더 작은 자식 노드로) Heapify()를 진행한다.


### 우선순위 큐 라이브러리를 활용한 힙 정렬 구현 예제(python)

```
import sys
import heapq
input =  sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(hepq.heappush(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res =  heapsort(arr)

for i in range(n):
    print(res[i])
```


### 우선순위 큐 라이브러리를 활용한 힙 정렬 구현 예제(c++)

```
#include <bits/stdc++.h>

using namespace std;

void heapSort(vector<int>&arr) {
    priority_queue<int> h;
    // 모든 원소를 차례대로 힙에 삽입
    for (int i = 0; i <arr.size(); i++) {
        h.push(-arr[i]);
}
    // 힙에 삽입된 모든 우너소를 차례대로 꺼내어 출력
    while (!s.empty()){
        printf("%d\n", -h.top());
        h.pop();
    }
}

int n;
vector<int> arr;

int main() {
    cin >> n
    for (int i = 0; i < n; i++) {
    int x;
    scanf("%d", &x);
    arr.push_back(x);
    }
    heapSort(arr);
}
```