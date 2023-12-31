### dw db 테이블 data 를 가공처리후 dm db에 저장할 예정

- 스케쥴을 하나로 엮어서 한 번에 처리할 수 있도록 구성하는 것이 목표

- py 파일 1번

```py
# project_v1_dag.py

from datetime import datetime, timedelta

# DAG 객체 모듈
from airflow import DAG

# 스케쥴 작업 동작 함수(class)
from airflow.operators.bash import BashOperator

d_arg = {
    'owner' : 'admin',
}

# 전체 스케쥴 관리 객체
corona_dag =  DAG(
    dag_id = 'corona_extract',
    default_args = d_arg,
    start_date = datetime(2024, 1, 3),
    dagrun_timeout = timedelta(minutes=5),
    schedule_interval = timedelta(days=1)
)

# 스케쥴 작업을 실시
run_n = BashOperator(
    task_id = 'corona_extract',
    bash_commmand = 'sh /root/study/corona_project/corona_extract.sh',
    dag = cornoa_dag
)
```

### py 파일 2번

- 코로나 현황 데이터를 날짜별로 테이블에 insert 하기 위함.

- spark 를 cluster 를 연결해서 sparkshell 을 open해서 사용하는 프로그램이 아니다.

- spark session과 spark context는 자동 생성이 안된다. -> 생성해서 사용해야 함(코드 필요)

- pyspark를 이용해서 생성하겠다.

    1. 기존 sparksession 이 있으면 초기화 : findspark 모듈이 필요
    2. session을 생성 : pyspark.sql의 SparkSession

```py
import pymysql
from datetime import date, datetime
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import *
import datetime as dt
import pandas as pd
import findspark # pip install findspark
from pyspark.sql import SparkSession

##########################################################################
# 전역변수 영역
# db 서버 정보와 db 정보 : url 키의 value
# 계정정보 : props

JDBC = {
      'url':'jdbc:mysql://localhost:3306/etlmysql?characterEncoding=utf8&serverTimezone=Asia/Seoul'
     ,'props':{
      'user':'bigMysql',
      'password':'bigMysql1234@'   
      }
}

##########################################################################
# 함수영역

# spark session 생성 후 객체 반환하는 함수
def get_spark_session():
    findspark.init() # spark 관련 객체 초기화
    return SparkSession.builder.getOrCreate() # 기존 session 에 있으면 사용 아니면 생성을 반환


# 코로나 환자 data hdfs -> sparkdf 로 load 하는 함수
# 특정 파일명을 파라미터로 받아서 df를 반환하는 함수
# 하루치 data를 가져온다.
def get_data(fileN) :
    file_name = 'hdfs://localhost:9000/corona_data/patient/'+str(fileN)
    spark_sc = get_spark_session()
    p_json = spark.read.json(file_name, encoding='UTF-8')
    return p_json


# 현재 날짜로부터 before_day 만큼 이전의 날짜를 생성해주는 함수
# parm 을 2개 줘서 구할 수도 있다. 
# 현재 날짜가 아닌 특정 날짜 사이의 값을 넣고 추출할 수도 있음.
def cal_std_day(start):
    x = dt.datetime.now() - dt.timedelta(start)
    year = x.year
    month = x.month if x.month >= 10 else '0'+ str(x.month)
    day = x.day if x.day >= 10 else '0'+ str(x.day)  
    return str(year)+ '-' +str(month)+ '-' +str(day)


### 특정일의 json 파일을 추출해서 필요 컬럼 생성후 db에 insert 하는 함수
def transform_data():
    file_name = 'corona_patient_'+cal_std_day(365)+'.json' 
    # corona_extract.py 에서 기준일이 365로 설정되어 있기 때문임.
    data = []
    co_p_json = get_data(file_name)
    for rdd1 in co_p_json.select(co_p_json.items).toLocalIterator() : 
        for rdd2 in rdd1.items:
            data.append(rdd2)

    tmp = get_spark_session().reateDataFrame(data)

    co_p = tmp.select(
        tmp.gubun.alias('LOC'),
        tmp.deathCnt.alias('DEATH_CNT'),
        tmp.defCnt.alias('DEF_CNT'),
        tmp.localOccCnt.alias('LOC_OCC_CNT'),
        tmp.qurRate.alias('QUR_RATE'),
        tmp.stdDay.alias('STD_DAY'))\
        .where(~(col('LOC').isin(['합계', '검역']))).distinct()
    return co_p

# db에 저장하는 역할
def dw_save():
    tm_data = transform_data()
    tm_data.write.jdbc(url = JDBC['url'], table = 'CORONA_PATIENTS', mode = 'append', properties =JDBC['props'])

if __name__ == '__main__':
    dw_save()
```

### py 파일 3번

