from confluent_kafka import Consumer,KafkaError,DeserializingConsumer
from confluent_kafka import TopicPartition
import json


def deserialize(topic, data):
    return json.loads(data)

def normal_consumer():
    conf = {'bootstrap.servers': 'localhost:9092','group.id': 'group1','auto.offset.reset':'earliest','enable.auto.commit': False}
    consumer = Consumer(conf)
    consumer.subscribe(['my-topic'])
    while True:
        try:
            msg = consumer.poll(1)
            if msg is None:
                #print(msg.value)
                continue
            your_message = msg.value()
            print(your_message)
        except KeyboardInterrupt:
            break

    consumer.close()

def deserailize_consumer():
    conf={'bootstrap.servers': 'localhost:9092','group.id': 'group1','auto.offset.reset':'earliest','enable.auto.commit': False}
    consumer=DeserializingConsumer(conf)
    consumer.subscribe(['my-topic'])

    while True:
        try:
            msg = consumer.poll(1)
            if msg is None:
                #print(msg.value)
                continue
            your_message = msg.value()
            print(your_message)
        except KeyboardInterrupt:
            break

    consumer.close()

normal_consumer()