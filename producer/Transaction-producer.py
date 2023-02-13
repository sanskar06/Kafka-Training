from confluent_kafka import Producer,SerializingProducer
from confluent_kafka.serialization import StringSerializer
import socket
import json

conf = {'bootstrap.servers': "localhost:9092",'transactional.id': 'temp_transaction_id'} 
producer = Producer(conf)

producer.init_transactions()
producer.begin_transaction()


message_value = 'your message value here'
message_key = 'your message key here'
message_topic = 'my-topic'
# headers = [('transactional.id', 'your.transactional.id.here')]

producer.produce(
    topic=message_topic,
    value=message_value,
    key=message_key,
    
)
producer.commit_transaction()