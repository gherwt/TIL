### 예제1

- python 프로그램을 생성
- python 프로그램을 실행하는 sh 명령을 task 등록

1. python 프로그램 : 빈 csv 파일을 저장하는 프로그램이다.
2. 1번 프로그램을 1분에 한 번씩 실행되도록 schedule interval 설정
    - 스페줄 파일 : ~ dag.py => /root/study/dags 저장
    - python 프로그램(응용) : 저장 디렉터리 상관없음

```py
### airflow test용 프로그램
### 빈 csv 파일을 생성하는 프로그램
### airflow schedule 에 등록해서 1분에 한번씩 생성되게함
### 파일 이름을 구별하기 위해서 test+id.csv로 파일명을 생성할 예정임

from datetime import datetime # 시간 data 는 매번 변경되므로 id 로 사용할 수 있다.

# 함수로 구성하겠다.
def result():
    dt = datetime.now() # 함수 호출 후 코드가 실행되는 시점의 시간숫자
    t_id = str(dt.microsecond)
    f = open('/root/study/test/test'+t_id+'.csv', 'w') # 쓰기 파일 열기
    f.close() # 바로 닫으면서 빈파일 생성

if __name__  == '__main__': # if 문이 참이 되는 경우 make_csv.py 파일 자체를 실행했을 때
    result() # 본프로그램의 일부코드인 result() 를 호출하면 if 는 false가 되어서 실행되지 않는다.
```

### sh 파일을 생성해서 터미널 명령어를 실행시킬 수 있다

- sh /root/study/test/make_csv.py

- 간접적으로 부를 파일이 여러 개라면, 쉘을 이용해서 간접으로 실행해주는 것이다.

### 예제 2

- 

```py
# /root/study/test/make_csv.py 실제 작업코드임
# /root/study/test/make_csv.sh py 프로그램을 실행시켜주는 명령코드 - 작업으로 등록해서 py가 실행되게 진행함

from datetime import timedelta
from airflow import DAG
from airflow.operator.bash import BashOperator
from airflow.utils.dates import days_ago # 상대적으로 이전 날짜 명시가능한 속성

args = {
    'owner' : 'admin',
}

dag = DAG(
    dag_id = 'exp_basOp',
    default_args = args,
    start_date = days_age(2), # default_args에 등록해도됨
    dagrun_timeout = timedelta(minute=1),
    schedule_interval = timedelta(minute=1)
)

tmp_cmd = """
    sh /root/study/test/make_csv.sh
"""

run_n = BashOperator(
    task_id = 'Bash_test',
    bash_commmand = tmp_cmd,
    dag = dag
)

if __name__ == '__main__':
    dag.cil() # dag command line linterface dag 객체 생성 cmd 명령이 전달된다.
```

### 예제3

```py
# name.py

def sum(a, b):
    return(a+b)

if __name__ == '__main__':
    print(__name__)
    print(sum(9, 7), '모듈 내 test')

# main.py
import name

print(name.sum(9, 7))
```
