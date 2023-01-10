from kafka import KafkaConsumer
from kafka import TopicPartition
import json


def consumer_func():
    consumer1 = KafkaConsumer('my-topic',bootstrap_servers=['localhost:9092'],auto_offset_reset='earliest',consumer_timeout_ms=5000)
    for msg in consumer1:
        print(msg.value)
def consumer_assign():
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092',auto_offset_reset='earliest')
    consumer.assign([TopicPartition('my-topic', 1)])
    msg = next(consumer) 
    print(msg)       
def consumer_subscribe():
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092',auto_offset_reset='earliest')
    consumer.subscribe(['my-topic'])
    for msg in consumer:
        print(msg.value)
def consumer_deserializer():
    consumer=KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')),auto_offset_reset='earliest')
    consumer.subscribe(['my-topic'])
    for msg in consumer:
        print(msg.value)
consumer_deserializer()