import json

from confluent_kafka import Producer
from decouple import config


class ConfluentKafkaApi:
    @staticmethod
    def read_config():
        conf = {
            "bootstrap.servers": config("KAFKA_SERVER"),
            "security.protocol": config("KAFKA_PROTOCOL"),
            "sasl.mechanisms": config("KAFKA_MECHANISM"),
            "sasl.username": config("KAFKA_USERNAME"),
            "sasl.password": config("KAFKA_PASSWORD"),
        }
        return conf
    @staticmethod
    def send_data(data, topic, headers=None):
        producer = Producer(ConfluentKafkaApi.read_config())
        try:
            data = json.dumps(data)
            
            producer.produce(topic, value=data, headers=headers)
        except Exception as e:
            print(str(e))
        finally:
            producer.flush()
