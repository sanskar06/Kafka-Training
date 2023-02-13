from confluent_kafka import Producer, SerializingProducer
from confluent_kafka.serialization import StringSerializer
import confluent_kafka
import os,time



def call(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg.value())))

conf = {
    "bootstrap.servers": 'localhost:9092',
    "key.serializer": StringSerializer(),
    "value.serializer": StringSerializer(),
    "transactional.id": "my-transactional-id",
    # "enable.idempotence":True,
    # "acks":"all"
}

producer = SerializingProducer(conf)
producer.init_transactions()
producer.begin_transaction()
for i in range(20,40):
    time.sleep(2)
    producer.produce(
        "my-topic",
        key="serialized_key",
        value=f" hello world {i} ",
        on_delivery=call,
    )
    producer.flush()

producer.commit_transaction()
