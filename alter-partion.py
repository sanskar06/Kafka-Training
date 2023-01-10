from kafka import KafkaAdminClient
from kafka.admin.new_partitions import NewPartitions
client=KafkaAdminClient(bootstrap_servers='localhost:9092')
rsp = client.create_partitions({'my-topic': NewPartitions(3)})
print(rsp)