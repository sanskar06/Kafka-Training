from confluent_kafka import Consumer

consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group-id',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': False
}

consumer = Consumer(consumer_conf)

message_topic = 'my-topic'
consumer.subscribe([message_topic])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print(msg.value())
