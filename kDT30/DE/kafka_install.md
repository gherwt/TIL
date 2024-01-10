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

## kafka : data 이동(흐름) 관리하는 프로그램

- 물리적으로는 전달된 메세지(topic, data) 를 관리하는 서버

## zookeeper : kafka 관리 프로그램

### kafka 실행 관련

- cd ~/kafka_2.13-3.4.1 로 이동

### zookeeper server 가 먼저 실행되어야 함(관리프로그램)

- sh ./bin/zookeeper-server-start.sh ./config/zookeeper.properties &

### kafka server 실행(독립 터미널에서 실행)

- bin/kafka-server-start.sh config/server.properties &

### 프로그램 실행 시 속성파일 참고

## kafka 역할

- 데이터를 공급자가 우너할 떄 공급받아서 보관하고 있다가 공급받는 자가 요청 시 전달해준다.

- data 를 topic 이라는 개념으로 관리한다
  - topic은 여러 개의 그룹일 수도 있고 하나의 데이터를 쪼갠 데이터 부분일 수도 있다.
  - topic은 메시지 단위로 관리가 된다.

- topic 생성 : topic 은 생성하게 되면 명시적으로 삭제하지 않는 한 계속 유지되게 된다. 즉 , topic 명은 중복될 수 없다.

- 생성된 topic에 procedure 는 데이터를 실어서 kafka 에게 전달
- consumer 는 kafka 의 topic을 요청해서 사용하게 됨

## topic 생성 명령 프로그램 (sh 프로그램)

- 새 터미널에서 실행

```aw
# 새 터미널에서 실행
cd kafka

/bin/kafka-topic.sh --create --topic 토픽명 --bootstrap 서버주소 --partitions 파티션 수 --replication-factor 파티션수

/bin/kafka-topic.sh --create --topic my-kafka-topic --bootstrap localhost:9092 --partitions 1 --replication-factor 1

# Created topic my-kafka-topic. 생성완료 문구

# 생성되고 관리되는 topic list 확인
./bin/kafka-topic.sh --bootstrap-server 서버주소 --list
./bin/kafka-topic.sh --bootstrap-server localhost:9092 --list

# 공급자 생성(데이터 상황별로 생성)
cd ~/kafka
./bin/kafka-console-producer.sh --topic 토픽명 --bootstrap-server 카프카 서버주소
./bin/kafka-console-producer.sh --topic my-kafka-topic --bootstrap-server localhost:9092

# 공급받는자 생성(필요한 데이터(topic)를 명시해서 공급받음
./bin/kafka-console-consumer.sh --topic my-kafka-topic --bootstrap-server localhost:9092
```