```py
# corona_transform_dm.py
from datetime import date, datetime
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import SparkSession
import findspark
import datetime as dt
import pandas as pd
# from corona_transform_dw impory get_spark_session # 기존 생성한 함수

## dw db 에서 data(table) 추출 / 변환 후 dm db로 저장한다
## dw와 dm이 서로 다른 db 사용 jdbc 정보가 2개 : 함수로 구성함

# 기준일 생성 함수
def cal_std_day(befor_day):   
    x = dt.datetime.now() - dt.timedelta(befor_day)
    year = x.year
    month = x.month if x.month >= 10 else '0'+ str(x.month)
    day = x.day if x.day >= 10 else '0'+ str(x.day)  
    return str(year)+ '-' +str(month)+ '-' +str(day)

def create_conf():
    conf_dw = {
        'url':'jdbc:mysql://localhost:3306/etlmysql?characterEncoding=utf8&serverTimezone=Asia/Seoul'
        ,'props':{
        'user':'bigMysql',
        'password':'bigMysql1234@'   
        }
    }

    conf_dm = {
        'url':'jdbc:mysql://localhost:3306/etlmysqlDM?characterEncoding=utf8&serverTimezone=Asia/Seoul'
        ,'props':{
        'user':'bigDM',
        'password':'bigDMl1234@'   
        }
    }

    return [conf_dw, conf_dm]

# spark session 생성 후 반환
def get_spark_session():
    findspark.init()
    return SparkSession.bulider.getOrCreate()

# db에서 전달된 table data를 추출
def find_data(config, table_name):
    return spark.read.jdbc(url=config['url'], table = table_name, properties = config['props'])


def find_query(config, query_t):
    spark_sc = get_spark_session
    df = spark_sc.read.format('jdbc')\
                  .option('url', config['url'])\
                  .option('drive', 'com.mysql.cj.jdbc.Driver')\
                  .option('query', query_t)\
                  .option('user', config['props']['user'])\
                  .option('password', config['props']['password'])\
                  .load()
    return df

# 전달된 db 를 db에 저장
def save_data(config, df, table_name):
    return df.write.jdbc(url=config['url'], table = table_name, mode = 'append', properties = config['props'])

# 코로나 현황과 인구의 관계
def transdata_popPatients():
    tmp_q = "select * from CORONA_PATIENTS where STD_DAY = '" + str(cal_std_day(365)) + "'"
    conf = create_conf()
    popu = find_data(conf[0], 'LOC')
    patients = find_query(conf[0], tmp_q) 

    ## 면적대비 인구수와 코로나 현황
    pop_patients = popu.join(patients, on = 'LOC')\
                        .select('LOC',
                            ceil(col('POPULATION')/col('AREA')).alias('popu_density'),
                                'QUR_RATE', 'STD_DAY')\
                        .orderBy('STD_DAY')
    
    # 각 행별로 고유 인덱스 컬럼 추가
    pop_patients = pop_patients .withColumn('CP_IDX', monotonically_increasing_id())

    # DM DB에 저장 - 테이블에 레코드가 insert 문
    save_data(conf[1], pop_patients,'CO_POPU_DENSITY')


# 지역별 인구 10만명당 백신 접종률 계산
def transdata_vaccinePatient():
    conf = create_conf()

    # 인구 data 
    popu = find_data(conf[0], 'LOC')

    # 코로나 현황 data 
    patients = find_data(cconf[0], 'CORONA_PATIENTS')

    # 백신 data 추출
    vaccine = find_data(conf[0], 'CORONA_VACCINE')
   
    vaccine = vaccine \
        .withColumn("V_CNT" ,
              vaccine["V_CNT"]
              .cast(IntegerType()))

    ### Long 형 df => wide 형 df
    ### pivot 사용 : pandas df 로 변환
    pd_vaccine = vaccine.to_pandas_on_spark()
    pd_vaccine.pivot_table(index = ['LOC', 'STD_DAY'], columns = 'V_TH', values = 'V_CNT')
    pd_vaccine = pd_vaccine.reset_index()

    # spark df로 변환
    vaccine = pd_vaccine.to_spark()

    # 인구 10만명당 백신 접종률 계산 - 3차 접종자를 기준으로
    vac_rate = vaccine.join(popu, on = 'LOC')\
                        .select('LOC',
                            'STD_DAY',
                            ceil(col('V3')/col('POPULATION') * 100000).alias('Third_RATE'))


    # 백신 접종 데이터와 코로나 현황 데이터 결합 후 필요한 컬럼만 추출
    co_vaccine =  vac_rate.join(patients, on = ['LOC', 'STD_DAY'])\
                            .select('LOC', 'STD_DAY', 'Third_RATE', 'QUR_RATE')

    # 기준키로 사용할 컬럼 생성
    co_vaccine = co_vaccine.withColumn('CV_IDX', monotonically_increasing_id())

    # data 를 저장해준다.
    save_data(conf[1], co_vaccine, 'CO_VACCINE_THIRD')
    

# 다중 이용시설과 코로나 확진자수 관계
def transdata_FacPatient():
    tmp_q = "select * from CORONA_PATIENTS where STD_DAY = '" + str(cal_std_day(365)) + "'"
    conf = create_conf()
    # 다중이용시설 data
    facil = find_data(conf[0], 'LOC_FACILITY_CNT') 
    # 코로나 확진자 data
    patients = find_data(conf[0], 'CORONA_PATIENTS') 
    # 인구 data
    popu = find_data(conf[0], 'LOC')

    # 인구 10만명 당 다중이용시설의 수
    fac_popu = popu.join(facil, on = 'LOC')\
            .select('LOC', ceil(facil.FAC_CNT/popu.POPULATION*100000).alias('FAC_POPU'))
    co_facil = patients.join(fac_popu, on = 'LOC')\
                    .select('LOC', 'FAC_POPU', 'QUR_RATE', 'STD_DAY')
    # idx 컬럼추가
    co_facil =  co_facil.withColumn('CF_IDX', monotonically_increasing_id())

    save_data(conf[1], co_facil, 'CO_FACILITY')

# 요일별 코로나 확진자수
# 1. 특정일(corona_extract.py 에서 추출한 날짜) 코로나 발생 현황 data 추출
# 2. dmdb의 CO_WEEKDAY tbl에서 가장 최근 기준일의 레코드를 추출
# 3. 1번 데이터의 요일 결정 전국 코로나 증가현황을 계산
# 4. 3번에서 계산한 특정 요일의 코로나 증가현황을 특정 요일의 기존 수와 더하기(특정요일 data 누적 증가)
def transdata_weekPatient():
    tmp_q = "select * from CORONA_PATIENTS where STD_DAY = '" + str(cal_std_day(365)) + "'"
    tmp_qd = 'select * from CO_WEEKDAY where std_day = (select max(std__day) from CO_WEEKDAY)"
    conf = create_conf()
    # 코로나 확진자 data
    patients = find_data(conf[0], 'CORONA_PATIENTS')
    # 기준일을 요일로 변환 : dayofweek(), 요일결정
    week_p = patients.withColumn('DAY_OF_WEEK', dayofweek(col('STD_DAY'))) 
    # 신규발생자 수를 요일별로 계산, 전국 증가 현황 계산
    week_p = week_p.groupby(week_p.DAY_OF_WEEK).agg(sum(col('LOC_OCC_CNT')).alias('patients'))
    # 숫자로 된 요일을 문자로 변경해준다.
    week_p = week_p.withColumn('DAY_OF_WEEK', when(week_p.DAY_OF_WEEK == 1, 'MON')
                                        .when(week_p.DAY_OF_WEEK == 2, 'TUE')
                                        .when(week_p.DAY_OF_WEEK == 3, 'WED')
                                        .when(week_p.DAY_OF_WEEK == 4, 'THR')
                                        .when(week_p.DAY_OF_WEEK == 5, 'FRI')
                                        .when(week_p.DAY_OF_WEEK == 6, 'SAT')
                                        .when(week_p.DAY_OF_WEEK == 7, 'SUN'))
    # week.show() # 요일별 발생현황 table
    # week_p.show() # 특정날짜의 발생현황

    # 특정 요일을 추출 - 4번 코드
    tmp_col = week_p.select(week_p.DAY_OF_WEEK).collect()[0][0]
    # print(tmp_col) # 요일 data 추출한다.
    # 위에서 추출한 요일의 data 를 week에서 추출
    tmp_val = week.select(tmp_col).collect()[0][0] + week.p.select('patients').collect()[0][0]
    # 위에서 계산한 수치를 tmp_col 요일에 반영한다.
    week = week.withcolumn(tmp_col, lit(tmp_val)) # 기준 컬럼 변경
    # print(tmp_val)

    # 피벗 테이블 형태로 바꿔준다.
    # pd_p = week_p.to_pandas_on_spark()
    # pd_p = pd_p.pivot_table(columns = 'DAY_OF_WEEK', values = 'patients')
    # week_p = pd_p.to_spark()

    # week_p.withColumn('STD_DAY', current_date().cast('string')).show()
    week = week.withColumn('STD_DAY', lit(cal_std_day(365)))
    # week_p = week_p.withColumn('STD_DAY', lit(cal_std_day(365)))
    save_data(conf[1], week, 'CO_WEEKDAY')

if __name__ == '__main__':
    transdata_popPatient()
    transdata_vaccinePatient()
    transdata_FacPatient()
    transdata_weekPatient()
```
