### kafka install

- 필요 소스 다운
- wget https://dlcdn.apache.org/kafka/3.4.1/파일명

> (wget https://dlcdn.apache.org/kafka/3.4.1/kafka_2.13-3.4.1.tgz)

### 압축해제, 바로가기 생성

- 압축해제 : tar -xzf kafka_2.13-3.4.1 tgz

- 바로가기 생성 : ln -s kafka_2.13-3.4.1 kakfa

- kafka 환경 설정

  - cd

  - vim ~/.bashrc

  - esc i (편집모드)

```aw
# 마지막에 추가
# 카프카 관리 ZOOKEEPER 프로그램의 HOME 생성
# 카프카 홈생성

# zookeeper path
ZOOKEEPER_HOME=/root/kafka
PATH=$PATH:$ZOOKEEPER_HOME/bin
export PATH

# kafka
KAFKA_HOME=/root/kafka
PATH=$PATH:$KAFKA_HOME/bin
```

- esc :wq

- source ~/.bashrc

### 카프카 기본 설정

- KAFKA_HOME/config/server.properies 파일(kafka 서버 설정)

  - topic(브로커한테 제공하는 데이터의 이름) 에 대해서 삭제가능하도록 변경해준다.

  - 응답자 주소를 서버에 설정

  - cd
  - cd kafka_2.13-3.4.1/config
  - vim server.properties

  - 아래 내용 주석 해제 ip를 localhost 로 변경
  
  - 가장 하단에 아래 내용을 추가
  
  - delete.topic.enable=true

### 카프카 설치 완료됨

### kafka 실행 관련

- cd ~/kafka_2.13-3.4.1 로 이동

### zookeeper 가 먼저 실행되어야 함(관리프로그램)

- ./bin/zookeeper-server-start.sh ./config/zookeeper.properties &

### kafka 실행(독립 터미널에서 실행)

- ./bin/kafka-server-start.sh ./config/server.properties &

### 프로그램 실행 시 속성파일 참고
