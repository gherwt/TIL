#### tick 설정

- tick은 축상의 위치 표시 지점-축에 간격을 구분하기 위해 표시하는 눈금

- xticks([x축값1,x축값2,...]) #튜플,리스트등 이용해서 축 값(위치 나열)
- yticks([y축값1,y축값2,...]) #튜플,리스트등 이용해서 축 값(위치 나열)
- tick_params()
- tick label(눈금 레이블) : tick에 써진 숫자 혹은 글자
x=[10,20,30,40,50,60]
y=[11,15,40,40,20,10]

- 눈금 레이블 지정
# 눈금 레이블 지정

x=[10,20,30,40,50,60]
y=[11,15,40,40,20,10]



x=[10,20,30,40,50,60]
y=[11,15,40,40,20,10]

- 그래프 제목 및 축 레이블 설정
    - plot.title(data,loc=, pad=, fontsize=)
        - loc= 'right'|'left'| 'center'| 'right'로 설정할 수 있으며 디폴트는 'center'
        - pad=point 은 타이틀과 그래프와의 간격 (오프셋)을 포인트(숫자) 단위로 설정
        - fontsize=제목폰트크기
        
    - plot.xlabel()
    - plot.ylabel()
# 그래프 제목 x축 y축 라벨 

x=[10,20,30,40,50,60]
y=[11,15,40,40,20,10]
# plt.title('그래프제목')
# plt.title('그래프제목', loc='right')
# plt.title('그래프제목', loc='right', pad=30)


#### 그래프 Title 폰트 관련 지정

- 딕셔너리형식으로 fontsize 및 fontwegith 등 지정 가능


- plot.grid(True) : 배경 그리드 표지
# 배경 그리드 표현

x=[10,20,30,40,50,60]
y=[11,15,40,40,20,10]


#### subplot() : 하나의 윈도우(figure)안에여러개의 플롯을 배열 형태로 표시
    - 그리드 형태의 Axes 객체들 생성

- 형식 : subplot(인수1,인수2,인수3)
- 인수1 과 인수2는 전체 그리드 행렬 모양 지시
- 인수3 : 그래프 위치 번호


    - subplot(2,2,1) 가 원칙이나 줄여서 221로 쓸 수 있음
    - subplot(221) 2행 2열의 그리드에서 첫번째 위치
    - subplot(224) 2행 2열의 그리드에서 마지막 위치
    
    
- tight_layout(pad=) : 플롯간 간격을 설정
    - pad = 간격값(실수)
# 2 x 2 형태의 네개의 플롯

np.random.seed(0) # 항상 같은 난수가 발생


- plt.subplots(행,열)

    - 여러개의 Axes 객체를 동시에 생성해주는 함수
    - 행렬 형태의 객체로 반환
    
    
   - 두개의 반환값이 있음 : 
        - 첫번 째 반환은 그래프 객체 전체 이름 - 거의 사용하지 않음
        - 두번 째 반환값에 Axes 객체를 반환 함
        - 두번 째 반환값이 필요하므로 반환 값 모두를 반환받아 두번 째 값을 사용해야 함
        
        - ex. fig, axes = plt.subplots(2,2)
        
#subplots() : 여러개의 Axes 객체 동시 생성해주는 함수


#### plot 함수 응용 예제
- numpy 모듈의 sin()함수를 이용하여 sin 곡선 그래프 그리기
# data 생성

t=np.arange(0,12,0.1) 
#arange(시작, 끝값+간격, 간격)
#시작값부터 끝값 - 간격까지 순서대로 수를 생성
t
# sin 값 생성
y=np.sin(t)

#위 그래프에 x,y 축 제목, 그래프 제목, 격자무늬를 표시하시오.
#x축 : time
#y축 : Amplitude
#그래프 제목 : Example of sinewave

#np.sin() : sin 값을 계산후 반환
#np.cos() : cos 값을 계산 후 반환

#위쪽 그래프에 cos 곡선을 추가하는 코드를 작성하시오.
#cos 곡선의 색상은 빨간색으로 설정 할 것

#### 범례(legend)표시
- plot에 label 속성이 추가되어 있어야 함
    - plt.plot(x,y,label='a')
- plt.legend(loc=, ncol= ) #범례표시, 
- loc = 1/2/3/4/5/6/7/8/9/10 # 범례표시 위치값
- loc = (x,y)
- ncol= 열갯수
![image.png](attachment:image.png)
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label='Demand (#)')


- 세로 막대 그래프 그리기: bar()
    - bar(x,y,color=[],alpha=)
    - color = [] : 색상값 설정
    - alpha = 투명도 설정
y=[2,3,1,4]
x=np.arange(len(y))
z=[2,3]
s=[0,1]

e=[1,4]
h=[2,3]

xlabel=['가','나','다','라']


