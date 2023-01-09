from kafka import  KafkaProducer
import os
BOOTSTRAP_SERVER=os.environ.get('KAFKA_BOOTSTRAP_SERVER')
print(BOOTSTRAP_SERVER)
producer1 = KafkaProducer(bootstrap_servers=['localhost:9092'])
producer1.send('my-topic', b'This is 2nd message')
producer1.flush()

