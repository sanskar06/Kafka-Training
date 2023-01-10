from kafka import KafkaAdminClient
from kafka.admin.new_partitions import NewPartitions
client=KafkaAdminClient(bootstrap_servers='localhost:9092')
rsp = client.create_partitions({'my-topic': NewPartitions(3)})
<<<<<<< HEAD:alter-partion.py

=======
print(rsp)
>>>>>>> 5708bc94867103659fa54a2d52de4da0b976c70b:topics/alter-partion.py
