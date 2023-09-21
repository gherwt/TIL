## css (cascading style sheet)

계단식으로 내려온다 -> 우선 순위에 따라서 자료들을 타고 내려온다.

id, class 로 사용한다

id = 유일한 구분자이다. 다른 요소들과 구분할 수 있는 요소이기 때문에 중복되서는 안된다.

class - 공통적인 속성을 가진다. 같은 소속이다.

앞에 . 을 써서 클래스로 지정해줄 수 있다.


### selector, 선택자

뭘 어떻게 바꿀 것인가? 에 대한 것들

h1{color ; font-size} => 딕셔너리처럼 선언한다.

프로퍼터, property 속성

프리셋으로 저장된 이름들만 사용해야 한다.

`*` :	HTML 문서 내의 모든 요소를 선택한다. html 요소를 포함한 모든 요소가 선택된다. (head 요소도 포함된다)

태그 셀렉터 : 지정된 태그명을 가지는 요소를 선택한다.


#### id 어트리뷰트 

 id 어트리뷰트 값을 지정하여 일치하는 요소를 선택한다. id 어트리뷰트 값은 중복될 수 없는 유일한 값이다. -> 건들지 않아야 하는 셀렉터이다.


#### class 어트리뷰트

 `.class` : class 어트리뷰트 값을 지정하여 일치하는 요소를 선택한다. 

 class 어트리뷰트 값은 중복될 수 있다. -> 동시 적용이 가능하다. 


#### 어트리뷰트 셀렉터 (Attribute Selector) 

 지정된 어트리뷰트를 갖는 모든 요소를 선택한다.


### units

#### px (픽셀)

화소 1개의 크기이다. 

디바이스 별로 픽셀(화소)의 크기는 제각각이기 때문에 픽셀을 기준으로 하는 단위는 명확하지 않다. 

> 대부분의 browser 는 1px 을 1/96 인치의 절대 단위로 인식한다.


인치 -> 디스플레이의 `대각선`을 기준으로 한다.


hd/fhd/qhd/uhd/4k/8k : 해상도, 선명도 , 픽셀이 몇개 있는가?

#### %

백분율 단위의 상대 단위(비율)이다. 요소에 지정된 사이즈에 `상대적인 사이즈`를 설정한다.

#### em

`배수 단위`로 상대 단위. 

요소에 지정된 사이즈에 `상대적`인 사이즈를 설정한다. 

자기를 참조하면서 계속 커지는 모습을 볼 수 있다.

#### rem

em의 기준은 상속의 영향으로 바뀔 수 있다.

언제나 같은 값을 보장할 수 있다.

`rem은 최상위 요소(html)의 사이즈를 기준`으로 삼는다. -> 브라우저 설정 내의 사이즈를 통해 값을 알 수 있다.

rem의 r은 root를 의미한다.

browser 기본 설정 글꼴 크기를 기준으로 한다. 

#### Viewport 단위(vh, vw, vmin, vmax)

|단위|	Description|
|--|--|
|vw|viewport 너비의 1/100|
|vh|viewport 높이의 1/100|
|vmin|	viewport 너비 또는 높이 중 작은 쪽의 1/100|
|vmax|	viewport 너비 또는 높이 중 큰 쪽의 1/100|

왜 중요한가?? 

> 반응형 web design 이기 때문이다. 비율의 중요성이 강조되고 있다.

어느 순간부터 디스플레이의 크기가 다양해졌기 때문에 디자인의 크기를 지정할 수 없게 되었다.

browser 에는 일정한 마진 값이 존재한다.

완벽하게 마진도 삭제할 수 있는 방법도 존재한다. margin : ~~

#### 색상 표현 단위

W3C css3-color,  Color keywords 등 다양한 예시들 있음 참고

- 단위들  
  - RGB (Red, Green, Blue)
  - RGBA (Red, Green, Blue, Alpha/투명도)


### box-model

모든 HTML 요소는 `Box 형태의 영역`을 가지고 있다. 

Box 형태란 물론 사각형을 의미한다.

> 콘텐트(Content), 패딩(Padding), 테두리(Border), 마진(Margin)로 구성

border 까지가 box 

layout을 결정하는 것이기 때문에 중요하다.

|명칭|	설명|
|--|--|
|Content| 요소의 텍스트나 이미지 등의 `실제 내용이 위치하는 영역`이다. width, height 프로퍼티를 갖는다.|
|Padding| 테두리(Border) 안쪽에 위치하는 `요소의 내부 여백` 영역이다. padding 프로퍼티 값은 패딩 영역의 두께를 의미하며 기본색은 투명이다. 요소에 적용된 배경의 컬러, 이미지는 패딩 영역까지 적용된다.|
|Border|테두리 영역으로 border 프로퍼티 값은 `테두리의 두께` 선이기 떄문에 두께를 지정할 수 있다.|
|Margin|테두리(Border) 바깥에 위치하는 `요소의 외부 여백 영역`이다. margin 프로퍼티 값은 마진 영역의 두께를 의미한다. 기본적으로 투명하며 배경색을 지정할 수 없다.|


####  width / height 프로퍼티


