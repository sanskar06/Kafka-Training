CSV to KAFKA-TOPIC 

Step1: Docker-compose.yml:- 

Step2:Go to Terminal of kafka-connect when it is started inside it  

Cd / 

Ls  

Cd/data/unprocessed ---> {this should be in our folder structure} 

Cd/data/processed ---> {this should be in our folder structure} 

Inside uprocessed --->there should be file with .csv extension  

Step3: run  

curl -s localhost:8083/connector-plugins 

	 

"com.github.jcustenborder.kafka.connect.spooldir.SpoolDirCsvSourceConnector" 
"com.github.jcustenborder.kafka.connect.spooldir.SpoolDirJsonSourceConnector" 
"com.github.jcustenborder.kafka.connect.spooldir.SpoolDirLineDelimitedSourceConnector" 
"com.github.jcustenborder.kafka.connect.spooldir.SpoolDirSchemaLessJsonSourceConnector" 
"com.github.jcustenborder.kafka.connect.spooldir.elf.SpoolDirELFSourceConnector" 


Step3: Loading data from CSV into Kafka and applying a schema 

curl -i -X PUT -H "Accept:application/json" \ 
   		  -H  "Content-Type:application/json" http://localhost:8083/connectors/source-    		            csv-spooldir-00/config \ 
   -d '{"connector.class":"com.github.jcustenborder.kafka.connect.spooldir.SpoolDirCsvSourceConnect, 
        "topic": "orders_spooldir_00", 
        "input.path": "/data/unprocessed", 
        "finished.path": "/data/processed", 
        "error.path": "/data/error", 
        "input.file.pattern": ".*\\.csv", 
        "schema.generation.enabled":"true", 
        "csv.first.row.as.header":"true" 
        }' 

This will get register and csv file will move to processed folder and this will get register in the schema-registry in avro format  

Step 4: To look for that csv data we can use the confluent kakfa : 

Before you need to know the subject and the id of schema where it will get register 

Curl http://localhost:8081/subjects --> this will tell the subjects  

Curl http://localhost:8081/subjects/<your subject name >/versions/latest --> by this we will get the details and id  

Now : run the python file given below to fetch the csv file from topic: 

 

 

from confluent_kafka import DeserializingConsumer 

import json 

from confluent_kafka.schema_registry.schema_registry_client import SchemaRegistryClient  

from confluent_kafka.schema_registry.avro import AvroDeserializer 

schema_registry = SchemaRegistryClient({'url': "http://localhost:8081"}) 

schema=schema_registry.get_schema(1) 

avro_deserializer = AvroDeserializer(schema_registry_client=schema_registry,schema_str=schema.schema_str) 

conf={'bootstrap.servers':"localhost:9092",'value.deserializer': avro_deserializer,'auto.offset.reset': 'earliest','group.id': 'your_group','enable.auto.commit':False} 

consumer = DeserializingConsumer(conf) 

consumer.subscribe(topics=['orders_spooldir_00']) 

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

 
 
 
 

 

Now to Delete the connector we have to use the curl command: 

---> curl -s -X DELETE http://localhost:8083/connectors/source-csv-spooldir-00 

To get the connector name 

--> curl http://localhost:8083/connectors 

 

 

 

 

 

 

------------------------------------------------------------------------------------------------------------------------------------------ 

Now if we wants to add the custom generators then: 

Step1:   

curl -i -X PUT -H "Accept:application/json" \ 
    -H  "Content-Type:application/json" http://localhost:8083/connectors/source-csv-spooldir-02/config \ 
    -d '{ 
        "connector.class": "com.github.jcustenborder.kafka.connect.spooldir.SpoolDirCsvSourceConnector", 
        "topic": "orders_spooldir_02", 
        "input.path": "/data/unprocessed", 
        "finished.path": "/data/processed", 
        "error.path": "/data/error", 
        "input.file.pattern": ".*\\.csv", 
        "schema.generation.enabled":"true", 
        "schema.generation.key.fields":"order_id", 
        "csv.first.row.as.header":"true", 
        "transforms":"castTypes", 
        "transforms.castTypes.type":"org.apache.kafka.connect.transforms.Cast$Value", 
        "transforms.castTypes.spec":"order_id:int32,customer_id:int32,order_total_usd:float32" 
        }' 

After running this --> 

{tranforms.castTypes.spec by this we can give the data type according to our need} 

Step2  

see the schema we are created: 

---> curl --silent --location --request GET 'http://localhost:8081/subjects/orders_spooldir_02-value/versions/latest 

 

------------------------------------------------------------------------------------------------------------------------------------------ 

 

Using the value convertor: 

curl -i -X PUT -H "Accept:application/json" \ 
    -H  "Content-Type:application/json" http://localhost:8083/connectors/source-csv-spooldir-03/config \ 
    -d '{ 
        "connector.class": "com.github.jcustenborder.kafka.connect.spooldir.SpoolDirLineDelimitedSourceConnector", 
        "value.converter":"org.apache.kafka.connect.storage.StringConverter", 
        "topic": "orders_spooldir_03", 
        "input.path": "/data/unprocessed", 
        "finished.path": "/data/processed", 
        "error.path": "/data/error", 
        "input.file.pattern": ".*\\.csv" 
        }' 

 

 