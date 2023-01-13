from confluent_kafka import DeserializingConsumer
import json
from confluent_kafka.schema_registry.schema_registry_client import SchemaRegistryClient 
from confluent_kafka.schema_registry.avro import AvroDeserializer

schema_registry = SchemaRegistryClient({'url': "http://localhost:8085"})
schema=schema_registry.get_schema(1)
avro_deserializer = AvroDeserializer(schema_registry_client=schema_registry,schema_str=schema.schema_str)
conf={'bootstrap.servers':"localhost:9092",'value.deserializer': avro_deserializer,'auto.offset.reset': 'earliest','group.id': 'your_group','enable.auto.commit':False}
consumer = DeserializingConsumer(conf)
consumer.subscribe(topics=['my-topic-value'])
while True:
    try:
        msg = consumer.poll(1)
        if msg is None:
            continue
        your_message = msg.value()
        print(your_message)
    except KeyboardInterrupt:
        break
consumer.close()




