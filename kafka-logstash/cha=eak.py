from kafka import KafkaConsumer
from kafka import TopicPartition
import json


def consumer_func():
    consumer1 = KafkaConsumer('logstash-0',bootstrap_servers=['localhost:9092'],auto_offset_reset='earliest')
    for msg in consumer1:
        print(msg.value)

consumer_func()