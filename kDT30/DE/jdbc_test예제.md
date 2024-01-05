```py
import pymysql
from datetime import date, datetime
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import *
import datetime as dt
import pandas as pd 
import findspark
from pyspark.sql import SparkSession

def create_conf() :
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
        'password':'bigDM1234@'   
        }
    }
    return [conf_dw, conf_dm]

# spark session 생성 후 반환 
def get_spark_session() :
    findspark.init()
    return SparkSession.builder.getOrCreate()

# db에서 전달된 table data를 추출
def find_data(config, table_name) :
    spark_sc = get_spark_session()
    return spark_sc.read.jdbc(url= config['url'], table=table_name, properties=config['props'])


# db 정보 호출
conf = create_conf()

spark_sc = get_spark_session()

# CORONA_PATIENTS 테이블의 모든 data 추출 (select * from CORONA_PATIENTS)
# spark_sc.read.jdbc(url = conf[0]['url'], table = 'CORONA_PATIENTS', properties = [0]['props'])


# dwdb(etlmysql)에서 코로나 현황(CORONA_PATIENTS 테이블) 1년 전 날짜에 해당하는 레코드만 추출해서 read
tmp_q = "select * from CORONA_PATIENTS where STD_DAY = '2022-12-31'"
# spark.read.format() : 여러 포맷의 data 추출이 가능하다.
# 왜 굳이 format을 사용? -> option 설정이 가능하다.
df = spark_sc.read.format('jdbc')\
                  .option('url', conf[0]['url'])\
                  .option('drive', 'com.mysql.cj.jdbc.Driver')\
                  .option('query', tmp_q)\
                  .option('user', conf[0]['props']['user'])\
                  .option('password', conf[0]['props']['password'])\
                  .load()


# dwdb(etlmysql)에서 db 내 idx 값이 들어 있는 테이버릉에서 가장큰 idx 값을 추출
tmp_q = "select max(CF_IDX) from CO_FACILITY"
# spark.read.format() : 여러 포맷의 data 추출이 가능하다.
# 왜 굳이 format을 사용? -> option 설정이 가능하다.
df = spark_sc.read.format('jdbc')\
                  .option('url', conf[0]['url'])\
                  .option('drive', 'com.mysql.cj.jdbc.Driver')\
                  .option('query', tmp_q)\
                  .option('user', conf[0]['props']['user'])\
                  .option('password', conf[0]['props']['password'])\
                  .load()
```
