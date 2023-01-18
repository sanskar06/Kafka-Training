from kafka import KafkaAdminClient
from kafka.admin import NewTopic
admin_client = KafkaAdminClient(bootstrap_servers='localhost:9092')

admin_client.create_topics(new_topics=
    [
        NewTopic(
            name='schema_value',
            num_partitions=1,
            replication_factor=1
        )
    ]
)
