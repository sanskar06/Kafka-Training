from confluent_kafka import SerializingProducer
import json
from confluent_kafka.schema_registry.schema_registry_client import SchemaRegistryClient 
from confluent_kafka.schema_registry.json_schema import JSONSerializer

schema_registry = SchemaRegistryClient({'url': "http://localhost:8085"})


schema = '{"type": "record", "name": "User_Salary","title":"JSON_Schema_Salary", "fields": [{"name": "Name", "type": "string"}, {"name": "Salary", "type": "int"}]}'
json_serializer = JSONSerializer(schema_registry_client=schema_registry,schema_str=str(schema),conf={'auto.register.schemas':True})
conf={'bootstrap.servers':"localhost:9092",'value.serializer': json_serializer}

producer = SerializingProducer(conf)
def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

producer.produce(topic='schema-value', value={'Name': 'sanskar', 'Salary': 25000}, on_delivery=delivery_report)
producer.flush()
producer.poll(1)
#curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" --data '{"schema":{\"type\": \"record\", \"name\": \"User_Salary\",\"title\":\"JSON_Schema_Salary\", \"fields\": [{\"name\": \"Name\", \"type\": \"string\"}, {\"name\": \"Salary\", \"type\": \"int\"}]}' http://localhost:8085/subjects//versions