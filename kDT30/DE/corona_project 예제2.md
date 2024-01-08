### dag 에 v2 파일 생성

- py 파일을 만들고 실행하는 코드 생성

- corona_project 에 대해 airflow 로 자동화 진행을 한 이유
  - 코로나 현황 데이터를 매일 수집해야 하기 때문
  - 모든 pipline process 에서는 최신 코로나 현황데이터만 반영되어야 한다.

- 인구면적, 다중이용시설, 백신접종 -> 고정 데이터들과 코로나 현황 데이터 간의 관계 데이터를 만들고 있다.
  - 그렇기 때문에 코나 현황 데이터가 최신 데이터만 반영되도록 만들어졌는지를 확인해줘야 한다.

1. corona_extract.py

- 코로나 현황 데이터를 기간이 아닌 특정일에 대한 data 를 추출(코드 반영됨)

2. corona_transform_dw.py

- 코로나 현황 데이터를 기간이 아닌 특정일에 대한 data를 변환 후 저장(코드 반영됨)

3. corona_transform_dm.py

- 4개 함수 각각 최신 코로나 데이터 활용해서 데이터 생성 후 insert 해준다.

```py
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# 스케쥴(DAG)
# with ~ as 구문 사용
# project dag 1 ~ 3 으로 3번 설정 가능

with DAG(
    dag_id = 'corona_etl_v2',
    default_args = {    
        'depends_on_past':False,
        'email' : ['acdbdaqwe@mail.com'],
        'email_on_failure' : False,
        'email_on_retry' : False,
        'retries' : 2, 
        'retries_delay' : timedelta(minutes=5)
    },
    description = 'corona etl pipline',
    schedule_interval = timedelta(days=1),
    start_date = datetime(2024, 1, 5, 13, 00),
    catchup = False, # 문법적 오류 등으로 실행되지 않는 DAG 를 다시 실행할 것인지 여부
    tags = ['corona_etl_v2']

)  as dag:
    t1 = BashOperator(
        task_id = 'extract_corona_api_v2'
        cwd = '/root/study/corona_project'
        bash_command = 'python3 corona_extract.py'
    )

    t2 = BashOperator(
        task_id = 'transDW_corona_api_v2'
        cwd = '/root/study/corona_project'
        bash_command = 'python3 corona_transform_dw.py'
    )

dag.doc_md = """
    This is corona project~
"""

with DAG(
    dag_id = 'corona_etl_fin',
    default_args = {    
        'depends_on_past':False,
        'email' : ['acdbdaqwe@mail.com'],
        'email_on_failure' : False,
        'email_on_retry' : False,
        'retries' : 2, 
        'retries_delay' : timedelta(minutes=5)
    },
    description = 'corona etl pipline',
    schedule_interval = timedelta(days=1),
    start_date = datetime(2024, 1, 8, 13, 00),
    catchup = False, # 문법적 오류 등으로 실행되지 않는 DAG 를 다시 실행할 것인지 여부
    tags = ['corona_etl_fin']

)  as dag:
    t1 = BashOperator(
        task_id = 'extract_corona_api_fin',
        cwd = '/root/study/corona_project',
        bash_command = 'python3 corona_transform_dw.py'
    )

    t2 = BashOperator(
        task_id = 'transDW_corona_api_fin',
        cwd = '/root/study/corona_project',
        bash_command = 'python3 corona_transform_dm.py'
    )

dag.doc_md = """
    This is corona project~
"""

t1 >> t2 >> t3

## 순서적 실행 : t1 >> t2
## 병렬 실행 : [t1, t2]
## 복합적으로 생성 가능 : [t3, t4] >> t2 >> t1 >> [t6, t7]
```