np.random.seed(0)
people=['몽룡','춘향','방자','향단']
y=np.arange(len(people))
#np.arange(4) : 0-4사이의 정수를 순서적으로 추출
#0,1,2,3
#np.random.rand(4) : 0-1사이의 난수를 4개 추출
#array([0.5488135 , 0.71518937, 0.60276338, 0.54488318])
# a=np.random.rand(len(people))
# a=np.random.rand(4)
# a

performance = 3+ 10 * np.random.rand(len(people))
#seed 고정되었을 경우 rand()함수를 여러번 사용하면
#사용할때마다 다른 난수가 발생한다.
#단, 특정함수를 여러번 실행시켜도 결과는 동일하다.
np.random.seed(0)
print(np.random.rand(4))
print(np.random.rand(4))
print(np.random.rand(4))
- 가로 막대 그래프 그리기
    - barh(x,y,color=[], alpha=)
np.random.seed(0)
people=['몽룡','춘향','방자','향단']
y=np.arange(len(people))
performance = 3+ 10 * np.random.rand(len(people))

#데이터 프레임으로 바 그래프 그리기 1
df1 = pd.DataFrame({
    '나이':[15,20,17,50,2,30,23],
    '이름':['둘리','도우너','또치','길동','희동','마이클','영희']
},columns=['나이','이름'])
# df1

x=[0,1,2,3,4,5,6,7] #xticks 시 위치 표시에 사용할 변수

#df로 막대그래프 그리기 첫번째 방법

#데이터 프레임으로 바 그래프 그리기 1-1
#열 지정없이 그래프를 그리면
#수치 데이터가 있는 모든 필드를 이용해서 묶음 막대 그래프를
#그리게 된다.
df1 = pd.DataFrame({
    '나이':[15,20,17,50,2,30,23],
    '키' : [165,150,151,175,80,175,185],
    '이름':['둘리','도우너','또치','길동','희동','마이클','영희']
},columns=['나이','키','이름'])
# df1

x=[0,1,2,3,4,5,6,7] #xticks 시 위치 표시에 사용할 변수

#df로 막대그래프 그리기 첫번째 방법

#데이터프레임으로 바 그래프 그리기 1-2
df1 = pd.DataFrame({
    '나이':[15,20,17,50,2,30,23],
    '키' : [165,150,151,175,80,175,185],
    '이름':['둘리','도우너','또치','길동','희동','마이클','영희']
},columns=['나이','키','이름'])


#데이터프레임의 일부 필드를 데이터프레임으로 추출해서
#그래프 그리기
df1 = pd.DataFrame({
    '나이':[15,20,17,50,2,30,23],
    '키' : [165,150,151,175,80,175,185],
    '이름':['둘리','도우너','또치','길동','희동','마이클','영희']
},columns=['나이','키','이름'])
# df1

x=[0,1,2,3,4,5,6,7] #xticks 시 위치 표시에 사용할 변수


#데이터프레임의 일부 필드를 데이터프레임으로 추출해서
#그래프 그리기
df1 = pd.DataFrame({
    '나이':[15,20,17,50,2,30,23],
    '이름':['둘리','도우너','또치','길동','희동','마이클','영희']
},columns=['나이','이름'])
# df1

a=[0,1,2,3,4,5,6,7] #xticks 시 위치 표시에 사용할 변수

스캐터 플롯(scatter plot) : scatter()
#분산형 그래프
t = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([9,8,7,9,8,3,2,4,3,4])


#버블차느 : 점 하나의 크기 또는 색상을 이용해서 서로 다른 데이터 값을 표시하는 그래프
#s 인수 : size
#c 인수 : color
N=30
np.random.seed(0)
x=np.random.rand(N)
y1 =np.random.rand(N)
y2 =np.random.rand(N)
y3=np.pi *(15 * np.random.rand(N))**2

#color map 을 이용해서 그래프 그리기
colormap = t


4. 히스토그램 : hist()
np.random.seed(0)
x=np.random.randn(1000) #난수 1000개 발생
# x

5.박스플롯 : boxplot()
#다차원 array 형태로 무작위 샘플을 생성
#np.random.normal(정규분포평균,표준편차,(행열) or 개수)
#정규분포 확률 밀도에서 표본 추출해주는 함수

#데이터 3개 생성
s1=np.random.normal(loc=0,scale=1,size=1000)
s2=np.random.normal(loc=5,scale=0.5,size=1000)
s3=np.random.normal(loc=10,scale=2,size=1000)
#line 그래프 이용해서 데이터 차이 확인

#박스 그래프

6.파이차트:pie()
#카테고리 별 값의 상대적인 비교를 할때 주로 사용하는 차트
#원의 형태를 유지할 수 있도록 다음 명령을 실행해야 함.
#콘솔에서는 별 다른 변화 없음. plot 창에서는 필요함
#plt.axis('equal')

#예제 데이터 생성
labels=['개구리','돼지','개','통나무']
size=[15,30,45,10]
colors=['yellowgreen','gold','lightskyblue','lightcoral']
explode=(0,0.4,0,0.5)