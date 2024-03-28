from decouple import config

from kafka01.kafka_api import ConfluentKafkaApi


def run():
    data = {
        "name":'manish',
        "address":"mumbai",
        "age":"32"
    }
    ConfluentKafkaApi.send_data(data, config('KAFKA_TESTING_TOPIC'))