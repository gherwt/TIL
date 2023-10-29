## Matplotlib

- 시각화 패키지

- 파이썬 표준 시각화 도구로 불림

- 2D 평면 그래프에 관한 다양한 포맷과 기능 지원

- 데이터 분석 결과를 시각화 하는데 필요한 다양한 기능을 제공


```
#그래프 패키지 모듈 등록
import matplotlib.pyplot as plt 
%matplotlib inline 
#그래프는 show()함수를 통해서 독립창에서 실행되는 것이 원칙
#그래프를 콘솔에서 바로 작도되록 하는 설정
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"
import pandas as pd
import numpy as np
```

### 패키지 사용 법

1. matplotlib 주 패키지 사용시 

  - import matplotlib as `mpl`
    
2. pylab 서브 패키지 사용시 : 주로 사용 한다.

  - import matplotlib.pyplot as `plt`

- 매직 명령어 `%matplotlib inline `
  
    - 주피터 노트북 사용시 노트북 `내부에 그림을 표시`하도록 지정하는 명령어
    

- 지원 되는 플롯 유형


    - 라인플롯(line plot) : plot()

    - 바 차트(bar chart) : bar()

    - 스캐터플롯(scatter plot) : scatter() 

    - 히스토그램(histogram) : hist()

    - 박스플롯(box plot) : boxplot()

    - 파이 차트(pie chart) : pie()

    - 기타 다양한 유형의 차트/플롯을 지원 : 관련 홈페이지를 참고
  
### 그래프 용어 정리

![그래프 용어 정리](attachment:image.png)

   
### 함수설명 

#### 라인 플롯 : plot()

- 기본으로 `선을 그리는 함수`

- 데이터가 시간, 순서 등에 따라 변화를 보여주기 위해 사용
    
    
- show()
  
    - 각화명령(그래프 그리는 함수) 후 `실제로 차트로 렌더링` 하고 마우스 이벤트등의 지시를 기다리는 함수
  
    - 주피터 노트북 에서는 셀 단위로 플롯 명령을 자동으로 렌더링  주므로 show 명령이 필요 없지만, 일반 파이썬 인터프리터(파이참)로 가동되는 경우를 대비해서 항상 마지막에 실행하도록 함.


- 관련 함수 및 속성    
    - figure(x,y) : 그래프 크기 설정 : 단위 인치
    - title() : 제목 출력
    - xlim : x 축 범위
    - ylim : y 축 범위
    - xticks():yticks() : 축과 값을 잇는 실선    
    - legend() : 범례
    - xlabel() : x축라벨(값)
    - ylabel() : y축라벨(값)
    - grid() : 그래프 배경으로 grid(격자선) 사용 결정 함수
    
    
- line plot 에서 자주 사용되는 스타일 속성
   *  color: c(선색깔)
   *  linewidth : lw(선 굵기)
   *  linestyle : ls(선스타일)
   *  marker : 마커 종류
   *  markersize : ms(마커크기)
   *  markeredgecolor : mec(마커선색깔)
   *  markeredgewidth : mew(마커선굵기)
   *  markerfacecolor : mfc(마커내부색깔)   
 
- plt.plot([]) 기본 문법 : []에 y 축값, x축값은 자동 생성

#### 그래프 크기설정 및 선 색상설정

- 색상은 단어로 지정 : color ='green'

t=[0,1,2,3,4,5,6]
y=[1,4,5,8,9,5,3]

- linestyle
  
![image.png](attachment:image.png)

- marker 
![image.png](attachment:image.png)

- 라인스타일 기호 지정
![image.png](attachment:image.png)

#### 그래프 그리기

```
# 선 스타일 설정 직선
# 색상은 단어로 지정 : color='green'
t = [0, 1, 2, 3, 4, 5, 6]
y = [1, 4, 5, 8, 9, 5, 3]

plt.plot(t, y, color='green', linestyle='-')
plt.xlabel('x축')
plt.ylabel('y축')
plt.title('선 그래프')
plt.show()
```

```
# 선 스타일 설정 점선
# 색상은 단어로 지정 : color='green'
t = [0, 1, 2, 3, 4, 5, 6]
y = [1, 4, 5, 8, 9, 5, 3]

plt.plot(t, y, color='green', linestyle='--')
plt.xlabel('x축')
plt.ylabel('y축')
plt.title('점선 그래프')
plt.show()
```

```
# 색상은 단어로 지정 : color='green'
t=[0,1,2,3,4,5,6]
y=[1,4,5,8,9,5,3]

plt.plot(t, y, color='green')
plt.xlabel('x축')
plt.ylabel('y축')
plt.title('점선 그래프')
plt.show()
```

```
# 색상은 단어로 지정 : color='green'
# markerfacecolor : 마커 색상, markerfacecolor : 마커 크기
t = [0, 1, 2, 3, 4, 5, 6]
y = [1, 4, 5, 8, 9, 5, 3]

plt.plot(t, y, color='green', marker='o', markerfacecolor='blue', markersize=10)
plt.xlabel('x축')
plt.ylabel('y축')
plt.title('마커가 있는 선 그래프')
plt.show()
```

- 스타일을 약자로 표시 

- color(c) : 선색깔
- linewidth(lw) : 선굵기
- linestyle(ls) : 선스타일

- marker : 마커의 종류
- markersize(ms) : 마커의 크기
- markeredgecolor(mec) : 마커 선 색깔
- markeredgewidth(mew) : 마커 선 굵기
- markerfacecolor(mfc) : 마커 내부 색깔

- 여러 데이터를 하나의 그래프에 여러 선 으로 표현
    - plot() 여러번 사용 가능
   
- 여러개의 선 그리기 : plot() 여러번 사용

```
t = np.arange(0., 5., 0.2)
y1 = np.sin(t)
y2 = np.cos(t)
y3 = np.tan(t)

plt.plot(t, y1, color='red', label='sin(t)')
plt.plot(t, y2, color='blue', label='cos(t)')
plt.plot(t, y3, color='green', label='tan(t)')
plt.xlabel('x축')
plt.ylabel('y축')
plt.title('여러 개의 선 그리기')
plt.legend()
plt.show()
```

- 위 그래프 코드를 plot() 하나로 한번에 표현하기

```
t = np.arange(0., 5., 0.2)
y1 = np.sin(t)
y2 = np.cos(t)
y3 = np.tan(t)

y = np.stack((y1, y2, y3))

plt.plot(t, y, color='red', linestyle='-', marker='o', markerfacecolor='blue', markersize=10)
plt.xlabel('x축')
plt.ylabel('y축')
plt.title('여러 개의 선 그리기')
plt.show()

```
