## 정렬(sorting)

- 데이터를 특정한 기준에 따라 순서대로 나열하는 것을 말한다.
- 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용된다.
  
### 선택 정렬

- 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복하는 것
- 매번 선형 탐색을 실시한다.

#### 선택 정렬 python

```
for i in ragne(len(array)):
    min_index = i # i 를 최소값으로 지정
    for j in range(i+1, len(array)): 
        if array[min_index] > array[j]: 
        # j값이 더 작으면 j를 최솟값으로 바꿔줌
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 최소값과 i 의 자리를 바꿔준다.

print(array)

```

#### 선택 정렬 C++

```
# include <bits/stdc++.h>

using namespace std;

int n = 10;
int target[10] = {2, 5, 4, 3, 1, 8, 9, 6, 7, 0};

int main(void) {
    for (int i = 0; i < n; i++) {
        int min_index = i;
        for (int j = i + 1; j < n; j++) {
            if (target[min_index] > target[j]) {
                min_index = j;
            }
        }
        swap(targetp[i], target[min_index]);
    }
    for (int i = 0; i < n; i++) {
        cout << target[i] << ' ';
    }
    return 0;
}

```

#### 선택정렬 java

```
import java.util.*;

public class Main {

    public static void main(Stromg[] args) {
        int n = 10;
        int[] arr = {2, 5, 4, 3, 1, 8, 9, 6, 7, 0};    
        
        for (int i = 0; i < n; i++) {
            for min_index = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[min_index] > arr[j]) {
                    min_index = j;
                }
            }           
    
            int temp = arr[i];
            arr[i] = arr[min_index];
            arr[min_index] = temp;
        }
        for (int i = 0; i < n; i++) {
        System.out.print(arr[i] + " ");
        }
    }
}
```

#### 선택 정령의 시간 복잡도

선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다.

구현 방식에 따라서 사소한 오차는 있을 수 있지만, 전체 연산 횟수는 

> N + (N - 1) + (N - 2) + ..... + 2
> (N^^2 + N - 2)/2 이다.

### 삽입정렬

- 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입힌다.
- 선택 정렬에 비해 구현 난이도는 높지만, 더 빠르다.
- 매번 위치를 바꿔가면서 위치를 찾는 것임.

#### 삽입 정렬 python

```
for i in ragne(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하면서 반복
        if array[j] > array[j-1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
    else: # 자기보다 작은 데이터를 만나면 그 자리에서 멈춤.
        break
print(array)

```

#### 삽입 정렬 C++

```
# include <bits/stdc++.h>

using namespace std;

int n = 10;
int target[10] = {2, 5, 4, 3, 1, 8, 9, 6, 7, 0};

int main(void) {
    for (int i = 1; i < n; i++) {
        for (int j = i; j > n; j--) {
            if (target[j] < target[j - 1]) {
                swap(targetp[j], target[j - 1]);
            }
            else break;
        }
    }    
    for int(int i = 0; i < n; i++) {
        cout << target[i] << ' ';
    }   
    return 0;
}
```

#### 삽입 정렬 java

```
import java.util.*;

public class Main {

    public static void main(Stromg[] args) {
        int n = 10;
        int[] arr = {2, 5, 4, 3, 1, 8, 9, 6, 7, 0};    
        
        for (int i = 1; i < n; i++) {
            for (int j = i; j > 0; j--) {
                if (arr[j] < arr[j - 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j - 1];
                    arr[j - 1] = temp;

                }
                else break;
            }           
    
        }
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
```

#### 삽입 정렬 시간복잡도

- 삽입 정렬의 복잡도는 O(N^^2)이며, 선택 정렬과 마찬가지로 반복문이 2 번 중첩되어 사용된다.

- 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다.
  - 최선의 경우 O(N)의 시간 복잡도를 가진다