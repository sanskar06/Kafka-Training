from confluent_kafka import SerializingProducer
import json
from confluent_kafka.schema_registry.schema_registry_client import SchemaRegistryClient

#from confluent_kafka.schema_registry.avro import AvroSerializer

schema_registry = SchemaRegistryClient({'url': "http://localhost:8085"})
#avro_serializer = AvroSerializer(schema_registry_client=schema_registry,schema_str='schema_str')

schema = {
    'type': 'record',
    'name': 'User',
    'fields': [
        {'name': 'name', 'type': 'string'},
        {'name': 'age', 'type': 'int'}
    ]
}
schema_id = schema_registry.register_schema('topic-2', schema)



conf={'bootstrap.servers':"localhost:9092",'schema.registry.url':"http://localhost:8085"}

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def serialize(topic, message):
    return json.dumps(message).encode()

def deserialize(topic, data):
    return json.loads(data)

producer = SerializingProducer(conf,value_serializer=serialize)
producer.produce(topic='my-topic', value={'name': 'John', 'age': 30}, key='user1', callback=delivery_report,schema_id=schema_id)
producer.flush()
