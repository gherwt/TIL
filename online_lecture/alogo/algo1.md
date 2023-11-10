비밀번호: algory@algory
코드: https://cafe.naver.com/algorystudy

파이썬 : 리스트(list) --> 배열(Array)

## 자료구조 : 요리재료 + 다듬는 방법

- 선형 자료구조
  - 리스트
    - 선형리스트(= 순찰리스트) : 배열, 빈틈이 없다.
        장점: 공간 절약된다.(= 비용 절감), 전체 접근 빠름
        단점: 오버헤드가 생긴다.
    - 단순 연결 리스트: Node(= Data + Link)
        장점: 삽입/삭제 시 오버헤드가 발생하지 않는다.
        단점: 공간이 더 필요(= 비용이 비쌈), 전체 접근 느림
        마지막 노드? Link == none
    - 원형 연결 리스트: 마지막 노드 link == head

  - 스택 : 한쪽 막힌 파이프, FIFO(= LILO), push(), pop(), top......
    isStackFull()? top == SIZE-1
    isStackEmpty()? top == -1
    실무 : 함수호출 A() push/pop -> B () push/pop --> C() --> D() return
    괄호검사: ((()())))  스택: error
 
  - 큐
    - 순차 큐(= 일반 큐) : 양쪽 뚫린 파이프, FIFO(= LILO), enQueue(),  deQueue(), front, rear
      isQueueEmpty: front == rear
      isQueueFull: rear == size -1 --> 개선(3가지), 오버헤드()
    - 원형 큐(= 환형 큐) : 꼬리가 다시 머리로 연결되는 큐.
      % SIZE => front = rear = 0, isQueueFull() : rear + 1 == front,
      1칸 사용 못함(특징)

- 비선형 자료구조
  
  - 트리
    - 이진트리
    - (쿼드 트리)
  
  - 그래프 : 개념 위주

## 알고리즘 : 요리법

- 정렬
  - 선택정렬
  - (버블정렬)
  - (퀵 정렬)

- 검색
  - 순차 검색
  - 이진 검색

- 재귀 : 다양한 사례들이 존재한다.

retData = numData[:]

numData[:]: 이것은 numData의 얕은 복사본을 생성

새로운 객체가 생성되고 해당 객체의 요소가 원본 객체와 동일하다는 것을 의미

이진 탐색 트리;

작은 값 왼쪽

큰값 오른쪾