width와 height 프로퍼티는 요소의 `너비`와 `높이`를 지정하기 위해 사용된다. 

이때 지정되는 요소의 너비와 높이는 `콘텐츠 영역을 대상`으로 한다.

width와 height 프로퍼티는 콘텐츠 영역을 대상으로 요소의 너비와 높이를 지정하므로 박스 전체 크기는 다음과 같이 계산할 수 있다.

```
전체 너비
width + left padding + right padding + left border + right border + left margin + right margin

전체 높이
height + top padding + bottom padding + top border + bottom border + top margin + bottom margin
```

block 요소의 경우, 

width는 부모 요소의 100% --> 중요/ 기본적으로 선은 지속되려는 성질 1차원의 line 과 연결되는 특성

height는 콘텐츠의 높이(+ 약간의 여분)가 지정 알아서 지정된다.

물론 조정도 가능하다.


####  margin / padding 프로퍼티


4개방향으로 지정 가능하다.(top, right, left, bottom)

- 지정한 값이 4개일 때

보통 방향은 시계 방향으로 지정한다.

- 지정한 값이 2개일 때

앞이 상하, 뒤가 좌우

-지정한 값이 1개일 때

상하좌우 모두 같은 1개 값을 적용해준다.


#### border 프로퍼티

border-style 프로퍼티는 테두리 선의 스타일을 지정한다.

border-radius -> 원을 만드는 것 border가 끝을 깍아내서 만드는 것임.


#### box-sizing 프로퍼티

box-sizing 프로퍼티는 width, height 프로퍼티의 대상 영역을 변경할 수 있다.


border-box로 지정하면 마진을 제외한 박스 모델 전체를 width, height 프로퍼티의 대상 영역으로 지정할 수 있어서 CSS Layout을 직관적으로 사용할 수 있게 한다.


|키워드|	설명|
|--|--|
|content-box|	width, height 프로퍼티 값은 content 영역을 의미한다. (기본값)|
|border-box|	width, height 프로퍼티 값은 content 영역, padding, border가 포함된 값을 의미한다.|


### display

|프로퍼티값| 키워드	설명|
|block|block 특성을 가지는 요소(block 레벨 요소)로 지정|
|inline|inline 특성을 가지는 요소(inline 레벨 요소)로 지정|
|inline-block|inline-block 특성을 가지는 요소(inline-block 레벨 요소)로 지정|
|none|	해당 요소를 화면에 표시하지 않는다 (공간조차 사라진다)|

#### block 레벨 요소

```
div
h1 ~ h6
p
ol
ul
li
hr
table
form
```

block = 면, 2차원 요소

1. 욕심이 많아서, 우측 남는자리에 아무것도 허용하지 않음(width 100%가 기본값)

2. 높이(height)는 컨텐트(내용, 안의 값)의 세로와 동일하다.


#### inline 레벨요소

inline => 선이다, 1차원 요소

```
span
a
strong
img
br
input
select
textarea
button
```

1. 선끼리는 자동으로 옆자리로 오는 특성이 있다.
2. browser 화면 가로폭(vw)끝에 도달할 때가지 계속 이어진다.
3. 상하 margin, padding 이 없다. 좌우는 있어서 지정 가능하다.
4. 상, 하 여백은 line-height로 지정한다.
5. 당연히 border는 없다.
6. 선은 중앙 기준을 잡을 수가 없다. -> 선을 포함하고 있는 블럭(면)에 중앙 정렬을 해야한다.


#### inline-block 레벨 요소 

block과 inline 레벨 요소의 특징을 모두 갖는다. 

block 이 inline 을 포함하기 때문.

block 인데 한줄로 오는 block 이라고 생각하면 된다.

기본적으로 inline 레벨 요소와 흡사하게 줄을 바꾸지 않고 다른 요소와 함께 한 행에 위치시킬 수 있다.

block 레벨 요소처럼 width, height, margin, padding 프로퍼티를 모두 정의할 수 있다. 

상, 하 여백을 margin과 line-height 두가지 프로퍼티 모두를 통해 제어할 수 있다.

content의 너비만큼 가로폭을 차지한다.

inline-block 레벨 요소 뒤에 공백(엔터, 스페이스 등)이 있는 경우, 정의하지 않은 space(4px)가 자동 지정된다. -> 물리적으로 붙여주면 이 공백을 삭제할 수 있다.

## 개구리 옮기기 게임 flexbox

`https://flexboxfroggy.com/#ko`

무조건 주-축 기준으로 정렬.

### justify-content 

주축 전체가 이동

around: 주변의 거리가 똑같아짐

between: 중간 간격이 똑같아

### align-items

교차축 전체가 이동

### flex-direction: 주 축을 지정해주는 것

- reverse : 주 축의 시작점이 변경된다.
- column: 주와 교차가 바뀌는 것

### order 

순서를 뒤집는다. 필요에 따라서 순서를 부여할 수 있다.

지정된 요소에 부여하는 것임.

기본값은 0이다.

### align-self

지정된 요소만 이동

### flex - flow

flex-direction과 flex-wrap이 자주 같이 사용되기 때문에 합쳐준 것들

### align-content

교차축을 움직여준다. wrap 에서 같이 사용한다.


