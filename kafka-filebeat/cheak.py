from kafka import KafkaConsumer
from kafka import TopicPartition
import json


def consumer_func():
    consumer1 = KafkaConsumer('log',bootstrap_servers=['localhost:9092'],auto_offset_reset='earliest',consumer_timeout_ms=5000)
    for msg in consumer1:
        print(msg.value)

consumer_func()