# kafka_prod_test.py

- 코드로 공급자 생성 예제

```py
from confluent_kafka import Producer # 공급자 생성 모듈


def delivery_report(self, msg, err=None) : # call back 함수 생성
    if err is not None :
        print('Message delivery failed:{}'.format(err))
    else : 
        print('Message delivered to {} [{}]'.format(msg.topic(),msg.partition()))
```

# kafka_client_test.py

- 데이터가 있는 동안~

```py

# kafka_client_test.py

from confluent_kafka import Consumer # 공급받는자 생성 모듈

if __name__ == '__main__' :
    # consumer 설정 파라미터
    conf = {
        'bootstrap.servers' : 'localhost:9092',
        'group.id':'test-group',
        'auto.offset.reset':'earliest'
    }

    # 공급받는자 생성
    consumer = Consumer(conf)

    # topic 설정 : Consumer.subscribe([topic list])
    consumer.subscribe(["my-kafka-topic"])

    running = True
    while(running) : 
        msg = consumer.poll(timeout=1.0) # 데이터 받기
        if msg is None : continue

        if msg.error() : # 전달받은 msg에 에러 코드가 있으면
            print(msg.error()) # 에러내용 출력
        else:
            print(msg.value().decode('utf-8'))

    consumer.close()
```
