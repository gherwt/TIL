## 스택 자료구조

- 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조이다.
    먼저 입력된 데이터가 나중에 출력 -> 박스 쌓기 예시를 생각하자.

- **입구와 출구가 동일**한 스택을 시각화할 수 있다.

### 스택 동작 예시

stack 구조 예시

```
삽입(5) -> 삽입(2) -> 삽입(3) -> 삽입 (7)

5237

삭제()

523

삽입(1) -> 삽입(4)

52314

삭제()

5321
```

### 파이썬을 활용한 stack 구조 -> 리스트를 활용

```
stack = [] # 빈 리스트 만들기

# append : 리스트 최상단에 삽입 
# pop : 리스트 최상단 요소 삭제

stack.append(5) # [5]
stack.append(2) # [5, 2]
stack.append(3) # [5, 2, 3]
stack.append(7) # [5, 2, 3, 7]
stack.pop() # [5, 2, 3]
stack.append(1) # [5, 2, 3, 1]
stack.append(4) # [5, 2, 3, 1,4 ]
stack.pop() # [5, 2, 3, 1]

print(stack[::1]) -> [1, 3, 2, 5] 
# 최상단 원소부터 출력, 순서를 뒤집어서 출력, 가장 늦게 들어온 원소부터

pring(stack) -> [5, 2, 3, 1] 

# 최하단 원소부터 출력, 그대로 출력
```

### C++ 이용한 스택 구현 예제

```
# include <bits/stdc++.h>

using namespace std;

stack<int> s;

int main(void) {
    s.push(5);
    s.push(2);
    s.push(3);
    s.push(7);
    s.pop;
    s.push(1);
    s.push(4);
    s.pop;
// 스택의 최상단 원소부터 출력하기
    while (!s.empty()){
        cout << s.top() >> '';
        s.pop();
    }
}
```

### 스택 구현 예제(Java)

```
import java.util.*;
public class Main {
    public static void main(Stromg[] args) {
        Stack<Integer> s = new Stack<>();
        s.push(5);
        s.push(2);
        s.push(3);
        s.push(7);
        s.pop;
        s.push(1);
        s.push(4); 
        s.pop;
        // 스택의 최상단 원소부터 출력
        while (!s.empty()){
            System.out.print(s.peek() + " ");
            s.pop();
        }
    }
}

```

## 큐 자료 구조

- 먼저 들어온 데이터가 먼저 나가는 (선입선출)의 자료 구조이다.
- 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있다.
  - 차례대로 처리한다. 일종의 대기열    


### 큐 동작 예시

```
삽입(5) -> 삽입(2) -> 삽입(3) -> 삽입 (7)

7325

삭제()

732

삽입(1) -> 삽입(4)

41732

삭제()

4173
```


### 파이썬을 사용한 큐 구현 예제


```
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용

queue = deque()

# 삽입(5) -> 삽입(2) -> 삽입(3) -> 삽입(7) -> 삭제() -> 삽입(1) -> 삽입(4) -> 삭제()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력  deque([3, 7, 1, 4])
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력 deque([4, 1, 7, 3])
```

deque 를 사용하지 않으면 특정 인덱스 내의 자료를 꺼내 순서를 조정해야하기 때문에 추가적으로 k 만큼의 시간 복잡도가 발생하기 때문에 시간 효율성을 위해서 deque 를 사용해주는 것이 파이썬에서는 좋다.


### C++ 이용한 큐 구현

```
# include <bits/stdc++.h>

using namespace std;

queue<int> s;

# 삽입(5) -> 삽입(2) -> 삽입(3) -> 삽입(7) -> 삭제() -> 삽입(1) -> 삽입(4) -> 삭제()

int main(void) {
    q.push(5);
    q.push(2);
    q.push(3);
    q.push(7);
    q.pop;
    q.push(1);
    q.push(4);
    q.pop;

// 먼저 들어온 원소부터 추출
    while (!s.empty()){
        cout << q.front() >> '';
        q.pop();
    }
}

## 3713 이 도출한다.
```

### 큐 구현 Java

```
import java.util.*;

public class Main {

    public static void main(Stromg[] args) {
        Queue<Integer> q = new LinkedList<>();

        # 삽입(5) -> 삽입(2) -> 삽입(3) -> 삽입(7) -> 삭제() -> 삽입(1) -> 삽입(4) -> 삭제()
        q.offer(5);
        q.offer(2);
        q.offer(3);
        q.offer(7);
        q.poll;
        q.offer(1);
        q.offer(4); 
        q.poll;
        // 스택의 최상단 원소부터 출력
        while (!q.isEmpty()){
            System.out.print(q.poll() + " ");
        }
    }
}

## 3713 이 도출한다.
```