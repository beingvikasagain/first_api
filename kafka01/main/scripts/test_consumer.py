import json

from confluent_kafka import Consumer
from decouple import config

from kafka01.kafka_api import ConfluentKafkaApi


def run():
    conf = ConfluentKafkaApi.read_config()
    conf['group.id']="kafka01_testing"
    conf['auto.offset.reset']='earliest'
    # conf['max.poll.interval.ms']=3600

    consumer = Consumer(conf)
    consumer.subscribe([config('KAFKA_TESTING_TOPIC')])

    try:
        while True:
            msg = consumer.poll(1)
            if msg and not msg.error():
                data = json.loads(msg.value())
                if data:
                    print(data)
                else:
                    print("no data!")

    except Exception as e:
        print(str(e))

