from kafka import  KafkaProducer
import json


def producer_with_keys():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send('my-topic', key=b'key1', value=b'value1')
    producer.send('my-topic', key=b'key2', value=b'value2')
    producer.flush()

def producer_with_value_serializer():
    producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer.send('my-topic', 'this is a serilized message')
    producer.flush()

def producer_with_key_serializer():
    producer = KafkaProducer(key_serializer=str.encode)
    producer.send('my-topic', key='key', value=b'1234')

producer_with_value_serializer()

